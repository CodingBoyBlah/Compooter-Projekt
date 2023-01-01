
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5 import uic
import sys

class Ui_suspensionWindow(QMainWindow):
    def __init__(self):
        super(Ui_suspensionWindow, self).__init__()

        # Load the ui file
        uic.loadUi('suspensionWindow.ui',self)

        # Defining Widgets
        self.header = self.findChild(QLabel, 'mainHeader')
        self.header_desc = self.findChild(QLabel, 'sus_desc')

# Initialize the app
app = QApplication(sys.argv)

# Create an instance of the Ui_suspensionWindow class, but do not show it yet
UIWindow = Ui_suspensionWindow()

# Show the app (now moved outside of the Ui_suspensionWindow class definition)
UIWindow.show()
app.exec_()
