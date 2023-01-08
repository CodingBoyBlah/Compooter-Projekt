
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_radialWindow(QMainWindow):
    def __init__(self):
        super(Ui_radialWindow, self).__init__()

        # Load the ui file
        uic.loadUi('radialtyres.ui',self)

        self.backButton = self.findChild(QPushButton, 'backButton')
        self.backButton.clicked.connect(self.showUI)

        self.show()

    def showUI(self):
        from tyreWindow import Ui_windowTyre
        self.close()
        self.ui = Ui_windowTyre()
        self.ui.show()


