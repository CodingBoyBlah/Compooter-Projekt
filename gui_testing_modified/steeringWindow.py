
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_windowSteering(QMainWindow):
    def __init__(self):
        super(Ui_windowSteering, self).__init__()

        # Load the ui file
        uic.loadUi('steeringWindow.ui',self)

        self.backButton = self.findChild(QPushButton, 'backButton')
        #self.steeringWheelButton = self.findChild(QPushButton,'steeringWheelButton')


        self.backButton.clicked.connect(self.showUI)
        #self.steeringWheelButton.clicked.connect(self.showSteering)


        self.show()

    def showUI(self):
        from website_proj2code import UI
        self.close()
        self.ui = UI()
        self.ui.show()

    '''def showSteering(self):
        from radialWindow_Code import Ui_radialWindow
        self.close()
        self.ui = Ui_radialWindow()
        self.ui.show()'''


