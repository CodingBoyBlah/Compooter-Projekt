
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5 import uic
import sys
from pathlib import Path

class Ui_engineWindow(QMainWindow):
    def __init__(self):
        super(Ui_engineWindow, self).__init__()

        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'engineWindow.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        # Defining Widgets
        self.header = self.findChild(QLabel, 'header_label')
        self.header_desc = self.findChild(QLabel, 'header_desc')

# Initialize the app
app = QApplication(sys.argv)

# Create an instance of the Ui_engineWindow class, but do not show it yet
UIWindow = Ui_engineWindow()

# Show the app (now moved outside of the Ui_engineWindow class definition)
UIWindow.show()
app.exec_()
