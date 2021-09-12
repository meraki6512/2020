#RECALLFILE 윈도우에서 파일작업 히스토리 출력하는 코드 작성해야함
#히스토리를 목록형식으로 만든 뒤, 목록에서 클릭하면 새로운 창이 뜨도록 해야함 -> 새로운 GUI 디자인파일 필요, 혹은 UI_TABLE 을 사용해도 좋음

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QCoreApplication, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction
import sys

class Ui_RECALLFILE(object):
    
    def setupUi(self, RECALLFILE):
        RECALLFILE.setObjectName("RECALLFILE")
        RECALLFILE.resize(1024, 768)
        RECALLFILE.setMaximumSize(QtCore.QSize(1024, 768))

        self.centralwidget = QtWidgets.QWidget(RECALLFILE)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.graphicsView.setMaximumSize(QtCore.QSize(1024, 768))
        self.graphicsView.setStyleSheet("background-color: rgb(41, 128, 185);")
        self.graphicsView.setObjectName("graphicsView")

        self.BACK = QtWidgets.QPushButton(self.centralwidget)
        self.BACK.setGeometry(QtCore.QRect(0, 0, 111, 101))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(12)
        self.BACK.setFont(font)
        self.BACK.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.BACK.setObjectName("BACK")

        RECALLFILE.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RECALLFILE)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menubar.setObjectName("menubar")
        RECALLFILE.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RECALLFILE)
        self.statusbar.setObjectName("statusbar")
        RECALLFILE.setStatusBar(self.statusbar)

        self.retranslateUi(RECALLFILE)
        QtCore.QMetaObject.connectSlotsByName(RECALLFILE)

    def retranslateUi(self, RECALLFILE):
        _translate = QtCore.QCoreApplication.translate
        RECALLFILE.setWindowTitle(_translate("RECALLFILE", "MainWindow"))
        self.BACK.setText(_translate("RECALLFILE", "BACK"))


if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    RECALLFILE = QtWidgets.QMainWindow()
    ui = Ui_RECALLFILE()
    ui.setupUi(RECALLFILE)
    RECALLFILE.show()
    sys.exit(app.exec_())