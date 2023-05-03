from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys

class MainUI(QDialog):
    def __init__(self):
        super(MainUI, self).__init__()

        # Load the ui file
        loadUi('C:\\Users\\linet\\OneDrive\\Documents\\GitHub\\Compooter-Projekt\\gui_testing_modified\\cart.ui',self)

  
        # When button pressed, Open new window
        self.BUY.clicked.connect(self.PaymentWindow)
        #self.show()

    def PaymentWindow(self):
        dialog = Ui_PaymentWindowDialog()
        dialog.exec()

class Ui_PaymentWindowDialog(QDialog): 
    def __init__(self):
        
        super(Ui_PaymentWindowDialog,self).__init__()
        loadUi("C:\\Users\\linet\\OneDrive\\Documents\\GitHub\\Compooter-Projekt\\gui_testing_modified\\confirmation.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()
