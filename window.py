# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 981, 581))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.welcomePage = QtWidgets.QWidget()
        self.welcomePage.setObjectName("welcomePage")
        self.label = QtWidgets.QLabel(self.welcomePage)
        self.label.setGeometry(QtCore.QRect(322, 20, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.welcomePage)
        self.textBrowser.setGeometry(QtCore.QRect(8, 100, 961, 441))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.welcomePage)
        self.label_2.setGeometry(QtCore.QRect(442, 70, 95, 18))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.welcomePage, "")
        self.DataFetcher = QtWidgets.QWidget()
        self.DataFetcher.setObjectName("DataFetcher")
        self.resetButton = QtWidgets.QPushButton(self.DataFetcher)
        self.resetButton.setGeometry(QtCore.QRect(10, 10, 241, 71))
        self.resetButton.setObjectName("resetButton")
        self.prevPageButton = QtWidgets.QPushButton(self.DataFetcher)
        self.prevPageButton.setGeometry(QtCore.QRect(10, 90, 241, 71))
        self.prevPageButton.setObjectName("prevPageButton")
        self.nextPageButton = QtWidgets.QPushButton(self.DataFetcher)
        self.nextPageButton.setGeometry(QtCore.QRect(10, 170, 241, 71))
        self.nextPageButton.setObjectName("nextPageButton")
        self.tableView = QtWidgets.QTableView(self.DataFetcher)
        self.tableView.setGeometry(QtCore.QRect(260, 10, 711, 531))
        self.tableView.setObjectName("tableView")
        self.searchButton = QtWidgets.QPushButton(self.DataFetcher)
        self.searchButton.setGeometry(QtCore.QRect(10, 390, 241, 71))
        self.searchButton.setObjectName("searchButton")
        self.searchConButton = QtWidgets.QPushButton(self.DataFetcher)
        self.searchConButton.setGeometry(QtCore.QRect(10, 470, 241, 71))
        self.searchConButton.setCheckable(False)
        self.searchConButton.setObjectName("searchConButton")
        self.tabWidget.addTab(self.DataFetcher, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Taipei RentFetcher"))
        self.label.setText(_translate("MainWindow", "Taipei RentFetcher"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">歡迎使用</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Taipei</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">RentFetcher</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">簡介</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">此為租屋網站</span><span style=\" font-weight:700;\">好房網HouseFun</span><span style=\" font-size:9pt;\">的前端程式，用於抓取台北地區的租屋行情資料</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /><span style=\" font-size:12pt; font-weight:700;\">使用說明<br /></span><span style=\" font-size:9pt; font-weight:700;\">1. </span><span style=\" font-size:9pt;\">點選 &quot;租屋行情查詢&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:700;\">2.</span><span style=\" font-size:9pt;\"> 點選 &quot;上一頁&quot; 與 &quot;下一頁&quot; 切換頁面</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:700;\">3. </span><span style=\" font-size:9pt;\">透過下拉式選單以及搜尋列選擇想要搜尋的條件</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:700;\">4.</span><span style=\" font-size:9pt;\"> 按下 &quot;搜尋&quot; 以根據條件進行搜尋</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Version 1.0.0-rc1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.welcomePage), _translate("MainWindow", "歡迎!"))
        self.resetButton.setText(_translate("MainWindow", "重置"))
        self.prevPageButton.setText(_translate("MainWindow", "上一頁"))
        self.nextPageButton.setText(_translate("MainWindow", "下一頁"))
        self.searchButton.setText(_translate("MainWindow", "搜尋"))
        self.searchConButton.setText(_translate("MainWindow", "搜尋條件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataFetcher), _translate("MainWindow", "租屋行情查詢"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "關於"))