from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit
from PyQt5 import QtWidgets
from PyQt5 import uic

import sys

class loginConfirm(QMainWindow):
    def __init__(self):
        super(loginConfirm, self).__init__()

        # Load the ui file
        uic.loadUi('login_confirm.ui',self)

        # Defining Widgets
        self.enterButton = self.findChild(QPushButton, 'enterButton')



        # When button pressed, open main window
        self.enterButton.clicked.connect(self.openMainWindow)

        self.show()

    def openMainWindow(self):
        from website_proj2code import UI
        self.close()
        self.ui = UI()
        self.ui.show()








