#!/usr/bin/env python3
import os
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
#import Attendance
## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen
## ==> LOGIN
from ui_login import Ui_Login
## ==> Menu
from ui_menu import Ui_menu
## ==> ADD
from ui_add import Ui_add
## ==>UPDATE
from ui_update import Ui_update
## ==>DELETE
from ui_delete import Ui_DELETE_2
## ==> GLOBALS
counter = 0

class add(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_add()
        self.ui.setupUi(self)
        self.ui.BACK.clicked.connect(self.menu)
    def menu(self):
         #connect menu window
        self.main = menu()
        self.main.show()
        # CLOSE add
        self.close()



class update(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_update()
        self.ui.setupUi(self)
        self.ui.BACK.clicked.connect(self.menu)
    def menu(self):
         #connect menu window
        self.main = menu()
        self.main.show()
        # CLOSE update
        self.close()    
        
class DELETE_2(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_DELETE_2()
        self.ui.setupUi(self)
        self.ui.BACK.clicked.connect(self.menu)
    def menu(self):
         #connect menu window
        self.main = menu()
        self.main.show()
        # CLOSE delete
        self.close()   

class menu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_menu()
        self.ui.setupUi(self)
        self.ui.FACE.clicked.connect(self.facerecog)
        self.ui.ADD.clicked.connect(self.add)
        self.ui.UPDATE.clicked.connect(self.update)
        self.ui.DELETE.clicked.connect(self.delete)
    
    def add(self):
        #connect add window
        self.main = add()
        self.main.show()
        # CLOSE menu
        self.close()
    def update(self):
        #connect update window
        self.main = update()
        self.main.show()
        # CLOSE menu
        self.close() 
    def facerecog(self):
        msg = QMessageBox()
        msg.setText("INSTRUCTION: PRESS 'Q' to close the camera")
        msg.exec_()  
        os.system("./Attendance.py ")

        #connect attendance.py     #     
    def delete(self):
        #connect delete
        self.main = DELETE_2()
        self.main.show()
        # CLOSE menu
        self.close()     
        

# YOUR APPLICATION
class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.pushButton.clicked.connect(self.on_click)


    def on_click(self):
        msg = QMessageBox()
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        if username == "admin" and password == "admin":
            # SHOW MAIN WINDOW
            msg.setText("Success")
            msg.exec_()
            self.main = menu()
            self.main.show()

            # CLOSE Login
            self.close()
        else:
            msg.setText("Incorrect Password")
            msg.exec_()    

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = Login()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
