from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Options import admin_panel


class Ui_AdminLogin(object):
    def setupUi(self, AdminLogin):
        AdminLogin.setObjectName("AdminLogin")
        AdminLogin.resize(738, 643)
        self.centralwidget = QtWidgets.QWidget(AdminLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 90, 171, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/AdminAvatar.png"))
        self.label.setObjectName("label")
        self.admin_username = QtWidgets.QLineEdit(self.centralwidget)
        self.admin_username.setGeometry(QtCore.QRect(200, 310, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.admin_username.setFont(font)
        self.admin_username.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);")
        self.admin_username.setObjectName("admin_username")
        self.admin_password = QtWidgets.QLineEdit(self.centralwidget)
        self.admin_password.setGeometry(QtCore.QRect(200, 410, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.admin_password.setFont(font)
        self.admin_password.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);")
        self.admin_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admin_password.setObjectName("admin_password")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 310, 121, 31))
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
        self.enterAdmin = QtWidgets.QPushButton(self.centralwidget)
        self.enterAdmin.setGeometry(QtCore.QRect(330, 520, 93, 28))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        self.enterAdmin.setFont(font)
        self.enterAdmin.setStyleSheet("QPushButton\n"
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
        self.enterAdmin.setObjectName("enterAdmin")
        self.enterAdmin.clicked.connect(self.enterAsAdmin)
        self.wrong_username = QtWidgets.QLabel(self.centralwidget)
        self.wrong_username.setGeometry(QtCore.QRect(30, 310, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wrong_username.setFont(font)
        self.wrong_username.setStyleSheet("color: red;")
        self.wrong_username.setText("")
        self.wrong_username.setAlignment(QtCore.Qt.AlignCenter)
        self.wrong_username.setObjectName("wrong_username")
        self.wrong_password = QtWidgets.QLabel(self.centralwidget)
        self.wrong_password.setGeometry(QtCore.QRect(30, 410, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wrong_password.setFont(font)
        self.wrong_password.setStyleSheet("color: red;")
        self.wrong_password.setText("")
        self.wrong_password.setAlignment(QtCore.Qt.AlignCenter)
        self.wrong_password.setObjectName("wrong_password")
        AdminLogin.setCentralWidget(self.centralwidget)
        self.action = QtWidgets.QAction(AdminLogin)
        self.action.setObjectName("action")
        self.AdminLogin = AdminLogin

        self.retranslateUi(AdminLogin)
        QtCore.QMetaObject.connectSlotsByName(AdminLogin)
        
    "require datbase"
    def enterAsAdmin(self):
        if self.admin_username.text() =='admin' and self.admin_password.text() == 'admin':
            self.adminPanel = QtWidgets.QMainWindow()
            self.ui = admin_panel.Ui_AdminPanel()
            self.ui.setupUi(self.adminPanel)
            self.adminPanel.show()
            self.AdminLogin.close()
        else: 
            self.wrong_username.setText("*Wrong Username")
            self.wrong_password.setText("*Wrong Password")
        
    def retranslateUi(self, AdminLogin):
        _translate = QtCore.QCoreApplication.translate
        AdminLogin.setWindowTitle(_translate("AdminLogin", "Login as Admin"))
        self.AdminLogin.setWindowIcon(QIcon('Images/AdminIcon.png'))
        self.label_2.setText(_translate("AdminLogin", "نام کاربری:"))
        self.label_3.setText(_translate("AdminLogin", "رمز عبور:"))
        self.enterAdmin.setText(_translate("AdminLogin", "ورود"))
        self.action.setText(_translate("AdminLogin", "دت"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminLogin = QtWidgets.QMainWindow()
    ui = Ui_AdminLogin()
    ui.setupUi(AdminLogin)
    AdminLogin.show()
    sys.exit(app.exec_())
