'''
    suspension.py
    
    implementation file for suspension window handling
    
'''

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
from pathlib import Path


###############################################################################
class Ui_offroadSuspensionWindow(QMainWindow):
    def __init__(self):
        super(Ui_offroadSuspensionWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'offroad suspension.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.button1 = self.findChild(QPushButton, 'SignIN')
        self.button2 = self.findChild(QPushButton, 'SignIN_2')
        self.button3 = self.findChild(QPushButton, 'SignIN_3')

        self.button1.clicked.connect(self.button1_handler)
        self.button2.clicked.connect(self.button2_handler)
        self.button3.clicked.connect(self.button3_handler)



    def button1_handler(self):
        print("button1_handler")
        pass

    def button2_handler(self):
        print("button2_handler")
        pass

    def button3_handler(self):
        print("button3_handler")
        pass

class Ui_trackSuspensionWindow(QMainWindow):
    def __init__(self):
        super(Ui_trackSuspensionWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'track suspension.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.button1 = self.findChild(QPushButton, 'SignIN')
        self.button2 = self.findChild(QPushButton, 'SignIN_2')
        self.button3 = self.findChild(QPushButton, 'SignIN_3')

        self.button1.clicked.connect(self.button1_handler)
        self.button2.clicked.connect(self.button2_handler)
        self.button3.clicked.connect(self.button3_handler)



    def button1_handler(self):
        print("button1_handler")
        pass

    def button2_handler(self):
        print("button2_handler")
        pass

    def button3_handler(self):
        print("button3_handler")
        pass


class Ui_airSuspensionWindow(QMainWindow):
    def __init__(self):
        super(Ui_airSuspensionWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'air suspension.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.button1 = self.findChild(QPushButton, 'SignIN')
        self.button2 = self.findChild(QPushButton, 'SignIN_2')
        self.button3 = self.findChild(QPushButton, 'SignIN_3')

        self.button1.clicked.connect(self.button1_handler)
        self.button2.clicked.connect(self.button2_handler)
        self.button3.clicked.connect(self.button3_handler)



    def button1_handler(self):
        print("button1_handler")
        pass

    def button2_handler(self):
        print("button2_handler")
        pass

    def button3_handler(self):
        print("button3_handler")
        pass

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
