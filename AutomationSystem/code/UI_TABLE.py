from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TABLE(object):
    def setupUi(self, TABLE):
        TABLE.setObjectName("TABLE")
        TABLE.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(TABLE)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.graphicsView.setStyleSheet("background-color: rgb(241, 196, 15);")
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

        TABLE.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TABLE)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menubar.setObjectName("menubar")
        TABLE.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TABLE)
        self.statusbar.setObjectName("statusbar")
        TABLE.setStatusBar(self.statusbar)

        self.retranslateUi(TABLE)
        QtCore.QMetaObject.connectSlotsByName(TABLE)

    def retranslateUi(self, TABLE):
        _translate = QtCore.QCoreApplication.translate
        TABLE.setWindowTitle(_translate("TABLE", "MainWindow"))
        self.BACK.setText(_translate("TABLE", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TABLE = QtWidgets.QMainWindow()
    ui = Ui_TABLE()
    ui.setupUi(TABLE)
    TABLE.show()
    sys.exit(app.exec_())