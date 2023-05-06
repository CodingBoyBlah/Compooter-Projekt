'''
    main_window.py

    implementation file for main window handling

'''

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog, QTableWidgetItem, QMessageBox , QHeaderView
from PyQt5 import QtWidgets
from PyQt5 import uic
from pathlib import Path
from suspension import Ui_SuspensionWindow
from Steeringg import Ui_SteeringWindow
from tyre import Ui_tyreWindow
from oils import Ui_OilWindow


import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', password = 'slay', database = 'torquecart')
mycur = mycon.cursor()
myemail="xyz"
totalAmount = 0

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'main_window.ui')
        # Load the ui file
        uic.loadUi(filepath,self)
        global myemail

        self.tyres = self.findChild(QPushButton, 'tyres')
        self.suspension = self.findChild(QPushButton, 'suspension')
        self.steering = self.findChild(QPushButton, 'steering')
        self.oils = self.findChild(QPushButton, 'oils')
        self.exhaust = self.findChild(QPushButton, 'exhaust')
        self.engine = self.findChild(QPushButton, 'engine')

        self.tyres.clicked.connect(self.tyres_handler)
        self.suspension.clicked.connect(self.suspension_handler)
        self.steering.clicked.connect(self.steering_handler)
        self.oils.clicked.connect(self.oils_handler)
        self.exhaust.clicked.connect(self.exhaust_handler)
        self.engine.clicked.connect(self.engine_handler)


        self.viewcart.clicked.connect(self.CartWindow)

    def closeEvent (self, event):
        print("main window destroyed")


    def tyres_handler(self):
        print("tyres_handler")
        self.suspension_window = Ui_tyreWindow(myemail)
        self.suspension_window.show()
        pass

    def suspension_handler(self):
        print("suspension_handler")
        self.suspension_window = Ui_SuspensionWindow()
        self.suspension_window.show()
        pass

    def steering_handler(self):
        print("steering_handler")
        self.suspension_window = Ui_SteeringWindow()
        self.suspension_window.show()
        pass

    def oils_handler(self):
        print("oils_handler")
        self.suspension_window = Ui_OilWindow()
        self.suspension_window.show()
        pass

    def exhaust_handler(self):
        print("exhaust_handler")
        pass

    def engine_handler(self):
        print("engine_handler")
        pass

    def CartWindow(self):
        dialog = Ui_CartWindowDialog()
        dialog.exec()


class Ui_CartWindowDialog(QDialog):
    def __init__(self):
        super(Ui_CartWindowDialog, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'cart.ui')
        # Load the ui file
        uic.loadUi(filepath,self)


        # When button pressed, Open new window
        #self.ADD.clicked.connect(self.CartWindow)
        self.BUY.clicked.connect(self.PaymentWindow)
        
        self.ProductList.itemChanged.connect(self.updateAmt)

        global totalAmount
        global myemail
       
        q1="SELECT * FROM cart WHERE email = %s"
        mycur.execute(q1,(myemail,))
        print(myemail)
        rescart = mycur.fetchall()
        i=0 
        totalAmount = 0
        print("sql executed")

    
        row_count = len(rescart)
        print(row_count)
        
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
            print(i)

        self.amount.setText(str(totalAmount))
        
        header = self.ProductList.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)

    def PaymentWindow(self):
        self.close()
        dialog = Ui_PaymentWindowDialog()
        dialog.exec()

    def updateAmt(self, item):

      global totalAmount
      if  item.column() == 3:
          
          prevCol = 2;
          nextCol = 4;
          updatedQty = self.ProductList.item(item.row(), item.column()).text()
          ItemType = self.ProductList.item(item.row(), prevCol).text()
          
          q2="SELECT Qty, price, slno from products WHERE item  = %s"
          mycur.execute(q2,(ItemType,))
          result = mycur.fetchall()

          #check sufficient qty
          QtyInStock = int(result[0][0])
          slno = int(result[0][2])

          if ("" != updatedQty and int(updatedQty) > QtyInStock ):
            self.ProductList.setItem(item.row(), item.column(),QTableWidgetItem("1"))
            msgBox = QMessageBox()
            msgBox.setText("Quantity selected not available")
            msgBox.exec()
          else:
            if ("" != updatedQty):

                #fetch the original amount and save it in Origamount
                origAmtItem = self.ProductList.item(item.row(), nextCol)
                if  origAmtItem : 
                    Origamount = origAmtItem.text()
                else:
                    Origamount =""
                
                #calculate the new amount
                newAmount = int(result[0][1]) * int(updatedQty) 
                self.ProductList.setItem(item.row(),4,QTableWidgetItem(str(newAmount)))
                
                #recalcualte the Total Amount by sutracting the OrigAmount and adding newAmount
                #update the Total in the label
                if ("" != Origamount):
                    totalAmount = totalAmount - int(Origamount) + newAmount
                    self.amount.setText(str(totalAmount))

class Ui_PaymentWindowDialog(QDialog): 
    def __init__(self):
        
        super(Ui_PaymentWindowDialog,self).__init__()

        global totalAmount

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'payment.ui')
        # Load the ui file
        uic.loadUi(filepath,self)
        print(filepath)

        #self.amount.setText(str(totalAmount))
        self.Confirm.clicked.connect(self.ConfirmationWindow)
        self.amount.setText(str(totalAmount))
        

    def ConfirmationWindow(self):
        
        if self.address.text() != "" and self.phone.text() != "" :
            self.close()
            dialog = Ui_ConfirmationWindowDialog()
            dialog.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setText("Please enter address and phone number. Both are mandatory")
            msgBox.exec()



class Ui_ConfirmationWindowDialog(QDialog): 
    def __init__(self):
        
        super(Ui_ConfirmationWindowDialog,self).__init__()
        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'confirmation.ui')
        # Load the ui file
        uic.loadUi(filepath,self)
        

        self.home.clicked.connect(self.MainWindow)
        global myemail

        #fetch all products
        q1 = "SELECT slno, qty FROM  products "
        mycur.execute(q1)
        resProd = mycur.fetchall()
        i=0
        for row in resProd:
                ProdSlno = resProd[i][0]
                QtyInStock =resProd[i][1]
                #fetch all rows in cart for a particular prod slno
                q2 = "SELECT qty FROM  cart WHERE slno = %s "
                mycur.execute(q2,(ProdSlno,))
                resCart = mycur.fetchall()
                j=0
                ReaminingQty = int(QtyInStock)
                for row in resCart:
                    updatedQty = resCart[j][0]

                    #calcualte the remaining Qty and update in Products table for the respective product
                    ReaminingQty = ReaminingQty - int(updatedQty)
                   
                    q3 = "UPDATE  products SET qty = %s WHERE slno = %s"                
                    mycur.execute(q3,(ReaminingQty,ProdSlno))
                    mycon.commit()
                j=j+1
        i=i+1

        q4="DELETE from cart WHERE email = %s"
        mycur.execute(q4,(myemail,))
        mycon.commit()

    def MainWindow(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
