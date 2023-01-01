from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
from tyreWindow import Ui_window2
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
        self.suspensionButton.clicked.connect(self.openSuspensionWindow)
        self.engineButton.clicked.connect(self.openEngineWindow)

        self.show()

    def openTyreWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_window2()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSuspensionWindow(self):
        from suspensionWindowCode import Ui_suspensionWindow
        self.suspension_window = Ui_suspensionWindow()
        self.suspension_window.show()

    def openEngineWindow(self):
        from engineWindowCode import Ui_engineWindow
        self.engine_window = Ui_engineWindow()
        self.engine_window.show()


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
