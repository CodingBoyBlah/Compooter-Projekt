
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton


from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_windowTyre(QMainWindow):
    def __init__(self):
        super(Ui_windowTyre, self).__init__()

        # Load the ui file
        uic.loadUi('tyreWindow.ui',self)

        self.backButton = self.findChild(QPushButton, 'backButton')
        self.backButton.clicked.connect(self.showUI)

        self.show()

    def showUI(self):
        from website_proj2code import UI
        self.close()
        self.ui = UI()
        self.ui.show()



