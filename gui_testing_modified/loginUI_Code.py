from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit
from PyQt5 import QtWidgets
from PyQt5 import uic

import sys

class loginUI_(QMainWindow):
    def __init__(self):
        super(loginUI_, self).__init__()

        # Load the ui file
        uic.loadUi('loginUI.ui',self)

        # Defining Widgets
        self.loginLabel = self.findChild(QLabel, 'loginLabel')
        self.emailLabel = self.findChild(QLabel, 'emailLabel')
        self.passLabel = self.findChild(QLabel, 'passLabel')
        self.emailLineEdit = self.findChild(QLineEdit, 'emalLineEdit')
        self.passLineEdit = self.findChild(QLineEdit, 'passLineEdit')
        self.enterButton = self.findChild(QPushButton, 'enterButton')
        self.imagebgLabel = self.findChild(QLabel, 'imagebgLabel')

        # Masking the password
        self.passLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        # When button pressed, open main window
        self.enterButton.clicked.connect(self.openConfirmWindow)

        self.show()

    def openConfirmWindow(self):
        from login_confirmCode import loginConfirm
        self.close()
        self.ui = loginConfirm()
        self.ui.show()





app = QApplication(sys.argv)
UIWindow = loginUI_()
app.exec_()
