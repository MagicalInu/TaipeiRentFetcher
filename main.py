
# Import stuffs, and notify user if dependencies are missing.
import sys

try:
    import pandas as pd
except ImportError:
    print('Pandas not installed')
    print('Please install all the dependencies of this project by using following command:')
    print('pip install -r requirements.txt')

try:
    from PyQt6 import QtWidgets, uic
    from PyQt6.QtCore import QAbstractTableModel, Qt


except ImportError:
    print('PyQt6 not installed!')
    print('Please install all the dependencies of this project by using following command:')
    print('pip install -r requirements.txt')

try:
    from window import Ui_MainWindow as mainWin_UI
    from searchWin import Ui_MainWindow as searchWin_UI

except ImportError:
    print('File missing!')
    print('Please make sure that you have downloaded the full version of Taipei RentFetcher.')

# Global Search Var
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
dfOrg = pd.read_html(url)
print('Loaded! Creating dataframe...')


for i in dfOrg:

    i.columns = i.iloc[0]
    i['坪數'] = i['坪數'].str.replace('\D+', '')
    i['租金'] = i['租金'].str.replace('\D+', '')

    i.rename(columns = {'坪數':'坪數 (坪)', '租金':'租金 (元)'}, inplace = True)
    edited = i[1:]

    df.append(edited)
print(f'Dataframe created! Total pages {len(df)}')
page = 0

class searchWin(QtWidgets.QMainWindow, searchWin_UI):
    def __init__(self, *args, obj=None, **kwargs):

        super(searchWin, self).__init__(*args, **kwargs)

        # Initialize the UI
        self.setupUi(self)

        self.apply.clicked.connect(lambda: self.applyCond())

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
            useLowestPriceVar = True

            print(f'Lowest price set to: {lowestPriceVar}')

        if self.useHighestPrice.isChecked() == True:
            highestPriceVar = self.highestPrice.value()
            useHighestPriceVar = True

        if self.useLowestSize.isChecked() == True:
            lowestSizeVar = self.lowestPrice.value()
            useLowestSizeVar == True

        if self.useHighestSize.isChecked() == True:
            highestSizeVar = self.highestSize.value()
            useHighestSizeVar == True

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

        self.s = None

        super(mainWindow, self).__init__(*args, **kwargs)

        # Initialize the UI
        self.setupUi(self)

        # Connect buttons to functions
        self.nextPageButton.clicked.connect(lambda: self.nextPage())
        self.prevPageButton.clicked.connect(lambda: self.prevPage())
        self.searchConButton.clicked.connect(lambda: self.searchCond())
        self.searchButton.clicked.connect(lambda: self.searchFunc(page))

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

    def searchFunc(self, pg):
        global searchResult
        global df

        temp1 = []
        temp2 = []
        temp3 = []
        temp4 = []
        searchResult = []

        for i in df:
            if all(item is False for item in [useHighestPriceVar, useLowestPriceVar, useHighestSizeVar, useLowestSizeVar]):
                continue
            else:
                if useLowestPriceVar == True:
                    i['lowPriceMatch'] = i['租金 (元)'].str.find(lowestPriceVar)
                    temp1.append(i.query('lowPriceMatch==0'))
                else:
                    temp1.append(i)
                if useHighestPriceVar == True:
                    temp1['highPriceMatch'] = temp1['租金 (元)'].str.find(highestPriceVar)
                    temp2.append(temp1.query('highPriceMatch==0'))
                else:
                    temp2.append(temp1)
                if useLowestSizeVar == True:
                    temp2['lowSizeMatch'] = temp2['坪數 (坪)'].str.find(lowestSizeVar)
                    temp3.append(temp2.query('highPriceMatch==0'))
                else:
                    temp3.append(temp2)
                if useHighestSizeVar == True:
                    temp3['highSizeMatch'] = temp3['坪數 (坪)'].str.find(highestSizeVar)
                    temp4.append(temp3.query('highPriceMatch==0'))
                else:
                    temp4.append(temp3)

            searchResult.append(pd.concat(temp4))
            print(searchResult)

# Main function
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()

    window.show()
    # searchWindow.show()

    window.fetchData(df, 0)

    sys.exit(app.exec())
