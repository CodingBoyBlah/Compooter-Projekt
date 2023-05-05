from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QDialog, QTableWidgetItem, QMessageBox
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys

import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', password = 'slay', database = 'torquecart')
mycur = mycon.cursor()
myemail="xyz"
global totalAmount
arg=10 




class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        # Load the ui file
        loadUi('C:\\Users\\linet\\OneDrive\\Documents\\GitHub\\Compooter-Projekt\\gui_testing_modified\\main_window.ui',self)

        self.viewcart.clicked.connect(self.CartWindow)
        self.tyres.clicked.connect(self.TyresWindow)



    def TyresWindow(self):
         dialog = Ui_TyresWindowDialog()
         dialog.exec()

    def CartWindow(self):
        dialog = Ui_CartWindowDialog()
        dialog.exec()

class Ui_TyresWindowDialog(QDialog):
    def __init__(self):
        super(Ui_TyresWindowDialog, self).__init__()

        # Load the ui file
        loadUi('C:\\Users\\linet\\OneDrive\\Documents\\GitHub\\Compooter-Projekt\\gui_testing_modified\\tyres.ui',self)




        self.track.clicked.connect(self.TrackTyresWindow)

    def TrackTyresWindow(self):
        dialog = Ui_TrackTyresWindowDialog()
        dialog.exec()

#global AddToCart
def AddToCart(slno):
    
    #slno=10
    q4="SELECT price from products WHERE slno  = %s"
    #print(slno)
    mycur.execute(q4,(slno,))
    result = mycur.fetchall()

    q3 = "insert into cart (slno,qty,amt,email) values ('{0}','{1}','{2}','{3}')".format(slno,1, result[0][0],myemail)
    
    mycur.execute(q3)
    mycon.commit()


class Ui_TrackTyresWindowDialog(QDialog):
    def __init__(self):
        super(Ui_TrackTyresWindowDialog, self).__init__()

        # Load the ui file
        loadUi('C:\\Users\\linet\\OneDrive\\Documents\\GitHub\\Compooter-Projekt\\gui_testing_modified\\tracktyrestest.ui',self)

        self.add_10.clicked.connect(lambda:AddToCart(10))
        self.add_11.clicked.connect(lambda:AddToCart(11))
        self.add_12.clicked.connect(lambda:AddToCart(12))   


class Ui_CartWindowDialog(QDialog):
    def __init__(self):
        super(Ui_CartWindowDialog, self).__init__()

        # Load the ui file
        loadUi('C:\\Users\\linet\\OneDrive\\Documents\\GitHub\\Compooter-Projekt\\gui_testing_modified\\cart.ui',self)

  
        # When button pressed, Open new window
        #self.ADD.clicked.connect(self.CartWindow)
        self.BUY.clicked.connect(self.PaymentWindow)
        
        self.ProductList.itemChanged.connect(self.updateAmt)


       # q1 = "SELECT * FROM cart WHERE email = 'xyz'"
        q1="SELECT * FROM cart WHERE email = %s"
        mycur.execute(q1,(myemail,))
        rescart = mycur.fetchall()
        i=0 
        totalAmount = 0
        for row in rescart:
            slnocart = str(rescart[i][0])
            q2="SELECT type,subtype,item,price from cart,products WHERE products.slno = %s"
            mycur.execute(q2,(slnocart,))
            respro = mycur.fetchall()
            
            self.ProductList.setItem(i,0,QTableWidgetItem(respro[0][0]))
            self.ProductList.setItem(i,1,QTableWidgetItem(respro[0][1]))
            self.ProductList.setItem(i,2,QTableWidgetItem(respro[0][2]))
            self.ProductList.setItem(i,3,QTableWidgetItem(str(rescart[i][1])))
            amount = respro[0][3] * rescart[i][1]    
            totalAmount = totalAmount + amount        
            self.ProductList.setItem(i,4,QTableWidgetItem(str(amount)))
            i=i+1

        self.amount.setText(str(totalAmount))

    def PaymentWindow(self):
        self.close()
        dialog = Ui_PaymentWindowDialog()
        dialog.exec()

    def updateAmt(self, item):
      if  item.column() == 3:
          curRow = self.ProductList.currentRow();
          prevCol = int (item.column()) - 1;
          nextCol = int (item.column()) - 1;
          updatedQty = self.ProductList.item(item.row(), item.column()).text()

          ItemType = self.ProductList.item(item.row(), prevCol).text()
          #amount = self.ProductList.item(item.row(), nextCol).text()

          q2="SELECT remqty, price, slno from products WHERE item  = %s"
          mycur.execute(q2,(ItemType,))
          result = mycur.fetchall()

          #check sufficient qty
          Qty = int(result[0][0])

          if ("" != updatedQty and int(updatedQty) > Qty ):
            self.ProductList.setItem(item.row(), item.column(),QTableWidgetItem("1"))
            msgBox = QMessageBox()
            msgBox.setText("Quantity selected not available")
            msgBox.exec()
          else:
            if ("" != updatedQty):
                amount = int(result[0][1]) * int(updatedQty) 
                self.ProductList.setItem(item.row(),4,QTableWidgetItem(str(amount)))
                self.UpdateAmount()

    def UpdateAmount(self):
        totalAmount = 0
        for row in range(self.ProductList.rowCount()):
            for col in range(self.ProductList.columnCount()):
                if (col == 4):
                    item = self.ProductList.item(row, col)
                    print(row,col)
                    if not item or not item.text():
                        print(row,col)
                        rowAmount = item.text()                        
                        print(rowAmount)
                        totalAmount = int(rowAmount) + totalAmount

        self.amount.setText(str(totalAmount))



          
          #self.ProductList.setItem(i,4,QTableWidgetItem(str(amount)))

class Ui_PaymentWindowDialog(QDialog): 
    def __init__(self):
        
        super(Ui_PaymentWindowDialog,self).__init__()
        loadUi("C:\\Users\\linet\\OneDrive\\Documents\\GitHub\\Compooter-Projekt\\gui_testing_modified\\payment.ui",self)

        self.Confirm.clicked.connect(self.ConfirmationWindow)
        

    def ConfirmationWindow(self):
        self.close()
        dialog = Ui_ConfirmationWindowDialog()
        dialog.exec()


class Ui_ConfirmationWindowDialog(QDialog): 
    def __init__(self):
        
        super(Ui_ConfirmationWindowDialog,self).__init__()
        loadUi("C:\\Users\\linet\\OneDrive\\Documents\\GitHub\\Compooter-Projekt\\gui_testing_modified\\confirmation.ui", self)

        self.home.clicked.connect(self.MainWindow)

    def MainWindow(self):
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()