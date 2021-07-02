from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_UserWallet(object):
    def setupUi(self, UserWallet):
        UserWallet.setObjectName("UserWallet")
        UserWallet.resize(803, 557)
        self.centralwidget = QtWidgets.QWidget(UserWallet)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 231, 51))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 30, 231, 51))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.sellers_wallet = QtWidgets.QListWidget(self.centralwidget)
        self.sellers_wallet.setGeometry(QtCore.QRect(30, 100, 321, 381))
        self.sellers_wallet.setObjectName("sellers_wallet")
        self.customers_wallet = QtWidgets.QListWidget(self.centralwidget)
        self.customers_wallet.setGeometry(QtCore.QRect(440, 100, 321, 381))
        self.customers_wallet.setObjectName("customers_wallet")
        UserWallet.setCentralWidget(self.centralwidget)
        self.UserWallet = UserWallet

         #نمایش تمام مشتری ها
        customers = open('customer_wallet.txt', 'r')
        customers = customers.readlines()
        customers = [customer.replace('\n','').split(':') for customer in customers]
        info=[]
        for i in range(len(customers)):
            info.append([customers[i][0],customers[i][1]])
        for i in info:
            item = ' : '.join(str(x) for x in i)
            self.customers_wallet.addItem(item)

        #نمایش فروشندگان
        sellers = open('seller_wallet.txt', 'r')
        sellers = sellers.readlines()
        sellers = [seller.replace('\n','').split(':') for seller in sellers]
        info=[]
        for i in range(len(sellers)):
            info.append([sellers[i][0],sellers[i][1]])
        for i in info:
            item = ' : '.join(str(x) for x in i)
            self.sellers_wallet.addItem(item)
        

        self.retranslateUi(UserWallet)
        QtCore.QMetaObject.connectSlotsByName(UserWallet)

    def retranslateUi(self, UserWallet):
        _translate = QtCore.QCoreApplication.translate
        UserWallet.setWindowTitle(_translate("UserWallet", "Users Wallet"))
        self.UserWallet.setWindowIcon(QIcon('Images/AdminIcon.png'))
        self.label.setText(_translate("UserWallet", "کیف پول فروشندگان"))
        self.label_2.setText(_translate("UserWallet", "کیف پول مشتریان"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserWallet = QtWidgets.QMainWindow()
    ui = Ui_UserWallet()
    ui.setupUi(UserWallet)
    UserWallet.show()
    sys.exit(app.exec_())
