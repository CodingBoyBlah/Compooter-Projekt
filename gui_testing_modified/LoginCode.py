# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LOGIN.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import mysql.connector as mys

mycon=mys.connect(host='localhost', user='root', password='root', database='torquecart')
mycursor=mycon.cursor()

from PyQt5 import QtCore, QtGui, QtWidgets
from signupcode import Ui_Dialog
from main_window import Ui_MainWindow

emailid, password1 = '',''

class Ui_Dialog(object):
        def setupUi(self, Dialog):
                Dialog.setObjectName("Dialog")
                Dialog.resize(1202, 824)
                self.label = QtWidgets.QLabel(Dialog)
                self.label.setGeometry(QtCore.QRect(-140, -30, 1541, 861))
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap("C:\\Users\\evaan\\OneDrive\\Documents\\GitHub\\Compooter-Projekt\\gui_testing_modified\\torqucart.jpg"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(Dialog)
                self.label_2.setGeometry(QtCore.QRect(0, 40, 1201, 121))
                self.label_2.setStyleSheet("color: rgb(191, 191, 191);\n"
        "font: 42pt \"ROG Fonts\";")
                self.label_2.setScaledContents(False)
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(Dialog)
                self.label_3.setGeometry(QtCore.QRect(0, 210, 1201, 121))
                self.label_3.setStyleSheet("color: rgb(225,225,225);\n"
        "font: 30pt \"ROG Fonts\";")
                self.label_3.setScaledContents(False)
                self.label_3.setAlignment(QtCore.Qt.AlignCenter)
                self.label_3.setObjectName("label_3")
                self.label_5 = QtWidgets.QLabel(Dialog)
                self.label_5.setGeometry(QtCore.QRect(330, 390, 211, 41))
                self.label_5.setStyleSheet("color: rgb(225,225,225);\n"
        "font: 15pt \"ROG Fonts\";")
                self.label_5.setScaledContents(False)
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(Dialog)
                self.label_6.setGeometry(QtCore.QRect(290, 470, 211, 41))
                self.label_6.setStyleSheet("color: rgb(225,225,225);\n"
        "font: 15pt \"ROG Fonts\";")
                self.label_6.setScaledContents(False)
                self.label_6.setObjectName("label_6")

                #EMAIL
                self.Email = QtWidgets.QLineEdit(Dialog)
                self.Email.setGeometry(QtCore.QRect(520, 390, 391, 41))
                self.Email.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
                self.Email.setObjectName("Email")


                #PASSWORD
                self.Password = QtWidgets.QLineEdit(Dialog)
                self.Password.setGeometry(QtCore.QRect(520, 470, 391, 41))
                self.Password.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
                self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
                self.Password.setObjectName("Password")


                #SIGNIN BUTTON
                self.SignIN = QtWidgets.QPushButton(Dialog)
                self.SignIN.setGeometry(QtCore.QRect(530, 570, 131, 51))
                self.SignIN.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../Downloads/back-undo-return-button-png-5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.SignIN.setIcon(icon)
                self.SignIN.setObjectName("SignIN")


                #CREATE ACCOUNT BUTTON
                self.Register = QtWidgets.QPushButton(Dialog)
                self.Register.setGeometry(QtCore.QRect(690, 710, 201, 51))
                self.Register.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
                self.Register.setIcon(icon)
                self.Register.setObjectName("Register")


                self.line = QtWidgets.QFrame(Dialog)
                self.line.setGeometry(QtCore.QRect(120, 190, 971, 31))
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.label_7 = QtWidgets.QLabel(Dialog)
                self.label_7.setGeometry(QtCore.QRect(230, 690, 441, 81))
                self.label_7.setStyleSheet("color: rgb(225,225,225);\n"
        "font: 15pt \"Oswald SemiBold\";")
                self.label_7.setScaledContents(False)
                self.label_7.setObjectName("label_7")
                self.line_2 = QtWidgets.QFrame(Dialog)
                self.line_2.setGeometry(QtCore.QRect(130, 660, 971, 31))
                self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_2.setObjectName("line_2")
                
                self.SignIN.clicked.connect(self.accept_email)
                self.SignIN.clicked.connect(self.accept_password)
                self.SignIN.clicked.connect(self.savetodb)

                self.Register.clicked.connect(self.movetocreate)


                self.retranslateUi(Dialog)
                QtCore.QMetaObject.connectSlotsByName(Dialog)

        def accept_email(self):
                global emailid
                emailid = self.Email.text()
        
        def accept_password(self):
                global password1
                password1 = self.Password.text()

        
        def savetodb(self):
                global emailid
                global password1
                mycursor.execute("SELECT password FROM userinfo WHERE email = %s", [emailid])
                passcheck=mycursor.fetchone()
                password = ''
                for item in passcheck:
                        password = password + item
                if password == password1:
                        print(password1)
                        q="insert into activeuser values('"+emailid+"')"
                        mycursor.execute(q)
                        mycon.commit()
                        self.main_window = Ui_MainWindow()
                        self.main_window.parent = self
                        self.main_window.show()
                        self.hide()

        
        def movetocreate(self):
                self.signup_window = Ui_Dialog()
                self.signup_window.show()

                        

                #q="insert into userinfo(name,email,password) values('"+username+"','"+email+"','"+password+"')"
                #mycursor.execute(q)
                #mycon.commit()

        
        def retranslateUi(self, Dialog):
                _translate = QtCore.QCoreApplication.translate
                Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
                self.label_2.setText(_translate("Dialog", "TORQUE CART"))
                self.label_3.setText(_translate("Dialog", "LOG IN "))
                self.label_5.setText(_translate("Dialog", "Email : "))
                self.label_6.setText(_translate("Dialog", "Password :"))
                self.SignIN.setText(_translate("Dialog", "Log In"))
                self.Register.setText(_translate("Dialog", "Create New Account"))
                self.label_7.setText(_translate("Dialog", "Don\'t have an account yet? Create one here"))

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
