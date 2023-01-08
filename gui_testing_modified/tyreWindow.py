
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton


from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_windowTyre(QMainWindow):
    def __init__(self):
        super(Ui_windowTyre, self).__init__()

        # Load the ui file
        uic.loadUi('tyreWindow.ui',self)

        self.backButton = self.findChild(QPushButton, 'backButton')
        self.rimsButton = self.findChild(QPushButton, 'rimsButton')
        self.offroadButton = self.findChild(QPushButton, 'offroadButton')
        self.sportsButton = self.findChild(QPushButton, 'sportsButton')
        self.radialButton = self.findChild(QPushButton, 'radialButton')

        self.backButton.clicked.connect(self.showUI)
        self.rimsButton.clicked.connect(self.showRimWindow)
        self.offroadButton.clicked.connect(self.showOffroadWindow)
        self.sportsButton.clicked.connect(self.showSportsWindow)
        self.radialButton.clicked.connect(self.showRadialWindow)

        self.show()

    def showUI(self):
        from website_proj2code import UI
        self.close()
        self.ui = UI()
        self.ui.show()

    def showRimWindow(self):
        from RimWindow_Code import Ui_RimWindow
        self.close()
        self.ui = Ui_RimWindow()
        self.ui.show()

    def showOffroadWindow(self):
        from offroadTyre_Code import Ui_offroadTyre
        self.close()
        self.ui = Ui_offroadTyre()
        self.ui.show()

    def showSportsWindow(self):
        from sportsTyre_Code import Ui_sportsWindow
        self.close()
        self.ui = Ui_sportsWindow()
        self.ui.show()

    def showRadialWindow(self):
        from radialWindow_Code import Ui_radialWindow
        self.close()
        self.ui = Ui_radialWindow()
        self.ui.show()



