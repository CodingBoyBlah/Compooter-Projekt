from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QDialog, QTableWidgetItem, QMessageBox
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
        self.ProductList.itemChanged.connect(self.updateAmt)


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
            
            self.ProductList.setItem(i,0,QTableWidgetItem(respro[0][0]))
            self.ProductList.setItem(i,1,QTableWidgetItem(respro[0][1]))
            self.ProductList.setItem(i,2,QTableWidgetItem(respro[0][2]))
            self.ProductList.setItem(i,3,QTableWidgetItem(str(rescart[i][1])))
            amount = respro[0][3] * rescart[i][1]            
            self.ProductList.setItem(i,4,QTableWidgetItem(str(amount)))
            i=i+1


    def PaymentWindow(self):
        dialog = Ui_PaymentWindowDialog()
        dialog.exec()

    def updateAmt(self, item):
      if  item.column() == 3:
          curRow = self.ProductList.currentRow();
          prevCol = int (item.column()) - 1;
          nextCol = int (item.column()) - 1;
          updatedQty = self.ProductList.item(item.row(), item.column()).text()
          ItemType = self.ProductList.item(item.row(), prevCol).text()
          amount = self.ProductList.item(item.row(), nextCol).text()

          q2="SELECT remqty, price from product WHERE item  = %s"
          mycur.execute(q2,(ItemType,))
          result = mycur.fetchall()

          #check sufficient qty
          Qty = int(result[0][0])
          if (int(updatedQty) > Qty ):
            msgBox = QMessageBox()
            msgBox.setText("Quantity selected not available")
            msgBox.exec()
            temp=1
            self.ProductList.setItem(0,3,QTableWidgetItem(temp))
          else:
            amount = int(result[0][1]) * int(updatedQty) 
            self.ProductList.setItem(item.row(),4,QTableWidgetItem(str(amount))) 

          
          #self.ProductList.setItem(i,4,QTableWidgetItem(str(amount)))

class Ui_PaymentWindowDialog(QDialog): 
    def __init__(self):
        
        super(Ui_PaymentWindowDialog,self).__init__()
        loadUi("C:\\Users\\linet\\OneDrive\\Documents\\GitHub\\Compooter-Projekt\\gui_testing_modified\\confirmation.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()