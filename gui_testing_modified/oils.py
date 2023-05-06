'''
    oils.py
    
    implementation file for oil window handling

'''


from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog , QMessageBox
from PyQt5 import QtWidgets
from PyQt5 import uic
from pathlib import Path


import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', password = 'slay', database = 'torquecart')
mycur = mycon.cursor()
myemail="xyz"


 #Add item to Cart
def AddToCart(slno):        
    
    q4="SELECT price, item from products WHERE slno  = %s"
    mycur.execute(q4,(slno,))
    result = mycur.fetchall()

    global myemail

    q3 = "insert into cart (slno,qty,amt,email) values ('{0}','{1}','{2}','{3}')".format(slno,1, result[0][0],myemail)
    
    mycur.execute(q3)
    mycon.commit()

    msgBox = QMessageBox()
    mesg = "Added "+result[0][1]+" to cart"
    msgBox.setText(mesg)
    msgBox.exec()


###############################################################################
class Ui_brakeOilWindow(QMainWindow):
    def __init__(self):
        super(Ui_brakeOilWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'brake fluid.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        
        self.button1 = self.findChild(QPushButton, 'add_43')
        self.button2 = self.findChild(QPushButton, 'add_44')
        self.button3 = self.findChild(QPushButton, 'add_45')

        self.button1.clicked.connect(lambda:AddToCart(43))
        self.button2.clicked.connect(lambda:AddToCart(44))
        self.button3.clicked.connect(lambda:AddToCart(45))  
         


############################################################################


class Ui_transOilWindow(QMainWindow):
    def __init__(self):
        super(Ui_transOilWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'transmission oil.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.button1 = self.findChild(QPushButton, 'add_37')
        self.button2 = self.findChild(QPushButton, 'add_38')
        self.button3 = self.findChild(QPushButton, 'add_39')

        self.button1.clicked.connect(lambda:AddToCart(37))
        self.button2.clicked.connect(lambda:AddToCart(38))
        self.button3.clicked.connect(lambda:AddToCart(39)) 


#############################################################################

class Ui_engineOilWindow(QMainWindow):
    def __init__(self):
        super(Ui_engineOilWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'engine oil.ui')
        # Load the ui file
        uic.loadUi(filepath,self)


        self.button1 = self.findChild(QPushButton, 'add_40')
        self.button2 = self.findChild(QPushButton, 'add_41')
        self.button3 = self.findChild(QPushButton, 'add_42')

        self.button1.clicked.connect(lambda:AddToCart(40))
        self.button2.clicked.connect(lambda:AddToCart(41))
        self.button3.clicked.connect(lambda:AddToCart(42))




###############################################################################

class Ui_OilWindow(QMainWindow):
    def __init__(self):
        super(Ui_OilWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'Oils.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.engine = self.findChild(QPushButton, 'engine')
        self.transmission = self.findChild(QPushButton, 'transmission')
        self.breaks = self.findChild(QPushButton, 'breaks')

        self.engine.clicked.connect(self.engine_handler)
        self.transmission.clicked.connect(self.trans_handler)
        self.brake.clicked.connect(self.brake_handler)



    def engine_handler(self):
        print("engine_handler")
        self.engine_Oil = Ui_engineOilWindow()
        self.engine_Oil.show()
        pass

    def trans_handler(self):
        print("trans_handler")
        self.trans_Oil = Ui_transOilWindow()
        self.trans_Oil.show()
        pass

    def brake_handler(self):
        print("brake_handler")
        self.offroad_Oil = Ui_brakeOilWindow()
        self.offroad_Oil.show()
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_OilWindow()
    ui.show()
    sys.exit(app.exec_())
