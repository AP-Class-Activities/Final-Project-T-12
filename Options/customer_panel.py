from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Options import add_money, products_list


class Ui_CustomerPanel(object):
    def setupUi(self, CustomerPanel, email):
        self.email = email
        CustomerPanel.setObjectName("CustomerPanel")
        CustomerPanel.resize(648, 578)
        self.centralwidget = QtWidgets.QWidget(CustomerPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.buy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.buy_btn.setGeometry(QtCore.QRect(150, 140, 331, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.buy_btn.setFont(font)
        self.buy_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buy_btn.setStyleSheet("QPushButton\n"
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
        self.buy_btn.setObjectName("buy_btn")
        self.buy_btn.clicked.connect(self.gotobuy)
        self.addMoney_btn = QtWidgets.QPushButton(self.centralwidget)
        self.addMoney_btn.setGeometry(QtCore.QRect(150, 340, 331, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.addMoney_btn.setFont(font)
        self.addMoney_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addMoney_btn.setStyleSheet("QPushButton\n"
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
        self.addMoney_btn.setObjectName("addMoney_btn")
        self.addMoney_btn.clicked.connect(self.gotoaddmoney)
        CustomerPanel.setCentralWidget(self.centralwidget)
        self.CustomerPanel = CustomerPanel

        self.retranslateUi(CustomerPanel)
        QtCore.QMetaObject.connectSlotsByName(CustomerPanel)

    def gotobuy(self):
        self.buy = QtWidgets.QMainWindow()
        self.ui = products_list.Ui_Products()
        self.ui.setupUi(self.buy, self.email)
        self.buy.show()

    def gotoaddmoney(self):
        self.addmoney = QtWidgets.QMainWindow()
        self.ui = add_money.Ui_AddMoney()
        self.ui.setupUi(self.addmoney, self.email)
        self.addmoney.show()

    def retranslateUi(self, CustomerPanel):
        _translate = QtCore.QCoreApplication.translate
        CustomerPanel.setWindowTitle(_translate("CustomerPanel", "Customer Panel"))
        self.CustomerPanel.setWindowIcon(QIcon('Images/null.png'))
        self.buy_btn.setText(_translate("CustomerPanel", "خرید"))
        self.addMoney_btn.setText(_translate("CustomerPanel", "شارژ اکانت"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CustomerPanel = QtWidgets.QMainWindow()
    ui = Ui_CustomerPanel()
    ui.setupUi(CustomerPanel)
    CustomerPanel.show()
    sys.exit(app.exec_())
