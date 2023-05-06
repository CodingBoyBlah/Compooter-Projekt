'''
    suspension.py
    
    implementation file for suspension window handling
    
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
class Ui_offroadSuspensionWindow(QMainWindow):
    def __init__(self):
        super(Ui_offroadSuspensionWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'offroad suspension.ui')
        # Load the ui file
        uic.loadUi(filepath,self)


        self.button1 = self.findChild(QPushButton, 'add_31')
        self.button2 = self.findChild(QPushButton, 'add_32')
        self.button3 = self.findChild(QPushButton, 'add_33')

        self.button1.clicked.connect(lambda:AddToCart(31))
        self.button2.clicked.connect(lambda:AddToCart(32))
        self.button3.clicked.connect(lambda:AddToCart(33))


###################################################################################         

class Ui_trackSuspensionWindow(QMainWindow):
    def __init__(self):
        super(Ui_trackSuspensionWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'track suspension.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.button1 = self.findChild(QPushButton, 'add_34')
        self.button2 = self.findChild(QPushButton, 'add_35')
        self.button3 = self.findChild(QPushButton, 'add_36')

        self.button1.clicked.connect(lambda:AddToCart(34))
        self.button2.clicked.connect(lambda:AddToCart(35))
        self.button3.clicked.connect(lambda:AddToCart(36))

###################################################################################


class Ui_airSuspensionWindow(QMainWindow):
    def __init__(self):
        super(Ui_airSuspensionWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'air suspension.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        
        
        self.button1 = self.findChild(QPushButton, 'add_28')
        self.button2 = self.findChild(QPushButton, 'add_29')
        self.button3 = self.findChild(QPushButton, 'add_30')

        self.button1.clicked.connect(lambda:AddToCart(28))
        self.button2.clicked.connect(lambda:AddToCart(29))
        self.button3.clicked.connect(lambda:AddToCart(30))


###############################################################################

class Ui_SuspensionWindow(QMainWindow):
    def __init__(self):
        super(Ui_SuspensionWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'Suspension.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.air = self.findChild(QPushButton, 'air')
        self.track = self.findChild(QPushButton, 'track')
        self.offroad = self.findChild(QPushButton, 'offroad')

        self.air.clicked.connect(self.air_handler)
        self.track.clicked.connect(self.track_handler)
        self.offroad.clicked.connect(self.offroad_handler)



    def air_handler(self):
        print("air_handler")
        self.air_suspension = Ui_airSuspensionWindow()
        self.air_suspension.show()
        pass

    def track_handler(self):
        print("track_handler")
        self.track_suspension = Ui_trackSuspensionWindow()
        self.track_suspension.show()
        pass

    def offroad_handler(self):
        print("offroad_handler")
        self.offroad_suspension = Ui_offroadSuspensionWindow()
        self.offroad_suspension.show()
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_SuspensionWindow()
    ui.show()
    sys.exit(app.exec_())
