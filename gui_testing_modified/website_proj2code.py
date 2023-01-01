from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
from tyreWindow import Ui_windowTyre
from steeringWindow import Ui_windowSteering
from engineWindow import Ui_windowEngine
from suspensionWindow import Ui_windowSuspension
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi('website_proj2gui.ui',self)

        # Defining Widgets
        self.tyreButton = self.findChild(QPushButton, 'tyreButton')
        self.steeringButton = self.findChild(QPushButton, 'steeringButton')
        self.engineButton = self.findChild(QPushButton, 'engineButton')
        self.suspensionButton = self.findChild(QPushButton, 'suspensionButton' )
        self.contactLabel = self.findChild(QLabel, 'contactLabel')
        self.emailLabel = self.findChild(QLabel, 'emailLabel')
        self.phoneLabel = self.findChild(QLabel, 'phoneLabel')
        self.mainLabel = self.findChild(QLabel, 'main_header_name')

        # When button pressed, Open new window
        self.tyreButton.clicked.connect(self.openTyreWindow)
        self.steeringButton.clicked.connect(self.openSteeringWindow)
        self.engineButton.clicked.connect(self.openEngineWindow)
        self.suspensionButton.clicked.connect(self.openSuspensionWindow)

        self.show()

    def openTyreWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_windowTyre()

    def openSteeringWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_windowSteering()

    def openEngineWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_windowEngine()

    def openSuspensionWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_windowSuspension()

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
