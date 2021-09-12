from PyQt5 import *
from PyQt5.QtWidgets import *
from UI_SUCCESS import *
from UI_EDIT_SELECT import *
from UI_RECALLFILE import *
import Merge
import sys   

class Ui_OVEN_START(object):

    def openSuccessWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OVEN_SUCCESS()
        self.ui.setupUi(self.window)
        self.window.show()

    def openEDITSELECTWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EDIT_SELECT()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.BACK.clicked.connect(self.window.hide)

    def openRECALLFILEWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RECALLFILE()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.BACK.clicked.connect(self.window.hide)

    def setupUi(self, OVEN_START):

        OVEN_START.setObjectName("OVEN_START")
        OVEN_START.resize(1024, 768)
        OVEN_START.setMinimumSize(QtCore.QSize(1024, 768))
        OVEN_START.setMaximumSize(QtCore.QSize(1024, 768))

        self.centralwidget = QtWidgets.QWidget(OVEN_START)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_OVEN = QtWidgets.QLabel(self.centralwidget)
        self.Label_OVEN.setGeometry(QtCore.QRect(440, 0, 131, 81))

        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)

        self.Label_OVEN.setFont(font)
        self.Label_OVEN.setObjectName("Label_OVEN")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 70, 961, 71))
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
        self.EQUIP.clicked.connect(self.pushEquipButton)

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
        self.FIVERLIST.clicked.connect(self.pushFiverListButton)

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
        self.EDIT.clicked.connect(self.pushEditSelectButton)

        self.PREPARING = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.PREPARING.setMaximumSize(QtCore.QSize(260, 195))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.PREPARING.setFont(font)
        self.PREPARING.setStyleSheet("background-color: rgb(241, 196, 15);")
        self.PREPARING.setObjectName("PREPARING")
        self.horizontalLayout.addWidget(self.PREPARING)
        self.PREPARING.clicked.connect(self.pushPreparingButton)

        self.EXIT = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        self.EXIT.setFont(font)
        self.EXIT.setStyleSheet("background-color: rgb(161, 186, 255);")
        self.EXIT.setObjectName("EXIT")
        self.horizontalLayout.addWidget(self.EXIT)
        self.EXIT.clicked.connect(self.pushExitButton)

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")

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

        self.graphicsView.raise_()
        self.Label_OVEN.raise_()
        self.horizontalLayoutWidget.raise_()
        self.listTable.raise_()
        self.showTable.raise_()

        OVEN_START.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OVEN_START)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menubar.setObjectName("menubar")

        OVEN_START.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OVEN_START)
        self.statusbar.setObjectName("statusbar")
        OVEN_START.setStatusBar(self.statusbar)

        self.retranslateUi(OVEN_START)
        QtCore.QMetaObject.connectSlotsByName(OVEN_START)

    def retranslateUi(self, OVEN_START):
        _translate = QtCore.QCoreApplication.translate
        OVEN_START.setWindowTitle(_translate("OVEN_START", "MainWindow"))
        self.Label_OVEN.setText(_translate("OVEN_START", "OVEN"))
        self.EQUIP.setText(_translate("OVEN_START", "EQUIP"))
        self.FIVERLIST.setText(_translate("OVEN_START", "FIVERLIST"))
        self.EDIT.setText(_translate("OVEN_START", "EDIT"))
        self.PREPARING.setText(_translate("OVEN_START", "PREPARING"))
        self.EXIT.setText(_translate("OVEN_START", "EXIT"))

    Fiverlist_file=0
    Equip_file=0
    file_list = list()

    def pushFiverListButton(self):
        qfd = QFileDialog()
        fname = QFileDialog.getOpenFileName(qfd, 'Open file', '\\')

        if(fname[0]==""):
            QMessageBox.about(QWidget(), "Warning", "파일을 선택하지 않았습니다.")
            Ui_OVEN_START.Fiverlist_file = 0
        else:
            Ui_OVEN_START.Fiverlist_file = 1
            print(fname)
            Ui_OVEN_START.file_list.insert(0,fname)

    def pushEquipButton(self):
        qfd = QFileDialog()
        fname =  QFileDialog.getOpenFileName(qfd, 'Open file', '\\')

        if(fname[0]==""):
            QMessageBox.about(QWidget(), "Warning", "파일을 선택하지 않았습니다.")
            Ui_OVEN_START.Equip_file = 0
        else:
           Ui_OVEN_START.Equip_file = 1
           print(fname)
           Ui_OVEN_START.file_list.insert(1,fname)

    def pushPreparingButton(self):
        if(Ui_OVEN_START.Fiverlist_file==1 and Ui_OVEN_START.Equip_file==1):
            #Merge의 합치는 코드 실행되도록 만들기
            QMessageBox.about(QWidget(), "Success", "데이터베이스 작업파일을 얻을 수 있습니다.")
            QMessageBox.about(QWidget(), "Success", "OK버튼을 누른 뒤, 노란색 SUCCESS 버튼을 누르면 파일 다운로드가 시작됩니다.")
            self.openSuccessWindow()
        else:
            QMessageBox.about(QWidget(), "Warning", "작업할 파일의 갯수가 부족합니다.")

    def pushEditSelectButton(self):
        self.openEDITSELECTWindow()

    def pushRecallfileButton(self):
        self.openRECALLFILEWindow()

    def pushExitButton(self):
        quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OVEN_START = QtWidgets.QMainWindow()
    ui = Ui_OVEN_START()
    ui.setupUi(OVEN_START)
    OVEN_START.show()
    sys.exit(app.exec_())