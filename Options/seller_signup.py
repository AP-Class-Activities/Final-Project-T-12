# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seller_signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import re

class Ui_SellerSignup(object):
    def setupUi(self, SellerSignup):
        
        #confirms Default as false
        self.emailconfirm,self.ageconfirm,self.passwordconfirm = False,False,False
        SellerSignup.setObjectName("SellerSignup")
        SellerSignup.resize(800, 797)
        self.centralwidget = QtWidgets.QWidget(SellerSignup)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 70, 151, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/Avatar.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 270, 91, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-family : B Nazanin , Arial;\n"
"color:rgb(1, 14, 255)")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(600, 360, 151, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font-family : B Nazanin , Arial;\n"
"color:rgb(1, 14, 255)")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(610, 450, 141, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font-family : B Nazanin , Arial;\n"
"color:rgb(1, 14, 255)")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(630, 540, 121, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font-family : B Nazanin , Arial;\n"
"color:rgb(1, 14, 255)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(660, 630, 91, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font-family : B Nazanin , Arial;\n"
"color:rgb(1, 14, 255)")
        self.label_10.setObjectName("label_10")
        self.firstName_newSeller_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.firstName_newSeller_lineEdit.setGeometry(QtCore.QRect(190, 280, 401, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.firstName_newSeller_lineEdit.setFont(font)
        self.firstName_newSeller_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.firstName_newSeller_lineEdit.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;\n"
"color: rgb(42, 42, 136);")
        self.firstName_newSeller_lineEdit.setObjectName("firstName_newSeller_lineEdit")
        self.lastName_newSeller_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lastName_newSeller_lineEdit.setGeometry(QtCore.QRect(190, 370, 401, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.lastName_newSeller_lineEdit.setFont(font)
        self.lastName_newSeller_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lastName_newSeller_lineEdit.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;\n"
"color: rgb(42, 42, 136);")
        self.lastName_newSeller_lineEdit.setObjectName("lastName_newSeller_lineEdit")
        self.email_newSeller_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.email_newSeller_lineEdit.setGeometry(QtCore.QRect(190, 460, 401, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.email_newSeller_lineEdit.setFont(font)
        self.email_newSeller_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.email_newSeller_lineEdit.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;\n"
"color: rgb(42, 42, 136);")
        self.email_newSeller_lineEdit.setObjectName("email_newSeller_lineEdit")
        self.birthYear_newSeller_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.birthYear_newSeller_lineEdit.setGeometry(QtCore.QRect(190, 550, 401, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.birthYear_newSeller_lineEdit.setFont(font)
        self.birthYear_newSeller_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.birthYear_newSeller_lineEdit.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;\n"
"color: rgb(42, 42, 136);")
        self.birthYear_newSeller_lineEdit.setObjectName("birthYear_newSeller_lineEdit")
        self.password_newSeller_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_newSeller_lineEdit.setGeometry(QtCore.QRect(190, 640, 401, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.password_newSeller_lineEdit.setFont(font)
        self.password_newSeller_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.password_newSeller_lineEdit.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;\n"
"color: rgb(42, 42, 136);")
        self.password_newSeller_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_newSeller_lineEdit.setObjectName("password_newSeller_lineEdit")
        self.save_newSeller = QtWidgets.QPushButton(self.centralwidget)
        self.save_newSeller.setGeometry(QtCore.QRect(350, 720, 93, 28))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        self.save_newSeller.setFont(font)
        self.save_newSeller.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"background-color: rgb(61, 135, 255);\n"
"border-radius:20%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family:B Nazanin, Arial\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color:rgb(61, 135, 255);\n"
"background-color:white;\n"
"border-radius:20%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family:B Nazanin, Arial\n"
"}")
        self.save_newSeller.setObjectName("save_newSeller")
        #Connecting pushbutton to their Functions
        self.save_newSeller.clicked.connect(self.checkEmail)
        self.save_newSeller.clicked.connect(self.checkBirthyear)
        self.save_newSeller.clicked.connect(self.checkPassword)
        self.save_newSeller.clicked.connect(self.saveNewSeller)
        
        self.email_error = QtWidgets.QLabel(self.centralwidget)
        
        self.email_error.setGeometry(QtCore.QRect(0, 460, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.email_error.setFont(font)
        self.email_error.setStyleSheet("color: red;")
        self.email_error.setText("")
        self.email_error.setAlignment(QtCore.Qt.AlignCenter)
        self.email_error.setObjectName("email_error")
        self.age_error = QtWidgets.QLabel(self.centralwidget)
        self.age_error.setGeometry(QtCore.QRect(0, 550, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.age_error.setFont(font)
        self.age_error.setStyleSheet("color: red;")
        self.age_error.setText("")
        self.age_error.setAlignment(QtCore.Qt.AlignCenter)
        self.age_error.setObjectName("age_error")
        self.password_error = QtWidgets.QLabel(self.centralwidget)
        self.password_error.setGeometry(QtCore.QRect(0, 620, 191, 141))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.password_error.setFont(font)
        self.password_error.setStyleSheet("color: red;")
        self.password_error.setText("")
        self.password_error.setAlignment(QtCore.Qt.AlignCenter)
        self.password_error.setObjectName("password_error")

        SellerSignup.setCentralWidget(self.centralwidget)
        self.SellerSignup = SellerSignup
        file = open('seller_data.txt', 'r')
        lines = file.readlines()
        #
        self.code = len(lines)
        
        file.close()

        self.retranslateUi(SellerSignup)
        QtCore.QMetaObject.connectSlotsByName(SellerSignup)

    def checkEmail(self, email):
        email = self.email_newSeller_lineEdit.text()
        pattern = '^(\w|\.|\_|\-)+[@](\w|\_|\-)+[.]\w{2,3}$'
        if re.search(pattern, email) == None :
            self.email_error.setText("*Invalid Email")
        else :
            self.email_error.setText("")
            self.emailconfirm = True

    def checkBirthyear(self):
        birth_year = self.birthYear_newSeller_lineEdit.text()
        if int(birth_year) <= 1382 and int(birth_year) >= 1300 :
            self.age_error.setText("")
            self.ageconfirm = True
        else:
            self.age_error.setText("*Users must be over 18")

    def checkPassword(self):
        password = self.password_newSeller_lineEdit.text()
        status = True
        if len(password) < 8:
            status = False
        if re.search('[0-9]', password) is None :
            status = False
        if re.search('[A-Z]', password) is None :
            status = False
        if re.search('[a-z]', password) is None :
            status = False
        if status == True:
            self.password_error.setText("")
            self.passwordconfirm = True
        else:
            self.password_error.setText("*Password must have\natleast 8 characters\none upper-case letter\none lower-case letter\none number")

    def saveNewSeller(self):
        if self.emailconfirm == True and self.ageconfirm == True and self.passwordconfirm == True:
            s_code = str(self.code)
            s_code = s_code.zfill(6)
            s_code = 'SL'+s_code
            new_seller =[ self.firstName_newSeller_lineEdit.text(), self.lastName_newSeller_lineEdit.text(),self.email_newSeller_lineEdit.text(),self.birthYear_newSeller_lineEdit.text(), self.password_newSeller_lineEdit.text(),s_code]
            new_seller_str = " , ".join(str(x) for x in new_seller) + "\n"
            with open('seller_data.txt' , 'a+',encoding="utf-8-sig") as file:
                file.write(new_seller_str)
            with open('seller_wallet.txt','a') as file:
                file.write(self.email_newSeller_lineEdit.text()+':0'+'\n')
            self.SellerSignup.close()

        

    def retranslateUi(self, SellerSignup):
        _translate = QtCore.QCoreApplication.translate
        SellerSignup.setWindowTitle(_translate("SellerSignup", "Sign-up as Seller"))
        self.SellerSignup.setWindowIcon(QIcon('Images/null.png'))
        self.label_2.setText(_translate("SellerSignup", " نام:"))
        self.label_7.setText(_translate("SellerSignup", " نام خانوادگی:"))
        self.label_8.setText(_translate("SellerSignup", " آدرس ایمیل:"))
        self.label_9.setText(_translate("SellerSignup", " سال تولد:"))
        self.label_10.setText(_translate("SellerSignup", " رمز عبور:"))
        self.save_newSeller.setText(_translate("SellerSignup", "ثبت"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SellerSignup = QtWidgets.QMainWindow()
    ui = Ui_SellerSignup()
    ui.setupUi(SellerSignup)
    SellerSignup.show()
    sys.exit(app.exec_())
