'''
    Steeringg.py
    
    implementation file for steerig window handling

'''

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog, QMessageBox
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
class Ui_commonSteeringsWindow(QMainWindow):
    def __init__(self, ui_file,subType):
        super(Ui_commonSteeringsWindow, self).__init__()

        self.ui_name = ui_file[:-3]
        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, ui_file)
        # Load the ui file
        uic.loadUi(filepath,self)


        if (subType == "carbon"):
            self.button1 = self.findChild(QPushButton, 'add_19')
            self.button2 = self.findChild(QPushButton, 'add_20')
            self.button3 = self.findChild(QPushButton, 'add_21')

            self.button1.clicked.connect(lambda:AddToCart(19))
            self.button2.clicked.connect(lambda:AddToCart(20))
            self.button3.clicked.connect(lambda:AddToCart(21))


        if (subType == "drift"):
            self.button1 = self.findChild(QPushButton, 'add_22')
            self.button2 = self.findChild(QPushButton, 'add_23')
            self.button3 = self.findChild(QPushButton, 'add_24')

            self.button1.clicked.connect(lambda:AddToCart(22))
            self.button2.clicked.connect(lambda:AddToCart(23))
            self.button3.clicked.connect(lambda:AddToCart(24))


        if (subType == "track"):
            self.button1 = self.findChild(QPushButton, 'add_25')
            self.button2 = self.findChild(QPushButton, 'add_26')
            self.button3 = self.findChild(QPushButton, 'add_27')

            self.button1.clicked.connect(lambda:AddToCart(25))
            self.button2.clicked.connect(lambda:AddToCart(26))
            self.button3.clicked.connect(lambda:AddToCart(27))



###############################################################################

class Ui_SteeringWindow(QMainWindow):
    def __init__(self,loginUser):
        super(Ui_SteeringWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'Steeringg.ui')
        # Load the ui file
        uic.loadUi(filepath,self)
        self.SteeringBack = self.findChild(QPushButton, 'SteeringBack')
        self.SteeringBack.clicked.connect(self.steering_close)

        self.rims = self.findChild(QPushButton, 'track')
        self.track = self.findChild(QPushButton, 'drift')
        self.offroad = self.findChild(QPushButton, 'carbon')

        self.rims.clicked.connect(self.rims_handler)
        self.track.clicked.connect(self.track_handler)
        self.offroad.clicked.connect(self.offroad_handler)

        global myemail
        myemail = loginUser

    def rims_handler(self):
        print("rims_handler")
        self.rims_Steering = Ui_commonSteeringsWindow("TrackSteering.ui",'track')
        self.rims_Steering.show()
        pass

    def track_handler(self):
        print("track_handler")
        self.track_Steering = Ui_commonSteeringsWindow("drift steering.ui",'drift')
        self.track_Steering.show()
        pass

    def offroad_handler(self):
        print("offroad_handler")
        self.offroad_Steering = Ui_commonSteeringsWindow("carbon steering.ui",'carbon')
        self.offroad_Steering.show()
        pass

    def steering_close(self):
        print("steering_close")
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_SteeringWindow()
    ui.show()
    sys.exit(app.exec_())
