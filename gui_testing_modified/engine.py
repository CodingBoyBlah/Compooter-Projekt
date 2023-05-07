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
class Ui_V8EngineWindow(QMainWindow):
    def __init__(self):
        super(Ui_V8EngineWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'v8_engines.ui')
        # Load the ui file
        uic.loadUi(filepath,self)


        self.button1 = self.findChild(QPushButton, 'add_4')
        self.button2 = self.findChild(QPushButton, 'add_5')
        self.button3 = self.findChild(QPushButton, 'add_6')

        self.button1.clicked.connect(lambda:AddToCart(4))
        self.button2.clicked.connect(lambda:AddToCart(5))
        self.button3.clicked.connect(lambda:AddToCart(6))


###################################################################################         

class Ui_Flat6EngineWindow(QMainWindow):
    def __init__(self):
        super(Ui_Flat6EngineWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'flatsix engine.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.button1 = self.findChild(QPushButton, 'add_1')
        self.button2 = self.findChild(QPushButton, 'add_2')
        self.button3 = self.findChild(QPushButton, 'add_3')

        self.button1.clicked.connect(lambda:AddToCart(1))
        self.button2.clicked.connect(lambda:AddToCart(2))
        self.button3.clicked.connect(lambda:AddToCart(3))

###################################################################################


class Ui_V10EngineWindow(QMainWindow):
    def __init__(self):
        super(Ui_V10EngineWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'v10_engines.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        
        
        self.button1 = self.findChild(QPushButton, 'add_7')
        self.button2 = self.findChild(QPushButton, 'add_8')
        self.button3 = self.findChild(QPushButton, 'add_9')

        self.button1.clicked.connect(lambda:AddToCart(7))
        self.button2.clicked.connect(lambda:AddToCart(8))
        self.button3.clicked.connect(lambda:AddToCart(9))


###############################################################################

class Ui_EngineWindow(QMainWindow):
    def __init__(self):
        super(Ui_EngineWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'engine window.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.air = self.findChild(QPushButton, 'v8')
        self.track = self.findChild(QPushButton, 'flat6')
        self.offroad = self.findChild(QPushButton, 'v10')

        self.v8.clicked.connect(self.v8_handler)
        self.flat6.clicked.connect(self.flat6_handler)
        self.v10.clicked.connect(self.v10_handler)



    def v8_handler(self):
        print("v8_handler")
        self.v8_engine = Ui_V8EngineWindow()
        self.v8_engine.show()
        pass

    def flat6_handler(self):
        print("flat6_handler")
        self.flatsix_engine = Ui_Flat6EngineWindow()
        self.flatsix_engine.show()
        pass

    def v10_handler(self):
        print("v10_handler")
        self.v10_engine = Ui_V10EngineWindow()
        self.v10_engine.show()
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_EngineWindow()
    ui.show()
    sys.exit(app.exec_())
