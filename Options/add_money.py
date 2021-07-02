from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_AddMoney(object):
    def setupUi(self, AddMoney, email):
        self.email = email
        self.amtcheck = False
        AddMoney.setObjectName("AddMoney")
        AddMoney.resize(649, 600)
        self.centralwidget = QtWidgets.QWidget(AddMoney)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 70, 291, 91))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.amount = QtWidgets.QLineEdit(self.centralwidget)
        self.amount.setGeometry(QtCore.QRect(70, 250, 521, 61))
        self.amount.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.amount.setObjectName("amount")
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        self.amount.setFont(font)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 500, 171, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.checkAmount)
        self.pushButton.clicked.connect(self.addMoney)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 340, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:red;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        AddMoney.setCentralWidget(self.centralwidget)
        self.AddMoney = AddMoney

        self.retranslateUi(AddMoney)
        QtCore.QMetaObject.connectSlotsByName(AddMoney)

    def checkAmount(self):
        amount = self.amount.text()
        if int(amount) > 0:
            self.amtcheck = True
        else:
            self.label_2.setText('*Invalid')

    def addMoney(self):
        newline = []
        if self.amtcheck == True:
            amount = self.amount.text()
            with open('customer_wallet.txt','r') as file:
                cWallet = file.readlines()
                cWallet = [customer.replace('\n','').split(':') for customer in cWallet]
                cWallet2 = cWallet
                for i in range(len(cWallet)):
                    if self.email == cWallet[i][0]:
                        money = cWallet[i][1]
                        amount = int(amount) + int(money)
                        newline.append(cWallet[i][0]+':'+str(amount))
                        cWallet2 = [cWallet[i] for i in range(len(cWallet)) if cWallet[i][0] != self.email]
                        file = open('customer_wallet.txt','a')
                        file.truncate(0)
                        newline = "".join(str(x) for x in newline[0])
                        file.write(newline)
                        for i in range(len(cWallet2)):
                            file.write('\n'+':'.join(cWallet2[i]))
                            self.AddMoney.close()

    def retranslateUi(self, AddMoney):
        _translate = QtCore.QCoreApplication.translate
        AddMoney.setWindowTitle(_translate("AddMoney", "Add Money"))
        self.AddMoney.setWindowIcon(QIcon('Images/null.png'))
        self.label.setText(_translate("AddMoney", "مبلغ را وارد کنید"))
        self.pushButton.setText(_translate("AddMoney", "تایید"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddMoney = QtWidgets.QMainWindow()
    ui = Ui_AddMoney()
    ui.setupUi(AddMoney)
    AddMoney.show()
    sys.exit(app.exec_())
