
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_windowEngine(QMainWindow):
    def __init__(self):
        super(Ui_windowEngine, self).__init__()

        # Load the ui file
        uic.loadUi('engineWindow.ui',self)

        self.show()

