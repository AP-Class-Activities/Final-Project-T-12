from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Options import seller_add_product

class Ui_SellerLogin(object):
    def setupUi(self, SellerLogin):
        SellerLogin.setObjectName("SellerLogin")
        SellerLogin.resize(738, 643)
        self.centralwidget = QtWidgets.QWidget(SellerLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 90, 171, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/LoginAvatar.png"))
        self.label.setObjectName("label")
        self.seller_email = QtWidgets.QLineEdit(self.centralwidget)
        self.seller_email.setGeometry(QtCore.QRect(200, 310, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.seller_email.setFont(font)
        self.seller_email.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);")
        self.seller_email.setObjectName("seller_email")
        self.seller_password = QtWidgets.QLineEdit(self.centralwidget)
        self.seller_password.setGeometry(QtCore.QRect(200, 410, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.seller_password.setFont(font)
        self.seller_password.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);")
        self.seller_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.seller_password.setObjectName("seller_password")
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
        self.enterSeller = QtWidgets.QPushButton(self.centralwidget)
        self.enterSeller.setGeometry(QtCore.QRect(330, 520, 93, 28))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        self.enterSeller.setFont(font)
        self.enterSeller.setStyleSheet("QPushButton\n"
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
        self.enterSeller.setObjectName("enterSeller")
        self.enterSeller.clicked.connect(self.enterAsSeller)
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
        SellerLogin.setCentralWidget(self.centralwidget)
        self.action = QtWidgets.QAction(SellerLogin)
        self.action.setObjectName("action")
        self.SellerLogin = SellerLogin

        self.retranslateUi(SellerLogin)
        QtCore.QMetaObject.connectSlotsByName(SellerLogin)

    "require database"
    def enterAsSeller(self):
        email = self.seller_email.text()
        password = self.seller_password.text()
        sellers = open('seller_data.txt','r')
        sellers = sellers.readlines()
        for i in sellers:
            if i == 'ï»؟\n':
                sellers.remove('ï»؟\n')
        sellers = [seller.replace(' ','') for seller in sellers]
        sellers = [seller.replace('\n','').split(',') for seller in sellers]
        for i in range(len(sellers)):
            if email == sellers[i][2] and password == sellers[i][4]:
                self.addProduct = QtWidgets.QMainWindow()
                self.ui = seller_add_product.Ui_AddProduct()
                self.ui.setupUi(self.addProduct, email)
                self.addProduct.show()
                self.SellerLogin.close()
            else:
                self.wrong_email.setText("*Wrong email")
                self.wrong_password.setText("*Wrong password")
        #print('enter seller')

    def retranslateUi(self, SellerLogin):
        _translate = QtCore.QCoreApplication.translate
        SellerLogin.setWindowTitle(_translate("SellerLogin", "Login as Seller"))
        self.SellerLogin.setWindowIcon(QIcon('Images/null.png'))
        self.label_2.setText(_translate("SellerLogin", "ایمیل:"))
        self.label_3.setText(_translate("SellerLogin", "رمز عبور:"))
        self.enterSeller.setText(_translate("SellerLogin", "ورود"))
        self.action.setText(_translate("SellerLogin", "دت"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SellerLogin = QtWidgets.QMainWindow()
    ui = Ui_SellerLogin()
    ui.setupUi(SellerLogin)
    SellerLogin.show()
    sys.exit(app.exec_())
