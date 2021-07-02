from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Options import customer_panel

class Ui_CustomerLogin(object):
    def setupUi(self, CustomerLogin):
        CustomerLogin.setObjectName("CustomerLogin")
        CustomerLogin.resize(738, 643)
        self.centralwidget = QtWidgets.QWidget(CustomerLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 90, 171, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/LoginAvatar.png"))
        self.label.setObjectName("label")
        self.customer_email = QtWidgets.QLineEdit(self.centralwidget)
        self.customer_email.setGeometry(QtCore.QRect(200, 310, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.customer_email.setFont(font)
        self.customer_email.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);")
        self.customer_email.setObjectName("customer_email")
        self.customer_password = QtWidgets.QLineEdit(self.centralwidget)
        self.customer_password.setGeometry(QtCore.QRect(200, 410, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.customer_password.setFont(font)
        self.customer_password.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);")
        self.customer_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.customer_password.setObjectName("customer_password")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 310, 71, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 410, 121, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;")
        self.label_3.setObjectName("label_3")
        self.enterCustomer = QtWidgets.QPushButton(self.centralwidget)
        self.enterCustomer.setGeometry(QtCore.QRect(330, 520, 93, 28))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        self.enterCustomer.setFont(font)
        self.enterCustomer.setStyleSheet("QPushButton\n"
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
        self.enterCustomer.setObjectName("enterCustomer")
        self.enterCustomer.clicked.connect(self.enterAsCustomer)
        self.wrong_email = QtWidgets.QLabel(self.centralwidget)
        self.wrong_email.setGeometry(QtCore.QRect(40, 310, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wrong_email.setFont(font)
        self.wrong_email.setStyleSheet("color: red;")
        self.wrong_email.setText("")
        self.wrong_email.setAlignment(QtCore.Qt.AlignCenter)
        self.wrong_email.setObjectName("wrong_email")
        self.wrong_password = QtWidgets.QLabel(self.centralwidget)
        self.wrong_password.setGeometry(QtCore.QRect(30, 420, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wrong_password.setFont(font)
        self.wrong_password.setStyleSheet("color: red;")
        self.wrong_password.setText("")
        self.wrong_password.setAlignment(QtCore.Qt.AlignCenter)
        self.wrong_password.setObjectName("wrong_password")
        CustomerLogin.setCentralWidget(self.centralwidget)
        self.action = QtWidgets.QAction(CustomerLogin)
        self.action.setObjectName("action")
        self.CustomerLogin = CustomerLogin

        self.retranslateUi(CustomerLogin)
        QtCore.QMetaObject.connectSlotsByName(CustomerLogin)
    
    #check customer_data.txt
    def enterAsCustomer(self):
        email = self.customer_email.text()
        password = self.customer_password.text()
        customers = open('customer_data.txt', 'r')
        customers = customers.readlines()
        for i in customers:
            if i == 'ï»؟\n':
                customers.remove('ï»؟\n')
        customers = [customer.replace(' ','') for customer in customers]
        customers = [customer.replace('\n','').split(',') for customer in customers]
        for i in range(len(customers)):
            if email == customers[i][2] and password == customers[i][4]:
                self.customerPanel = QtWidgets.QMainWindow()
                self.ui = customer_panel.Ui_CustomerPanel()
                self.ui.setupUi(self.customerPanel, email)
                self.customerPanel.show()
                self.CustomerLogin.close()
            elif password != customers[i][4]:
                self.wrong_password.setText("*Wrong password")
            elif email != customers[i][2]:
                self.wrong_email.setText("*Wrong email")

    def retranslateUi(self, CustomerLogin):
        _translate = QtCore.QCoreApplication.translate
        CustomerLogin.setWindowTitle(_translate("CustomerLogin", "Login as Customer"))
        self.CustomerLogin.setWindowIcon(QIcon('Images/null.png'))
        self.label_2.setText(_translate("CustomerLogin", "ایمیل:"))
        self.label_3.setText(_translate("CustomerLogin", "رمز عبور:"))
        self.enterCustomer.setText(_translate("CustomerLogin", "ورود"))
        self.action.setText(_translate("CustomerLogin", "دت"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CustomerLogin = QtWidgets.QMainWindow()
    ui = Ui_CustomerLogin()
    ui.setupUi(CustomerLogin)
    CustomerLogin.show()
    sys.exit(app.exec_())
