'''
    suspension.py
    
    implementation file for exhaust window handling
    
'''

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog , QMessageBox
from PyQt5 import QtWidgets
from PyQt5 import uic
from pathlib import Path


import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', password = 'slay', database = 'torquecart')
mycur = mycon.cursor()
myemail=""


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
class Ui_SliponExhaustWindow(QMainWindow):
    def __init__(self):
        super(Ui_SliponExhaustWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'SliponExhaust.ui')
        # Load the ui file
        uic.loadUi(filepath,self)


        self.button1 = self.findChild(QPushButton, 'add_49')
        self.button2 = self.findChild(QPushButton, 'add_50')
        self.button3 = self.findChild(QPushButton, 'add_51')

        self.button1.clicked.connect(lambda:AddToCart(49))
        self.button2.clicked.connect(lambda:AddToCart(50))
        self.button3.clicked.connect(lambda:AddToCart(51))


###################################################################################         

class Ui_FullsysExhaustsWindow(QMainWindow):
    def __init__(self):
        super(Ui_FullsysExhaustsWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'FullsysExhausts.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.button1 = self.findChild(QPushButton, 'add_52')
        self.button2 = self.findChild(QPushButton, 'add_53')
        self.button3 = self.findChild(QPushButton, 'add_54')

        self.button1.clicked.connect(lambda:AddToCart(52))
        self.button2.clicked.connect(lambda:AddToCart(53))
        self.button3.clicked.connect(lambda:AddToCart(54))

###################################################################################


class Ui_FactoryExhaustWindow(QMainWindow):
    def __init__(self):
        super(Ui_FactoryExhaustWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'factory exhausts.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        
        
        self.button1 = self.findChild(QPushButton, 'add_46')
        self.button2 = self.findChild(QPushButton, 'add_47')
        self.button3 = self.findChild(QPushButton, 'add_48')

        self.button1.clicked.connect(lambda:AddToCart(46))
        self.button2.clicked.connect(lambda:AddToCart(47))
        self.button3.clicked.connect(lambda:AddToCart(48))


###############################################################################

class Ui_ExhaustWindow(QMainWindow):
    def __init__(self,loginUser):
        super(Ui_ExhaustWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'exhaust.ui')
        # Load the ui file
        uic.loadUi(filepath,self)
        self.ExhaustBack = self.findChild(QPushButton, 'ExhaustBack')
        self.ExhaustBack.clicked.connect(self.exhaust_close)

        self.air = self.findChild(QPushButton, 'sliponbutton')
        self.track = self.findChild(QPushButton, 'fullsysbutton')
        self.offroad = self.findChild(QPushButton, 'factorybutton_2')

        self.sliponbutton.clicked.connect(self.slipon_handler)
        self.fullsysbutton.clicked.connect(self.fullsys_handler)
        self.factorybutton_2.clicked.connect(self.factory_handler)

        global myemail
        myemail = loginUser



    def slipon_handler(self):
        print("air_handler")
        self.slipon_exhaust = Ui_SliponExhaustWindow()
        self.slipon_exhaust.show()
        pass

    def fullsys_handler(self):
        print("track_handler")
        self.fullsystem_exhaust = Ui_FullsysExhaustsWindow()
        self.fullsystem_exhaust.show()
        pass

    def factory_handler(self):
        print("offroad_handler")
        self.factory_exhaust = Ui_FactoryExhaustWindow()
        self.factory_exhaust.show()
        pass

    def exhaust_close(self):
        print("exhaust_close")
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_ExhaustWindow()
    ui.show()
    sys.exit(app.exec_())
