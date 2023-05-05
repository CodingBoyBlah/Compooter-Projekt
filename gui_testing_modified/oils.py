'''
    oils.py
    
    implementation file for oil window handling

'''


from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
from pathlib import Path

###############################################################################
class Ui_offroadOilWindow(QMainWindow):
    def __init__(self):
        super(Ui_offroadOilWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'brake fluid.ui')
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


class Ui_transOilWindow(QMainWindow):
    def __init__(self):
        super(Ui_transOilWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'transmission oil.ui')
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


class Ui_engineOilWindow(QMainWindow):
    def __init__(self):
        super(Ui_engineOilWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'engine oil.ui')
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

class Ui_OilWindow(QMainWindow):
    def __init__(self):
        super(Ui_OilWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'Oils.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.rims = self.findChild(QPushButton, 'rims')
        self.track = self.findChild(QPushButton, 'track')
        self.offroad = self.findChild(QPushButton, 'offroad')

        self.rims.clicked.connect(self.rims_handler)
        self.track.clicked.connect(self.track_handler)
        self.offroad.clicked.connect(self.offroad_handler)



    def rims_handler(self):
        print("engine_handler")
        self.engine_Oil = Ui_engineOilWindow()
        self.engine_Oil.show()
        pass

    def track_handler(self):
        print("trans_handler")
        self.trans_Oil = Ui_transOilWindow()
        self.trans_Oil.show()
        pass

    def offroad_handler(self):
        print("offroad_handler")
        self.offroad_Oil = Ui_offroadOilWindow()
        self.offroad_Oil.show()
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_OilWindow()
    ui.show()
    sys.exit(app.exec_())
