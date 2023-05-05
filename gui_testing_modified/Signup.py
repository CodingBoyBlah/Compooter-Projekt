
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
from pathlib import Path

class Ui_SignupWindow(QDialog):
    def __init__(self):
        super(Ui_SignupWindow, self).__init__()
        
        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'SIGNUP.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.username = self.findChild(QLineEdit, 'Email_3')
        self.email = self.findChild(QLineEdit, 'Email_2')
        self.password = self.findChild(QLineEdit, 'Password')
        self.signin = self.findChild(QPushButton, 'SignIN')

        self.signin.clicked.connect(self.signin_handler)

    def signin_handler(self):
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()
        print(username, email, password)
        #TODO: ask user to change name if username exists
        #      ask user to change email if email exists
        #      insert username/email/password into table
        #      "account created successfully. click ok to close this window"
        #      close this window
        #sys.exit(app.exec_())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_SignupWindow()
    ui.show()
    sys.exit(app.exec_())
