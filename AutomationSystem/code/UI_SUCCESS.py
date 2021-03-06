from PyQt5 import QtCore, QtGui, QtWidgets
import Merge

class Ui_OVEN_SUCCESS(object):
    def setupUi(self, OVEN_SUCCESS):
        OVEN_SUCCESS.setObjectName("OVEN_SUCCESS")
        OVEN_SUCCESS.resize(1024, 768)
        OVEN_SUCCESS.setMaximumSize(QtCore.QSize(1024, 768))
        self.centralwidget = QtWidgets.QWidget(OVEN_SUCCESS)
        self.centralwidget.setObjectName("centralwidget")
        self.listTable = QtWidgets.QTableWidget(self.centralwidget)
        self.listTable.setGeometry(QtCore.QRect(30, 230, 171, 411))
        self.listTable.setRowCount(15)
        self.listTable.setColumnCount(1)
        self.listTable.setObjectName("listTable")
        self.showTable = QtWidgets.QTableWidget(self.centralwidget)
        self.showTable.setGeometry(QtCore.QRect(220, 230, 781, 411))
        self.showTable.setIconSize(QtCore.QSize(0, 0))
        self.showTable.setRowCount(1000)
        self.showTable.setColumnCount(16)
        self.showTable.setObjectName("showTable")
        self.Label_OVEN = QtWidgets.QLabel(self.centralwidget)
        self.Label_OVEN.setGeometry(QtCore.QRect(450, 0, 131, 81))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.Label_OVEN.setFont(font)
        self.Label_OVEN.setObjectName("Label_OVEN")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 70, 961, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(60)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EQUIP = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.EQUIP.setMaximumSize(QtCore.QSize(260, 195))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.EQUIP.setFont(font)
        self.EQUIP.setStyleSheet("background-color: rgb(46, 204, 113);")
        self.EQUIP.setObjectName("EQUIP")
        self.horizontalLayout.addWidget(self.EQUIP)
        self.FIVERLIST = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.FIVERLIST.setMaximumSize(QtCore.QSize(260, 195))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.FIVERLIST.setFont(font)
        self.FIVERLIST.setStyleSheet("background-color: rgb(26, 188, 156);\n"
"border-color: rgb(26, 188, 156);")
        self.FIVERLIST.setObjectName("FIVERLIST")
        self.horizontalLayout.addWidget(self.FIVERLIST)
        self.EDIT = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.EDIT.setMaximumSize(QtCore.QSize(260, 195))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.EDIT.setFont(font)
        self.EDIT.setStyleSheet("background-color: rgb(22, 160, 133);\n"
"selection-color: rgb(22, 160, 133);")
        self.EDIT.setObjectName("EDIT")
        self.horizontalLayout.addWidget(self.EDIT)
        self.SUCCESS = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SUCCESS.setMaximumSize(QtCore.QSize(260, 195))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.SUCCESS.setFont(font)
        self.SUCCESS.setStyleSheet("background-color: rgb(241, 196, 15);")
        self.SUCCESS.setObjectName("SUCCESS")
        self.horizontalLayout.addWidget(self.SUCCESS)
        self.EXIT = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        self.EXIT.setFont(font)
        self.EXIT.setStyleSheet("background-color: rgb(161, 186, 255);")
        self.EXIT.setObjectName("EXIT")
        self.horizontalLayout.addWidget(self.EXIT)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.listTable.raise_()
        self.showTable.raise_()
        self.Label_OVEN.raise_()
        self.horizontalLayoutWidget.raise_()
        OVEN_SUCCESS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OVEN_SUCCESS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menubar.setObjectName("menubar")
        OVEN_SUCCESS.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OVEN_SUCCESS)
        self.statusbar.setObjectName("statusbar")
        OVEN_SUCCESS.setStatusBar(self.statusbar)

        self.retranslateUi(OVEN_SUCCESS)
        QtCore.QMetaObject.connectSlotsByName(OVEN_SUCCESS)

    def retranslateUi(self, OVEN_SUCCESS):
        _translate = QtCore.QCoreApplication.translate
        OVEN_SUCCESS.setWindowTitle(_translate("OVEN_SUCCESS", "MainWindow"))
        self.Label_OVEN.setText(_translate("OVEN_SUCCESS", "OVEN"))
        self.EQUIP.setText(_translate("OVEN_SUCCESS", "EQUIP"))
        self.FIVERLIST.setText(_translate("OVEN_SUCCESS", "FIVERLIST"))
        self.EDIT.setText(_translate("OVEN_SUCCESS", "EDIT"))
        self.SUCCESS.setText(_translate("OVEN_SUCCESS", "success"))
        self.EXIT.setText(_translate("OVEN_SUCCESS", "EXIT"))
