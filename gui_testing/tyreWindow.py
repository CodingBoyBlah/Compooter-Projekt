


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window2(object):
    def setupUi(self, window2):
        window2.setObjectName("window2")
        window2.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(window2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        window2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 18))
        self.menubar.setObjectName("menubar")
        window2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window2)
        self.statusbar.setObjectName("statusbar")
        window2.setStatusBar(self.statusbar)

        self.retranslateUi(window2)
        QtCore.QMetaObject.connectSlotsByName(window2)

    def retranslateUi(self, window2):
        _translate = QtCore.QCoreApplication.translate
        window2.setWindowTitle(_translate("window2", "MainWindow"))
        self.label.setText(_translate("window2", "Tyre"))
        self.label_2.setText(_translate("window2", "A Tyre is the one which ultimately supports and runs the car.\n"
""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window2 = QtWidgets.QMainWindow()
    ui = Ui_window2()
    ui.setupUi(window2)
    window2.show()
    sys.exit(app.exec_())
