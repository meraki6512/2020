import UI_EDIT_SELECT
import UI_EDIT_ADD
import UI_EDIT_MODIFY
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import *

def pushDoneButton(text):
    box = QMessageBox()

    if(text==""):    
        box.setIcon(QMessageBox.Warning)
        box.setWindowTitle("Warning")
        box.setText("입력된 내용이 없습니다.")
        x=box.exec_()
        return -1
    else:
        box.setIcon(QMessageBox.Information)
        box.setWindowTitle("Success")
        box.setText("입력성공      ")
        x=box.exec_()
        return 1

def finalDoneButton(cablesuccess, coresuccess, linesuccess, edittextlist, type):
    if(cablesuccess==1 and coresuccess==1 and linesuccess ==1):
        QMessageBox.about(QWidget(), "Success", "성공적으로 저장되었습니다")
        edittextlist.append(type) #타입이 1이면 수정, 2면 추가, 3이면 삭제
        print(edittextlist)
        return edittextlist
    else:
        if(cablesuccess == 0):
            QMessageBox.about(QWidget(), "Warning", "케이블명에 입력된 내용이 없습니다.")
        elif(coresuccess == 0):
            QMessageBox.about(QWidget(), "Warning", "코어번호에 입력된 내용이 없습니다.")
        else:
            QMessageBox.about(QWidget(), "Warning", "캐리어/회선명에 입력된 내용이 없습니다.")