
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sportsWindow(QMainWindow):
    def __init__(self):
        super(Ui_sportsWindow, self).__init__()

        # Load the ui file
        uic.loadUi('sportstyres.ui',self)

        self.backButton = self.findChild(QPushButton, 'backButton')
        self.backButton.clicked.connect(self.showUI)

        self.buyButton1 = self.findChild(QPushButton, 'buyButton1')
        self.buyButton1.clicked.connect(lambda: self.showBuyWindow('Pirelli PZero Corsa','INR 21,40,000'))

        self.buyButton2 = self.findChild(QPushButton, 'buyButton1_2')
        self.buyButton2.clicked.connect(lambda: self.showBuyWindow('Michelin SuperCup 3RS','INR 24,60,000'))

        self.show()

    def showUI(self):
        from tyreWindow import Ui_windowTyre
        self.close()
        self.ui = Ui_windowTyre()
        self.ui.show()

    def showBuyWindow(self, product_name, cost):
        from buyConfirmWindow_Code import Ui_BuyConfirmWindow
        self.close()
        self.ui = Ui_BuyConfirmWindow(product_name,cost)
        self.ui.show()


