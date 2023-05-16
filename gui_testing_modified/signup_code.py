
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog, QMessageBox
from PyQt5 import QtWidgets
from PyQt5 import uic
from pathlib import Path
import re

import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', password = 'slay', database = 'torquecart')
mycur = mycon.cursor()

class Ui_SignupWindow(QDialog):
    def __init__(self):
        super(Ui_SignupWindow, self).__init__()
        
        filepath = Path(__file__).parent.resolve()
        filepath = Path.joinpath(filepath, 'SIGNUP.ui')
        # Load the ui file
        uic.loadUi(filepath,self)

        self.username = self.findChild(QLineEdit, 'username')
        self.email = self.findChild(QLineEdit, 'email')
        self.password = self.findChild(QLineEdit, 'Password')
        self.signin = self.findChild(QPushButton, 'SignIN')

        self.SignIN.clicked.connect(self.signin_handler)

    def signin_handler(self):
        username = self.Username.text()
        email = self.email.text()
        password = self.password.text()
        #print(username, email, password)

        if ("" == username or "" == email or "" == password ):
            msgBox = QMessageBox()
            msgBox.setText("Username/Email/Password cannot be empty. All fields are mandatory.")
            msgBox.exec()
        else:
            # Make a regular expression
            # for validating an Email
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
             
               
            # pass the regular expression
            # and the string into the fullmatch() method
            if(re.fullmatch(regex, email)):
                
                # if username exists
                mycur.execute("SELECT * FROM userinfo WHERE email = %s", [email])
                usercheck=mycur.fetchall()
                if usercheck :
                    msgBox = QMessageBox()
                    msgBox.setText("User already exists. Please Log In")
                    msgBox.exec()
                else:
                    #  insert username/email/password into table
                    q="insert into userinfo(name,email,password) values('"+username+"','"+email+"','"+password+"')"
                    mycur.execute(q)
                    mycon.commit()
                    #  "account created successfully."
                    msgBox = QMessageBox()
                    msgBox.setText("User "+username+" registered successfully")
                    msgBox.exec()
                self.close()
            else:
                msgBox = QMessageBox()
                msgBox.setText("Enter valid email")
                msgBox.exec()  
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_SignupWindow()
    ui.show()
    sys.exit(app.exec_())
