
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

        self.buyButton1 = self.findChild(QPushButton, 'buyButton1')
        self.buyButton1.clicked.connect(lambda: self.showBuyWindow('CEAT ProRadia','INR 82,000'))

        self.buyButton2 = self.findChild(QPushButton, 'buyButton1_2')
        self.buyButton2.clicked.connect(lambda: self.showBuyWindow('Bridgestone Turanza','INR 92,000'))


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


