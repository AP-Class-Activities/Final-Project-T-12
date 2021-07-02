from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Options import admin_page, users_wallet

class Ui_AdminPanel(object):
    def setupUi(self, AdminPanel):
        AdminPanel.setObjectName("AdminPanel")
        AdminPanel.resize(625, 604)
        self.centralwidget = QtWidgets.QWidget(AdminPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.add_delete = QtWidgets.QPushButton(self.centralwidget)
        self.add_delete.setGeometry(QtCore.QRect(20, 130, 581, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.add_delete.setFont(font)
        self.add_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_delete.setStyleSheet("QPushButton\n"
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
        self.add_delete.setObjectName("add_delete")
        self.add_delete.clicked.connect(self.gotoadminpage)
        self.wallet = QtWidgets.QPushButton(self.centralwidget)
        self.wallet.setGeometry(QtCore.QRect(20, 360, 581, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.wallet.setFont(font)
        self.wallet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wallet.setStyleSheet("QPushButton\n"
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
        self.wallet.setObjectName("wallet")
        self.wallet.clicked.connect(self.gotowallet)
        AdminPanel.setCentralWidget(self.centralwidget)
        self.AdminPanel = AdminPanel

        self.retranslateUi(AdminPanel)
        QtCore.QMetaObject.connectSlotsByName(AdminPanel)
    
    def gotoadminpage(self):
        self.adminPage = QtWidgets.QMainWindow()
        self.ui = admin_page.Ui_AdminPage()
        self.ui.setupUi(self.adminPage)
        self.adminPage.show()
    
    def gotowallet(self):
        self.usersWallet = QtWidgets.QMainWindow()
        self.ui = users_wallet.Ui_UserWallet()
        self.ui.setupUi(self.usersWallet)
        self.usersWallet.show()

    def retranslateUi(self, AdminPanel):
        _translate = QtCore.QCoreApplication.translate
        AdminPanel.setWindowTitle(_translate("AdminPanel", "Admin Panel"))
        self.AdminPanel.setWindowIcon(QIcon('Images/AdminIcon.png'))
        self.add_delete.setText(_translate("AdminPanel", "مشاهده لیست و حذف و اضفه کردن مشتریان و فروشندگان"))
        self.wallet.setText(_translate("AdminPanel", "مشاهده کیف پول مشتریان و فروشندگان"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminPanel = QtWidgets.QMainWindow()
    ui = Ui_AdminPanel()
    ui.setupUi(AdminPanel)
    AdminPanel.show()
    sys.exit(app.exec_())
