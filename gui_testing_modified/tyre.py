'''
    tyre.py
    
    implementation file for tyre window handling

'''

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
from pathlib import Path

###############################################################################
class Ui_commonTyresWindow(QMainWindow):
    def __init__(self, ui_file):
        super(Ui_commonTyresWindow, self).__init__()

        self.ui_name = ui_file[:-3]
        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, ui_file)
        # Load the ui file
        uic.loadUi(filepath,self)

        self.button1 = self.findChild(QPushButton, 'SignIN')
        self.button2 = self.findChild(QPushButton, 'SignIN_2')
        self.button3 = self.findChild(QPushButton, 'SignIN_3')

        self.button1.clicked.connect(self.button1_handler)
        self.button2.clicked.connect(self.button2_handler)
        self.button3.clicked.connect(self.button3_handler)



    def button1_handler(self):
        print(f"{self.ui_name} button1_handler")
        pass

    def button2_handler(self):
        print(f"{self.ui_name} button2_handler")
        pass

    def button3_handler(self):
        print(f"{self.ui_name} button3_handler")
        pass



###############################################################################

class Ui_tyreWindow(QMainWindow):
    def __init__(self):
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



    def track_handler(self):
        print("track_handler")
        self.trackTyres = Ui_commonTyresWindow('track_tyres.ui')
        self.trackTyres.show()
        pass

    def offroad_handler(self):
        print("offroad_handler")
        self.offroadTyres = Ui_commonTyresWindow('offroad tyres.ui') #Ui_offroadTyresWindow()
        self.offroadTyres.show()
        pass

    def street_handler(self):
        print("street_handler")
        self.offroad_suspension = Ui_commonTyresWindow('street tyres.ui') #Ui_offroadSuspensionWindow()
        self.offroad_suspension.show()
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_tyreWindow()
    ui.show()
    sys.exit(app.exec_())
