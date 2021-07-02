from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import re

class Ui_CustomerSignup(object):
    def setupUi(self, CustomerSignup):
        self.emailconfirm,self.ageconfirm,self.passwordconfirm = False,False,False
        CustomerSignup.setObjectName("CustomerSignup")
        CustomerSignup.resize(797, 961)
        self.centralwidget = QtWidgets.QWidget(CustomerSignup)
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
        self.firstName_newCustomer_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.firstName_newCustomer_lineEdit.setGeometry(QtCore.QRect(190, 280, 401, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.firstName_newCustomer_lineEdit.setFont(font)
        self.firstName_newCustomer_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.firstName_newCustomer_lineEdit.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;\n"
"color: rgb(42, 42, 136);")
        self.firstName_newCustomer_lineEdit.setObjectName("firstName_newCustomer_lineEdit")
        self.lastName_newCustomer_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lastName_newCustomer_lineEdit.setGeometry(QtCore.QRect(190, 370, 401, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.lastName_newCustomer_lineEdit.setFont(font)
        self.lastName_newCustomer_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lastName_newCustomer_lineEdit.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;\n"
"color: rgb(42, 42, 136);")
        self.lastName_newCustomer_lineEdit.setObjectName("lastName_newCustomer_lineEdit")
        self.email_newCustomer_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.email_newCustomer_lineEdit.setGeometry(QtCore.QRect(190, 460, 401, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.email_newCustomer_lineEdit.setFont(font)
        self.email_newCustomer_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.email_newCustomer_lineEdit.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;\n"
"color: rgb(42, 42, 136);")
        self.email_newCustomer_lineEdit.setObjectName("email_newCustomer_lineEdit")
        self.birthYear_newCustomer_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.birthYear_newCustomer_lineEdit.setGeometry(QtCore.QRect(190, 550, 401, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.birthYear_newCustomer_lineEdit.setFont(font)
        self.birthYear_newCustomer_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.birthYear_newCustomer_lineEdit.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;\n"
"color: rgb(42, 42, 136);")
        self.birthYear_newCustomer_lineEdit.setObjectName("birthYear_newCustomer_lineEdit")
        self.password_newCustomer_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_newCustomer_lineEdit.setGeometry(QtCore.QRect(190, 640, 401, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.password_newCustomer_lineEdit.setFont(font)
        self.password_newCustomer_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.password_newCustomer_lineEdit.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;\n"
"color: rgb(42, 42, 136);")
        self.password_newCustomer_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_newCustomer_lineEdit.setObjectName("password_newCustomer_lineEdit")
        self.save_newCustomer = QtWidgets.QPushButton(self.centralwidget)
        self.save_newCustomer.setGeometry(QtCore.QRect(350, 910, 93, 28))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        self.save_newCustomer.setFont(font)
        self.save_newCustomer.setStyleSheet("QPushButton\n"
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
        self.save_newCustomer.setObjectName("save_newCustomer")
        self.save_newCustomer.clicked.connect(self.checkEmail)
        self.save_newCustomer.clicked.connect(self.checkBirthyear)
        self.save_newCustomer.clicked.connect(self.checkPassword)
        self.save_newCustomer.clicked.connect(self.saveNewCustomer)
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
        self.address_newCustomer_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.address_newCustomer_lineEdit.setGeometry(QtCore.QRect(190, 820, 401, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.address_newCustomer_lineEdit.setFont(font)
        self.address_newCustomer_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.address_newCustomer_lineEdit.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;\n"
"color: rgb(42, 42, 136);")
        self.address_newCustomer_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.address_newCustomer_lineEdit.setObjectName("address_newCustomer_lineEdit")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(650, 720, 91, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font-family : B Nazanin , Arial;\n"
"color:rgb(1, 14, 255)")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(650, 810, 91, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("font-family : B Nazanin , Arial;\n"
"color:rgb(1, 14, 255)")
        self.label_12.setObjectName("label_12")
        self.provice_combo = QtWidgets.QComboBox(self.centralwidget)
        self.provice_combo.setGeometry(QtCore.QRect(190, 730, 401, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.provice_combo.setFont(font)
        self.provice_combo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.provice_combo.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;\n"
"color: rgb(42, 42, 136);")
        self.provice_combo.setObjectName("provice_combo")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        self.provice_combo.addItem("")
        CustomerSignup.setCentralWidget(self.centralwidget)
        self.CustomerSignup = CustomerSignup
        file = open('customer_data.txt', 'r')
        lines = file.readlines()
        self.code = len(lines)
        file.close()

        self.retranslateUi(CustomerSignup)
        QtCore.QMetaObject.connectSlotsByName(CustomerSignup)

    def checkEmail(self, email):
        email = self.email_newCustomer_lineEdit.text()
        pattern = '^(\w|\.|\_|\-)+[@](\w|\_|\-)+[.]\w{2,3}$'
        if re.search(pattern, email) == None :
            self.email_error.setText("*Invalid Email")
        else :
            self.email_error.setText("")
            self.emailconfirm = True

    def checkBirthyear(self):
        birth_year = self.birthYear_newCustomer_lineEdit.text()
        if int(birth_year) <= 1382 and int(birth_year) >= 1300 :
            self.age_error.setText("")
            self.ageconfirm = True
        else:
            self.age_error.setText("*Users must be over 18")

    def checkPassword(self):
        password = self.password_newCustomer_lineEdit.text()
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
    

    #add customer
    def saveNewCustomer(self):
        if self.emailconfirm == True and self.ageconfirm == True and self.passwordconfirm == True:
            c_code = str(self.code)
            c_code = c_code.zfill(6)
            c_code = 'CU'+c_code
            new_customer =[ self.firstName_newCustomer_lineEdit.text(), self.lastName_newCustomer_lineEdit.text(),self.email_newCustomer_lineEdit.text(),self.birthYear_newCustomer_lineEdit.text(), self.password_newCustomer_lineEdit.text(),self.provice_combo.currentText(),self.address_newCustomer_lineEdit.text(),c_code]
            new_customer_str = "\n"+ " , ".join(str(x) for x in new_customer)
            with open('customer_data.txt' , 'a+',encoding="utf-8-sig") as file:
                file.write(new_customer_str)
            with open('customer_wallet.txt','a') as cwfile:
                cwfile.write(self.email_newCustomer_lineEdit.text()+':0'+'\n')
            self.CustomerSignup.close()
            

    def retranslateUi(self, CustomerSignup):
        _translate = QtCore.QCoreApplication.translate
        CustomerSignup.setWindowTitle(_translate("CustomerSignup", "Signup as Customer"))
        self.CustomerSignup.setWindowIcon(QIcon('Images/null.png'))
        self.label_2.setText(_translate("CustomerSignup", " نام:"))
        self.label_7.setText(_translate("CustomerSignup", " نام خانوادگی:"))
        self.label_8.setText(_translate("CustomerSignup", " آدرس ایمیل:"))
        self.label_9.setText(_translate("CustomerSignup", " سال تولد:"))
        self.label_10.setText(_translate("CustomerSignup", " رمز عبور:"))
        self.save_newCustomer.setText(_translate("CustomerSignup", "ثبت"))
        self.label_11.setText(_translate("CustomerSignup", "استان:"))
        self.label_12.setText(_translate("CustomerSignup", "آدرس:"))
        self.provice_combo.setItemText(0, _translate("CustomerSignup", "آذربایجان شرقی"))
        self.provice_combo.setItemText(1, _translate("CustomerSignup", "آذربایجان غربی"))
        self.provice_combo.setItemText(2, _translate("CustomerSignup", "اردبیل"))
        self.provice_combo.setItemText(3, _translate("CustomerSignup", "اصفهان"))
        self.provice_combo.setItemText(4, _translate("CustomerSignup", "البرز"))
        self.provice_combo.setItemText(5, _translate("CustomerSignup", "ایلام"))
        self.provice_combo.setItemText(6, _translate("CustomerSignup", "بوشهر"))
        self.provice_combo.setItemText(7, _translate("CustomerSignup", "تهران"))
        self.provice_combo.setItemText(8, _translate("CustomerSignup", "چهارمجال و بختیاری"))
        self.provice_combo.setItemText(9, _translate("CustomerSignup", "خراسان جنوبی"))
        self.provice_combo.setItemText(10, _translate("CustomerSignup", "خراسان رضوی"))
        self.provice_combo.setItemText(11, _translate("CustomerSignup", "خراسان شمالی"))
        self.provice_combo.setItemText(12, _translate("CustomerSignup", "خوزستان"))
        self.provice_combo.setItemText(13, _translate("CustomerSignup", "زنجان"))
        self.provice_combo.setItemText(14, _translate("CustomerSignup", "سمنان"))
        self.provice_combo.setItemText(15, _translate("CustomerSignup", "سیستان و بلوچستان"))
        self.provice_combo.setItemText(16, _translate("CustomerSignup", "فارس"))
        self.provice_combo.setItemText(17, _translate("CustomerSignup", "قزوین"))
        self.provice_combo.setItemText(18, _translate("CustomerSignup", "کردستان"))
        self.provice_combo.setItemText(19, _translate("CustomerSignup", "کرمان"))
        self.provice_combo.setItemText(20, _translate("CustomerSignup", "کرمانشاه"))
        self.provice_combo.setItemText(21, _translate("CustomerSignup", "گلستان"))
        self.provice_combo.setItemText(22, _translate("CustomerSignup", "گیلان"))
        self.provice_combo.setItemText(23, _translate("CustomerSignup", "لرستان"))
        self.provice_combo.setItemText(24, _translate("CustomerSignup", "مازندران"))
        self.provice_combo.setItemText(25, _translate("CustomerSignup", "مرکزی"))
        self.provice_combo.setItemText(26, _translate("CustomerSignup", "هرمزگان"))
        self.provice_combo.setItemText(27, _translate("CustomerSignup", "همدان"))
        self.provice_combo.setItemText(28, _translate("CustomerSignup", "یزد"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CustomerSignup = QtWidgets.QMainWindow()
    ui = Ui_CustomerSignup()
    ui.setupUi(CustomerSignup)
    CustomerSignup.show()
    sys.exit(app.exec_())
