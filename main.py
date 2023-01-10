
# Import stuffs, and notify user if dependencies are missing.
import sys

try:
    import pandas as pd
except ImportError:
    print('Pandas not installed!')
    print('Please install all the dependencies of this project by using following command:')
    print('pip install -r requirements.txt')
    exit()

try:
    from PyQt6 import QtWidgets, uic
    from PyQt6.QtCore import QAbstractTableModel, Qt

except ImportError:
    print('PyQt6 not installed!')
    print('Please install all the dependencies of this project by using following command:')
    print('pip install -r requirements.txt')
    exit()

try:
    from window import Ui_MainWindow as mainWin_UI
    from searchWin import Ui_MainWindow as searchWin_UI

except ImportError:
    print('File missing!')
    print('Please make sure that you have downloaded the full version of Taipei RentFetcher.')
    exit()

# Global Var
lowestPriceVar = 0
highestPriceVar = 0
lowestSizeVar = 0
highestSizeVar = 0

useLowestPriceVar = False
useHighestPriceVar = False
useLowestSizeVar = False
useHighestSizeVar = False

searchOpen = False

df = []
searchResult = []

# Import datas
url = 'https://rent.housefun.com.tw/rentprice/printlist.aspx?sid=144722453'
print('Loading data from: rent.housefun.com.tw ...')
try:
    dfOrg = pd.read_html(url)
except ValueError:
    print('Internet Error!')
    print('TaipeiRentFetcher require Internet to function normally.')
    exit()

print('Loaded! Creating dataframe...')


for i in dfOrg:

    i.columns = i.iloc[0]
    i['坪數'] = i['坪數'].map(lambda x: x.rstrip('坪'))
    i['租金'] = i['租金'].map(lambda x: x.rstrip('元').replace(',',''))

    i.rename(columns = {'坪數':'坪數 (坪)', '租金':'租金 (元)'}, inplace = True)

    edited = i[1:]
    edited['坪數 (坪)'] = edited['坪數 (坪)'].astype(float)
    edited['租金 (元)'] = edited['租金 (元)'].astype(int)
    edited['成交時間'] = pd.to_datetime(edited['成交時間'])
    edited['成交時間'] = edited['成交時間'].dt.date
    df.append(edited)
print(f'Dataframe created! Total pages {len(df)}')
page = 0

class searchWin(QtWidgets.QMainWindow, searchWin_UI):
    def __init__(self, *args, obj=None, **kwargs):

        super(searchWin, self).__init__(*args, **kwargs)

        # Initialize the UI
        self.setupUi(self)

        self.apply.clicked.connect(lambda: self.applyCond())
        self.reset.clicked.connect(lambda: self.resetCond())

    def resetCond(self):
        global useLowestSizeVar
        global useHighestSizeVar
        global useLowestPriceVar
        global useHighestPriceVar

        global lowestSizeVar
        global highestSizeVar
        global lowestPriceVar
        global highestPriceVar

        useLowestPriceVar = False
        useHighestSizeVar = False
        useLowestPriceVar = False
        useHighestPriceVar = False

        lowestSizeVar = 0
        highestSizeVar = 0
        lowestPriceVar = 0
        highestPriceVar = 0

        self.lowestSize.setValue(lowestSizeVar)
        self.highestSize.setValue(highestSizeVar)
        self.lowestPrice.setValue(lowestPriceVar)
        self.highestPrice.setValue(highestPriceVar)

        self.useLowestSize.setChecked(useLowestSizeVar)
        self.useHighestSize.setChecked(useHighestSizeVar)
        self.useLowestPrice.setChecked(useLowestPriceVar)
        self.useHighestPrice.setChecked(useHighestPriceVar)
        
    def applyCond(self):

        global useLowestSizeVar
        global useHighestSizeVar
        global useLowestPriceVar
        global useHighestPriceVar

        global lowestSizeVar
        global highestSizeVar
        global lowestPriceVar
        global highestPriceVar

        if self.useLowestPrice.isChecked() == True:
            lowestPriceVar = self.lowestPrice.value()
            print(type(lowestSizeVar))
            useLowestPriceVar = True

            print(f'Lowest price set to: {lowestPriceVar}')
        else:
            useLowestPriceVar = False


        if self.useHighestPrice.isChecked() == True:
            highestPriceVar = self.highestPrice.value()
            useHighestPriceVar = True
        else:
            useHighestPriceVar = False

        if self.useLowestSize.isChecked() == True:
            lowestSizeVar = self.lowestPrice.value()
            useLowestSizeVar == True
        else:
            useLowestSizeVar == False


        if self.useHighestSize.isChecked() == True:
            highestSizeVar = self.highestSize.value()
            useHighestSizeVar == True
        else:
            useHighestSizeVar == False

    def closeEvent(self, event):

        global searchOpen

        searchOpen = False
        event.accept()




# Custom Table Model for Pandas
class pdModel(QAbstractTableModel):

    global page

    def __init__(self, data):
        super(pdModel, self).__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole:
                return str(self._data.iloc[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self._data.columns[col]
        return None

class mainWindow(QtWidgets.QMainWindow, mainWin_UI):

    def __init__(self, *args, obj=None, **kwargs):

        global page
        global df

        self.s = None

        super(mainWindow, self).__init__(*args, **kwargs)

        # Initialize the UI
        self.setupUi(self)

        # Connect buttons to functions
        self.resetButton.clicked.connect(lambda: self.fetchData(df, 0))
        self.nextPageButton.clicked.connect(lambda: self.nextPage())
        self.prevPageButton.clicked.connect(lambda: self.prevPage())
        self.searchConButton.clicked.connect(lambda: self.searchCond())
        self.searchButton.clicked.connect(lambda: self.searchFunc())

    def fetchData(self, data, pg):
        model = pdModel(data[pg])
        self.tableView.setModel(model)
    def nextPage(self):
        global page
        global df

        if page < len(df)-1:
            page += 1

        self.fetchData(df, page)

    def prevPage(self):
        global page
        global df

        if page > 0:
            page -= 1

        self.fetchData(df, page)

    def searchCond(self):

        global useLowestSizeVar
        global useHighestSizeVar
        global useLowestPriceVar
        global useHighestPriceVar

        global lowestSizeVar
        global highestSizeVar
        global lowestPriceVar
        global highestPriceVar

        global searchOpen

        if searchOpen == False:
            self.s = searchWin()

            self.s.lowestSize.setValue(lowestSizeVar)
            self.s.highestSize.setValue(highestSizeVar)
            self.s.lowestPrice.setValue(lowestPriceVar)
            self.s.highestPrice.setValue(highestPriceVar)

            self.s.useLowestSize.setChecked(useLowestSizeVar)
            self.s.useHighestSize.setChecked(useHighestSizeVar)
            self.s.useLowestPrice.setChecked(useLowestPriceVar)
            self.s.useHighestPrice.setChecked(useHighestPriceVar)

            self.s.show()
            searchOpen = True

        else:
            self.s.close()
            searchOpen = False

    def searchFunc(self):
        global searchResult
        global df

        searchResult = []

        df_comp = pd.concat(df)


        if all(item is False for item in [useHighestPriceVar, useLowestPriceVar, useHighestSizeVar, useLowestSizeVar]):
            searchResult = df
            pass

        else:
            if useLowestPriceVar == True:
                df_comp = df_comp[df_comp['租金 (元)'] >= lowestPriceVar]

            if useHighestPriceVar == True:
                df_comp = df_comp[df_comp['租金 (元)'] <= highestPriceVar]

            if useLowestSizeVar == True:
                df_comp = df_comp[df_comp['坪數 (坪)'] >= lowestSizeVar]

            if useHighestSizeVar == True:
                df_comp = df_comp[df_comp['坪數 (坪)'] <= highestSizeVar]

            searchResult.append(df_comp)


        print(df_comp)
        self.fetchData(searchResult, 0)

# Main function
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()

    window.show()
    # searchWindow.show()

    window.fetchData(df, 0)

    sys.exit(app.exec())
