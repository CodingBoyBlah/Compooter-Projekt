
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton


from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BuyConfirmWindow(QMainWindow):
    def __init__(self, product_name, cost):
        super(Ui_BuyConfirmWindow, self).__init__()
        # Load the ui file
        uic.loadUi('buyConfirmWindow.ui', self)

        self.backButton = self.findChild(QPushButton, 'backButton')
        self.backButton.clicked.connect(self.showUI)

        self.productName = self.findChild(QLabel, 'inputProdName')
        self.productName.setText(product_name)

        self.costProd = self.findChild(QLabel,'costLabel')
        self.costProd.setText(cost)

        self.show()

    def showUI(self):
        from website_proj2code import UI
        self.close()
        self.ui = UI()
        self.ui.show()





