        # -*- coding: utf-8 -*-

        # Form implementation generated from reading ui file 'Dialog.ui'
        #
        # Created by: PyQt5 UI code generator 5.15.9
        #
        # WARNING: Any manual changes made to this file will be lost when pyuic5 is
        # run again.  Do not edit this file unless you know what you are doing.

import mysql.connector as mys

mycon=mys.connect(host='localhost', user='root', password='slay', database='torquecart')
mycursor=mycon.cursor()

from PyQt5 import QtCore, QtGui, QtWidgets

username, email, password = '','',''

class Ui_SignUpDialog(object):
        

        def setupUi(self, Dialog):
                Dialog.setObjectName("Dialog")
                Dialog.resize(1202, 801)


                self.label = QtWidgets.QLabel(Dialog)
                self.label.setGeometry(QtCore.QRect(-140, -30, 1541, 831))
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap("C:\\Users\\evaan\\OneDrive\\Documents\\GitHub\\Compooter-Projekt\\gui_testing_modified\\torqucart.jpg"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")


                self.label_2 = QtWidgets.QLabel(Dialog)
                self.label_2.setGeometry(QtCore.QRect(0, 40, 1201, 121))
                self.label_2.setStyleSheet("color: rgb(191, 191, 191);\nfont: 42pt \"Asus Rog\";")
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
                self.label_6 = QtWidgets.QLabel(Dialog)
                self.label_6.setGeometry(QtCore.QRect(270, 600, 211, 41))
                self.label_6.setStyleSheet("color: rgb(225,225,225);\n"
        "font: 15pt \"ROG Fonts\";")
                self.label_6.setScaledContents(False)
                self.label_6.setObjectName("label_6")

        #PASSWORD
                self.Password = QtWidgets.QLineEdit(Dialog)
                self.Password.setGeometry(QtCore.QRect(500, 600, 391, 41))
                self.Password.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
                self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
                self.Password.setObjectName("Password")


        #BUTTON
                self.SignIN = QtWidgets.QPushButton(Dialog)
                self.SignIN.setGeometry(QtCore.QRect(510, 690, 131, 51))
                self.SignIN.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../Downloads/back-undo-return-button-png-5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.SignIN.setIcon(icon)
                self.SignIN.setObjectName("SignIN")


                self.line = QtWidgets.QFrame(Dialog)
                self.line.setGeometry(QtCore.QRect(120, 190, 971, 31))
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.label_7 = QtWidgets.QLabel(Dialog)
                self.label_7.setGeometry(QtCore.QRect(490, 290, 441, 81))
                self.label_7.setStyleSheet("color: rgb(225,225,225);\n"
        "font: 15pt \"Oswald SemiBold\";")
                self.label_7.setScaledContents(False)
                self.label_7.setObjectName("label_7")
                self.label_8 = QtWidgets.QLabel(Dialog)
                self.label_8.setGeometry(QtCore.QRect(340, 520, 211, 41))
                self.label_8.setStyleSheet("color: rgb(225,225,225);\n"
        "font: 15pt \"ROG Fonts\";")
                self.label_8.setScaledContents(False)
                self.label_8.setObjectName("label_8")

        #EMAIL
                self.Email_2 = QtWidgets.QLineEdit(Dialog)
                self.Email_2.setGeometry(QtCore.QRect(500, 520, 391, 41))
                self.Email_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
                self.Email_2.setObjectName("Email_2")

                self.label_9 = QtWidgets.QLabel(Dialog)
                self.label_9.setGeometry(QtCore.QRect(260, 440, 211, 41))
                self.label_9.setStyleSheet("color: rgb(225,225,225);\n"
        "font: 15pt \"ROG Fonts\";")
                self.label_9.setScaledContents(False)
                self.label_9.setObjectName("label_9")

        #USERNAME
                self.Email_3 = QtWidgets.QLineEdit(Dialog)
                self.Email_3.setGeometry(QtCore.QRect(500, 440, 391, 41))
                self.Email_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
                self.Email_3.setText("")
                self.Email_3.setObjectName("Email_3")
                
                self.SignIN.clicked.connect(self.accept_username)
                self.SignIN.clicked.connect(self.accept_email)
                self.SignIN.clicked.connect(self.accept_password)
                self.SignIN.clicked.connect(self.savetodb)

                self.retranslateUi(Dialog)
                QtCore.QMetaObject.connectSlotsByName(Dialog)

        def savetodb(self):
                global username
                global email
                global password
                q="insert into userinfo(name,email,password) values('"+username+"','"+email+"','"+password+"')"
                mycursor.execute(q)
                mycon.commit()
        
        def accept_username(self):
                global username
                username = self.Email_3.text()

        def accept_email(self):
                global email
                email = self.Email_2.text()

        def accept_password(self):
                global password
                password = self.Password.text()


        def retranslateUi(self, Dialog):
                _translate = QtCore.QCoreApplication.translate
                Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
                self.label_2.setText(_translate("Dialog", "TORQUE CART"))
                self.label_3.setText(_translate("Dialog", "SIGN UP"))
                self.label_6.setText(_translate("Dialog", "Password :"))
                self.SignIN.setText(_translate("Dialog", "Sign Up!"))
                self.label_7.setText(_translate("Dialog", "Create your account!"))
                self.label_8.setText(_translate("Dialog", "Email : "))
                self.label_9.setText(_translate("Dialog", "USERNAME : "))


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_SignUpDialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
