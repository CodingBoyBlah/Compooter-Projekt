'''
    main_window.py

    implementation file for main window handling

'''

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
from pathlib import Path
from suspension import Ui_SuspensionWindow
from Steeringg import Ui_SteeringWindow
from tyre import Ui_tyreWindow
from oils import Ui_OilWindow

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'main_window.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

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

    def closeEvent (self, event):
        print("main window destroyed")


    def tyres_handler(self):
        print("tyres_handler")
        self.suspension_window = Ui_tyreWindow()
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
