from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Options import customer_login, seller_login, admin_login

class Ui_LoginPanel(object):
    def setupUi(self, LoginPanel):
        LoginPanel.setObjectName("LoginPanel")
        LoginPanel.resize(800, 643)
        self.centralwidget = QtWidgets.QWidget(LoginPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.Customer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Customer_btn.setGeometry(QtCore.QRect(230, 240, 331, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.Customer_btn.setFont(font)
        self.Customer_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Customer_btn.setStyleSheet("QPushButton\n"
"{\n"
"color:rgb(61, 135, 255);\n"
"background-color:white;\n"
"border-radius:20%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family:B Nazanin, Arial\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color:white;\n"
"background-color: rgb(61, 135, 255);\n"
"border-radius:20%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family:B Nazanin, Arial\n"
"}")
        self.Customer_btn.setObjectName("Customer_btn")
        self.Customer_btn.clicked.connect(self.gotocustomerlogin)
        self.seller_btn = QtWidgets.QPushButton(self.centralwidget)
        self.seller_btn.setGeometry(QtCore.QRect(230, 360, 331, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.seller_btn.setFont(font)
        self.seller_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seller_btn.setStyleSheet("QPushButton\n"
"{\n"
"color:rgb(61, 135, 255);\n"
"background-color:white;\n"
"border-radius:20%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family:B Nazanin, Arial\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color:white;\n"
"background-color: rgb(61, 135, 255);\n"
"border-radius:20%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family:B Nazanin, Arial\n"
"}")
        self.seller_btn.setObjectName("seller_btn")
        self.seller_btn.clicked.connect(self.gotosellerlogin)
        self.operator_btn = QtWidgets.QPushButton(self.centralwidget)
        self.operator_btn.setGeometry(QtCore.QRect(230, 480, 331, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.operator_btn.setFont(font)
        self.operator_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.operator_btn.setStyleSheet("QPushButton\n"
"{\n"
"color:rgb(61, 135, 255);\n"
"background-color:white;\n"
"border-radius:20%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family:B Nazanin, Arial\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color:white;\n"
"background-color: rgb(61, 135, 255);\n"
"border-radius:20%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family:B Nazanin, Arial\n"
"}")
        self.operator_btn.setObjectName("operator_btn")
        self.operator_btn.clicked.connect(self.gotoadminlogin)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 731, 151))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(61, 135, 255);\n"
"font-family:B Titr, Arial")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        LoginPanel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginPanel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        LoginPanel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginPanel)
        self.statusbar.setObjectName("statusbar")
        LoginPanel.setStatusBar(self.statusbar)
        self.LoginPanel = LoginPanel

        self.retranslateUi(LoginPanel)
        QtCore.QMetaObject.connectSlotsByName(LoginPanel)

    def gotocustomerlogin(self):
        self.customerLogin = QtWidgets.QMainWindow()
        self.ui = customer_login.Ui_CustomerLogin()
        self.ui.setupUi(self.customerLogin)
        self.customerLogin.show()
        self.LoginPanel.close()

    def gotosellerlogin(self):
        self.sellerLogin = QtWidgets.QMainWindow()
        self.ui = seller_login.Ui_SellerLogin()
        self.ui.setupUi(self.sellerLogin)
        self.sellerLogin.show()
        self.LoginPanel.close()
    
    def gotoadminlogin(self):
        self.adminLogin = QtWidgets.QMainWindow()
        self.ui = admin_login.Ui_AdminLogin()
        self.ui.setupUi(self.adminLogin)
        self.adminLogin.show()
        self.LoginPanel.close()

    def retranslateUi(self, LoginPanel):
        _translate = QtCore.QCoreApplication.translate
        LoginPanel.setWindowTitle(_translate("LoginPanel", "Login Panels"))
        LoginPanel.setWindowIcon(QIcon('Images/null.png'))
        self.Customer_btn.setText(_translate("LoginPanel", "پنل مشتری"))
        self.seller_btn.setText(_translate("LoginPanel", "پنل فروشنده"))
        self.operator_btn.setText(_translate("LoginPanel", "پنل مدیریت"))
        self.label.setText(_translate("LoginPanel", "به آنلاین شاپ خوش آمدید\n"
"برای ورود بر روی یکی از پنل های زیر کلیک کنید"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPanel = QtWidgets.QMainWindow()
    ui = Ui_LoginPanel()
    ui.setupUi(LoginPanel)
    LoginPanel.show()
    sys.exit(app.exec_())
