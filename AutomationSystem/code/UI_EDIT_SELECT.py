from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI_EDIT_ADD import Ui_EDIT_ADD
from UI_EDIT_MODIFY import Ui_EDIT_MODIFY
from UI_EDIT_DELETE import Ui_EDIT_DELETE
import sys

class Ui_EDIT_SELECT(object):

    def openEditAddWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EDIT_ADD()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.BACK.clicked.connect(self.window.hide)

    def openEditModifyWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EDIT_MODIFY()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.BACK_2.clicked.connect(self.window.hide)

    def openEditDeleteWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EDIT_DELETE()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.BACK_2.clicked.connect(self.window.hide)

    def setupUi(self, EDIT_SELECT):
        EDIT_SELECT.setObjectName("EDIT_SELECT")
        EDIT_SELECT.resize(1024, 768)
        EDIT_SELECT.setMaximumSize(QtCore.QSize(1024, 768))
        self.centralwidget = QtWidgets.QWidget(EDIT_SELECT)
        self.centralwidget.setObjectName("centralwidget")

        self.SELECTFILE = QtWidgets.QPushButton(self.centralwidget)
        self.SELECTFILE.setGeometry(QtCore.QRect(0, 0, 1025, 221))
        self.SELECTFILE.setStyleSheet("background-color: rgb(22, 160, 133); font: 24pt \"HY견고딕\";")
        self.SELECTFILE.setObjectName("SELECTFILE")
        self.SELECTFILE.clicked.connect(self.pushSelectFileButton)

        self.MODIFY = QtWidgets.QPushButton(self.centralwidget)
        self.MODIFY.setGeometry(QtCore.QRect(0, 220, 343, 505))
        self.MODIFY.setStyleSheet("font: 24pt \"HY견고딕\";\n"
"background-color: rgb(26, 188, 156);")
        self.MODIFY.setObjectName("MODIFY")
        self.MODIFY.clicked.connect(self.pushModifyButton)

        self.ADD = QtWidgets.QPushButton(self.centralwidget)
        self.ADD.setGeometry(QtCore.QRect(340, 220, 343, 505))
        self.ADD.setStyleSheet("font: 24pt \"HY견고딕\";\n"
"background-color: rgb(46, 204, 113);")
        self.ADD.setObjectName("ADD")
        self.ADD.clicked.connect(self.pushAddButton)

        self.DELETE = QtWidgets.QPushButton(self.centralwidget)
        self.DELETE.setGeometry(QtCore.QRect(680, 220, 343, 505))
        self.DELETE.setStyleSheet("font: 24pt \"HY견고딕\";\n"
"background-color: rgb(241, 196, 15);")
        self.DELETE.setObjectName("DELETE")
        self.DELETE.clicked.connect(self.pushDeleteButton)

        self.BACK = QtWidgets.QPushButton(self.centralwidget)
        self.BACK.setGeometry(QtCore.QRect(0, 0, 111, 101))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(12)
        self.BACK.setFont(font)
        self.BACK.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.BACK.setObjectName("BACK")

        EDIT_SELECT.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EDIT_SELECT)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menubar.setObjectName("menubar")

        EDIT_SELECT.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EDIT_SELECT)
        self.statusbar.setObjectName("statusbar")
        EDIT_SELECT.setStatusBar(self.statusbar)

        self.retranslateUi(EDIT_SELECT)
        QtCore.QMetaObject.connectSlotsByName(EDIT_SELECT)

    def retranslateUi(self, EDIT_SELECT):
        _translate = QtCore.QCoreApplication.translate
        EDIT_SELECT.setWindowTitle(_translate("EDIT_SELECT", "MainWindow"))
        self.SELECTFILE.setText(_translate("EDIT_SELECT", "SELECT FILE"))
        self.MODIFY.setText(_translate("EDIT_SELECT", "MODIFY"))
        self.ADD.setText(_translate("EDIT_SELECT", "ADD"))
        self.DELETE.setText(_translate("EDIT_SELECT", "DELETE"))
        self.BACK.setText(_translate("EDIT_SELECT", "BACK"))

    Edit_File = 0

    def pushSelectFileButton(self):
        qfd = QFileDialog()
        fname = QFileDialog.getOpenFileName(qfd, 'Open file', '\\')

        if(fname[0]==""):
            QMessageBox.about(QWidget(), "Warning", "파일을 선택하지 않았습니다.")
            Ui_EDIT_SELECT.Edit_File = 0
        else:
            QMessageBox.about(QWidget(), "Success", "MODIFY, ADD, DELETE 중 원하는 작업을 선택하세요.")
            Ui_EDIT_SELECT.Edit_File = 1

    def pushAddButton(self):
        if(Ui_EDIT_SELECT.Edit_File == 1):
            QMessageBox.about(QWidget(), "Add", "추가하고 싶은 케이블명, 코어번호, 캐리어/회선명을 입력하세요.")
            uiedit = Ui_EDIT_ADD()
            uiedit.mainlabeltext = "ADD"
            self.openEditAddWindow()
        else:
            QMessageBox.about(QWidget(), "Warning", "파일을 선택하지 않았습니다.")

    def pushModifyButton(self):
        if(Ui_EDIT_SELECT.Edit_File == 1):
            QMessageBox.about(QWidget(), "Modify", "수정하고 싶은 케이블명, 코어번호, 캐리어/회선명을 입력하세요.")
            uiedit = Ui_EDIT_MODIFY()
            uiedit.mainlabeltext = "MODIFY"
            self.openEditModifyWindow()
        else:
            QMessageBox.about(QWidget(), "Warning", "파일을 선택하지 않았습니다.")

    def pushDeleteButton(self):
        if(Ui_EDIT_SELECT.Edit_File == 1):
            QMessageBox.about(QWidget(), "Delete", "삭제하고 싶은 케이블명, 코어번호, 캐리어/회선명을 입력하세요.")
            uiedit = Ui_EDIT_DELETE()
            uiedit.mainlabeltext = "DELETE"
            self.openEditDeleteWindow()
        else:
            QMessageBox.about(QWidget(), "Warning", "파일을 선택하지 않았습니다.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EDIT_SELECT = QtWidgets.QMainWindow()
    ui = Ui_EDIT_SELECT()
    ui.setupUi(EDIT_SELECT)
    EDIT_SELECT.show()
    sys.exit(app.exec_())
