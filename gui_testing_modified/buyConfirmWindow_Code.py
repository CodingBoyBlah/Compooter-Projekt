
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton


from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BuyConfirmWindow(QMainWindow):
    def __init__(self):
        super(Ui_BuyConfirmWindow, self).__init__()

        # Load the ui file
        uic.loadUi('buyConfirmWindow.ui',self)



        self.show()






