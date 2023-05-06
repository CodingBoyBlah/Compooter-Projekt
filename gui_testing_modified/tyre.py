'''
    tyre.py
    
    implementation file for tyre window handling

'''

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog, QMessageBox
from PyQt5 import QtWidgets
from PyQt5 import uic
from pathlib import Path

import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', password = 'slay', database = 'torquecart')
mycur = mycon.cursor()
myemail="xyz"


 #Add item to Cart
def AddToCart(slno):        
    
    q4="SELECT price , item from products WHERE slno  = %s"
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
class Ui_commonTyresWindow(QMainWindow):
    def __init__(self, ui_file, subType):
        super(Ui_commonTyresWindow, self).__init__()

        self.ui_name = ui_file[:-3]
        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, ui_file)
        # Load the ui file
        uic.loadUi(filepath,self)


        if (subType == "track"):
            self.button1 = self.findChild(QPushButton, 'add_10')
            self.button2 = self.findChild(QPushButton, 'add_11')
            self.button3 = self.findChild(QPushButton, 'add_12')

            self.button1.clicked.connect(lambda:AddToCart(10))
            self.button2.clicked.connect(lambda:AddToCart(11))
            self.button3.clicked.connect(lambda:AddToCart(12))


        if (subType == "offroad"):
            self.button1 = self.findChild(QPushButton, 'add_13')
            self.button2 = self.findChild(QPushButton, 'add_14')
            self.button3 = self.findChild(QPushButton, 'add_15')

            self.button1.clicked.connect(lambda:AddToCart(13))
            self.button2.clicked.connect(lambda:AddToCart(14))
            self.button3.clicked.connect(lambda:AddToCart(15))


        if (subType == "street"):
            self.button1 = self.findChild(QPushButton, 'add_16')
            self.button2 = self.findChild(QPushButton, 'add_17')
            self.button3 = self.findChild(QPushButton, 'add_18')

            self.button1.clicked.connect(lambda:AddToCart(16))
            self.button2.clicked.connect(lambda:AddToCart(17))
            self.button3.clicked.connect(lambda:AddToCart(18))


###############################################################################

class Ui_tyreWindow(QMainWindow):
    def __init__(self,loginUser):
        super(Ui_tyreWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'tyres.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.track = self.findChild(QPushButton, 'track')
        self.offroad = self.findChild(QPushButton, 'offroad')
        self.street = self.findChild(QPushButton, 'street')

        self.track.clicked.connect(self.track_handler)
        self.offroad.clicked.connect(self.offroad_handler)
        self.street.clicked.connect(self.street_handler)

        global myemail
        myemail = loginUser

    def track_handler(self):
        print("track_handler")
        self.trackTyres = Ui_commonTyresWindow('track_tyres.ui','track')
        self.trackTyres.show()
        pass

    def offroad_handler(self):
        print("offroad_handler")
        self.offroadTyres = Ui_commonTyresWindow('offroad tyres.ui','offroad') #Ui_offroadTyresWindow()
        self.offroadTyres.show()
        pass

    def street_handler(self):
        print("street_handler")
        self.streetTyres = Ui_commonTyresWindow('street tyres.ui','street')#Ui_offroadSuspensionWindow()
        self.streetTyres.show()
        pass





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_tyreWindow()
    ui.show()
    sys.exit(app.exec_())
