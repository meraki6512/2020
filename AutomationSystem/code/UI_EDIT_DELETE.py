
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import *
import editinput as EI

class Ui_EDIT_DELETE(object):
    edittextlist = list()

    def setupUi(self, EDIT_DELETE):
        EDIT_DELETE.setObjectName("EDIT_DELETE")
        EDIT_DELETE.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(EDIT_DELETE)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.graphicsView.setStyleSheet("background-color:rgb(22, 160, 133);\n"
"")
        self.graphicsView.setObjectName("graphicsView")

        self.CABLENAME = QtWidgets.QLabel(self.centralwidget)
        self.CABLENAME.setGeometry(QtCore.QRect(210, 160, 111, 51))
        self.CABLENAME.setStyleSheet("font: 20pt \"HY견고딕\";")
        self.CABLENAME.setObjectName("CABLENAME")

        self.CABLEINPUT = QtWidgets.QLineEdit(self.centralwidget)
        self.CABLEINPUT.setGeometry(QtCore.QRect(460, 170, 361, 41))
        self.CABLEINPUT.setObjectName("CABLEINPUT")

        self.CORENUM = QtWidgets.QLabel(self.centralwidget)
        self.CORENUM.setGeometry(QtCore.QRect(210, 320, 111, 51))
        self.CORENUM.setStyleSheet("font: 20pt \"HY견고딕\";")
        self.CORENUM.setObjectName("CORENUM")

        self.COREINPUT = QtWidgets.QLineEdit(self.centralwidget)
        self.COREINPUT.setGeometry(QtCore.QRect(460, 330, 361, 41))
        self.COREINPUT.setObjectName("COREINPUT")

        self.LINENAME = QtWidgets.QLabel(self.centralwidget)
        self.LINENAME.setGeometry(QtCore.QRect(140, 480, 181, 51))
        self.LINENAME.setStyleSheet("font: 20pt \"HY견고딕\";")
        self.LINENAME.setObjectName("LINENAME")

        self.LINEINPUT = QtWidgets.QLineEdit(self.centralwidget)
        self.LINEINPUT.setGeometry(QtCore.QRect(460, 490, 361, 41))
        self.LINEINPUT.setObjectName("LINEINPUT")

        self.LABEL_DELETE = QtWidgets.QLabel(self.centralwidget)
        self.LABEL_DELETE.setGeometry(QtCore.QRect(460, 40, 121, 51))
        self.LABEL_DELETE.setStyleSheet("font: 20pt \"HY견고딕\";")
        self.LABEL_DELETE.setObjectName("LABEL_DELETE")

        self.DONECABLE = QtWidgets.QPushButton(self.centralwidget)
        self.DONECABLE.setGeometry(QtCore.QRect(880, 170, 101, 41))
        self.DONECABLE.setStyleSheet("font: 14pt \"HY견고딕\";\n"
"background-color: rgb(241, 196, 15);")
        self.DONECABLE.setObjectName("DONECABLE")
        self.DONECABLE.clicked.connect(self.pushDoneCableButton)

        self.DONECORE = QtWidgets.QPushButton(self.centralwidget)
        self.DONECORE.setGeometry(QtCore.QRect(880, 330, 101, 41))
        self.DONECORE.setStyleSheet("font: 14pt \"HY견고딕\";\n"
"background-color: rgb(241, 196, 15);")
        self.DONECORE.setObjectName("DONECORE")
        self.DONECORE.clicked.connect(self.pushDoneCoreButton)

        self.DONELINE = QtWidgets.QPushButton(self.centralwidget)
        self.DONELINE.setGeometry(QtCore.QRect(880, 490, 101, 41))
        self.DONELINE.setStyleSheet("font: 14pt \"HY견고딕\";\n"
"background-color: rgb(241, 196, 15);")
        self.DONELINE.setObjectName("DONELINE")
        self.DONELINE.clicked.connect(self.pushDoneLineButton)

        self.DONETOTAL = QtWidgets.QPushButton(self.centralwidget)
        self.DONETOTAL.setGeometry(QtCore.QRect(450, 620, 101, 51))
        self.DONETOTAL.setStyleSheet("font: 14pt \"HY견고딕\";\n"
"background-color: rgb(241, 196, 15);")
        self.DONETOTAL.setObjectName("DONETOTAL")
        self.DONETOTAL.clicked.connect(self.pushDoneTotalButton)

        self.BACK_2 = QtWidgets.QPushButton(self.centralwidget)
        self.BACK_2.setGeometry(QtCore.QRect(0, 0, 111, 101))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(12)
        self.BACK_2.setFont(font)
        self.BACK_2.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.BACK_2.setObjectName("BACK_2")

        EDIT_DELETE.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EDIT_DELETE)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menubar.setObjectName("menubar")
        EDIT_DELETE.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EDIT_DELETE)
        self.statusbar.setObjectName("statusbar")
        EDIT_DELETE.setStatusBar(self.statusbar)

        self.retranslateUi(EDIT_DELETE)
        QtCore.QMetaObject.connectSlotsByName(EDIT_DELETE)

    def retranslateUi(self, EDIT_DELETE):
        _translate = QtCore.QCoreApplication.translate
        EDIT_DELETE.setWindowTitle(_translate("EDIT_DELETE", "MainWindow"))
        self.CABLENAME.setText(_translate("EDIT_DELETE", "케이블명"))
        self.CORENUM.setText(_translate("EDIT_DELETE", "코어번호"))
        self.LINENAME.setText(_translate("EDIT_DELETE", "캐리어/회선명"))
        self.LABEL_DELETE.setText(_translate("EDIT_DELETE", "DELETE"))
        self.DONECABLE.setText(_translate("EDIT_DELETE", "DONE"))
        self.DONECORE.setText(_translate("EDIT_DELETE", "DONE"))
        self.DONELINE.setText(_translate("EDIT_DELETE", "DONE"))
        self.DONETOTAL.setText(_translate("EDIT_DELETE", "DONE"))
        self.BACK_2.setText(_translate("EDIT_DELETE", "BACK"))

    cableinputsuccess = 0
    coreinputsuccess = 0
    lineinputsuccess = 0

    def pushDoneCableButton(self):
        cableinputtext = self.CABLEINPUT.text()
        Ui_EDIT_DELETE.cableinputsuccess = EI.pushDoneButton(cableinputtext)
        if(Ui_EDIT_DELETE.cableinputsuccess == 1):
            Ui_EDIT_DELETE.edittextlist.insert(0, cableinputtext)
        else:
            Ui_EDIT_DELETE.cableinputsuccess = 0
        
    def pushDoneCoreButton(self):
        coreinputtext = self.COREINPUT.text()
        Ui_EDIT_DELETE.coreinputsuccess = EI.pushDoneButton(coreinputtext)
        if(Ui_EDIT_DELETE.coreinputsuccess == 1):
            Ui_EDIT_DELETE.edittextlist.insert(1, coreinputtext)
        else:
            Ui_EDIT_DELETE.coreinputsuccess = 0

    def pushDoneLineButton(self):
        lineinputtext = self.LINEINPUT.text()
        Ui_EDIT_DELETE.lineinputsuccess = EI.pushDoneButton(lineinputtext)
        if(Ui_EDIT_DELETE.lineinputsuccess==1):
            Ui_EDIT_DELETE.edittextlist.insert(2, lineinputtext)
        else:
            Ui_EDIT_DELETE.lineinputsuccess = 0

    def pushDoneTotalButton(self):
        EI.finalDoneButton(Ui_EDIT_DELETE.cableinputsuccess, Ui_EDIT_DELETE.coreinputsuccess, 
                           Ui_EDIT_DELETE.lineinputsuccess, Ui_EDIT_DELETE.edittextlist, 3)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EDIT_DELETE = QtWidgets.QMainWindow()
    ui = Ui_EDIT_DELETE()
    ui.setupUi(EDIT_DELETE)
    EDIT_DELETE.show()
    sys.exit(app.exec_())