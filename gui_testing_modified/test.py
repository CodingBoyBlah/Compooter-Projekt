from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QDialog, QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys

import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', password = 'slay', database = 'torquecart')
mycur = mycon.cursor()
myemail="xyz"

class MainUI(QDialog):
    def __init__(self):
        super(MainUI, self).__init__()

        # Load the ui file
        loadUi('C:\\Users\\linet\\OneDrive\\Documents\\GitHub\\Compooter-Projekt\\gui_testing_modified\\cart.ui',self)

  
        # When button pressed, Open new window
        self.BUY.clicked.connect(self.PaymentWindow)
        #self.show()
        
       # q1 = "SELECT * FROM cart WHERE email = 'xyz'"
        q1="SELECT * FROM cart WHERE email = %s"
        mycur.execute(q1,(myemail,))
        rescart = mycur.fetchall()
        i=0 
        for row in rescart:
            slnocart = str(rescart[i][0])
            q2="SELECT type,subtype,item,price from cart,product WHERE product.slno = %s"
            mycur.execute(q2,(slnocart,))
            respro = mycur.fetchall()
            print(rescart)
            self.ProductList.setItem(i,0,QTableWidgetItem(respro[0][0]))
            self.ProductList.setItem(i,1,QTableWidgetItem(respro[0][1]))
            self.ProductList.setItem(i,2,QTableWidgetItem(respro[0][2]))
            self.ProductList.setItem(i,3,QTableWidgetItem(rescart[i][1]))
            amount = respro[0][3] * rescart[i][1]
            self.ProductList.setItem(i,4,QTableWidgetItem(amount))
            i=i+1  
            
                      



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
