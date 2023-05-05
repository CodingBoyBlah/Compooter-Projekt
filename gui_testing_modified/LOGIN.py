# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
from pathlib import Path
from signup_code import Ui_SignupWindow
from main_window import Ui_MainWindow

class Ui_LoginWindow(QDialog):
    def __init__(self):
        super(Ui_LoginWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'LOGIN.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.email = self.findChild(QLineEdit, 'Email')
        self.password = self.findChild(QLineEdit, 'Password')
        self.signin = self.findChild(QPushButton, 'SignIN')
        self.register = self.findChild(QPushButton, 'Register')

        self.signin.clicked.connect(self.signin_handler)
        self.register.clicked.connect(self.register_handler)



    def signin_handler(self):
        email = self.email.text()
        password = self.password.text()
        print(email, password)
        #TODO: fetch password for username
        #      compare password with queried password
        #      grant access on match
        #      open ui window for next screen
        self.main_window = Ui_MainWindow()
        self.main_window.show()


    def register_handler(self):
        print("wanna register???")
        self.signup_window = Ui_SignupWindow()
        self.signup_window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_LoginWindow()
    ui.show()
    sys.exit(app.exec_())