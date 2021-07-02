from PyQt5 import QtCore, QtGui, QtWidgets
from Options import customer_signup, seller_signup
from PyQt5.QtGui import QIcon


class Ui_AdminPage(object):
    def setupUi(self, AdminPage):
        AdminPage.setObjectName("AdminPage")
        AdminPage.resize(803, 645)
        self.centralwidget = QtWidgets.QWidget(AdminPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 201, 51))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 30, 181, 51))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.sellers_list = QtWidgets.QListWidget(self.centralwidget)
        self.sellers_list.setGeometry(QtCore.QRect(30, 100, 321, 381))
        self.sellers_list.setObjectName("sellers_list")
        self.customers_list = QtWidgets.QListWidget(self.centralwidget)
        self.customers_list.setGeometry(QtCore.QRect(440, 100, 321, 381))
        self.customers_list.setObjectName("customers_list")
        self.delete_customer = QtWidgets.QPushButton(self.centralwidget)
        self.delete_customer.setGeometry(QtCore.QRect(470, 580, 121, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(11)
        self.delete_customer.setFont(font)
        self.delete_customer.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"background-color: rgb(208, 0, 0);\n"
"border-radius:20%;\n"
"border: 2px solid rgb(208, 0, 0);\n"
"font-family:B Nazanin, Arial\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color:white;\n"
"background-color:rgb(103, 0, 0);\n"
"border-radius:20%;\n"
"border: 2px solid rgb(103, 0, 0);\n"
"font-family:B Nazanin, Arial\n"
"}")
        self.delete_customer.setObjectName("delete_customer")
        self.delete_customer.clicked.connect(self.delcustomer)
        self.delete_seller = QtWidgets.QPushButton(self.centralwidget)
        self.delete_seller.setGeometry(QtCore.QRect(60, 580, 121, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(11)
        self.delete_seller.setFont(font)
        self.delete_seller.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"background-color: rgb(208, 0, 0);\n"
"border-radius:20%;\n"
"border: 2px solid rgb(208, 0, 0);\n"
"font-family:B Nazanin, Arial\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color:white;\n"
"background-color:rgb(103, 0, 0);\n"
"border-radius:20%;\n"
"border: 2px solid rgb(103, 0, 0);\n"
"font-family:B Nazanin, Arial\n"
"}")
        self.delete_seller.setObjectName("delete_seller")
        self.delete_seller.clicked.connect(self.delseller)
        self.add_customer = QtWidgets.QPushButton(self.centralwidget)
        self.add_customer.setGeometry(QtCore.QRect(610, 580, 121, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(11)
        self.add_customer.setFont(font)
        self.add_customer.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"background-color: rgb(32, 149, 0);\n"
"border-radius:20%;\n"
"border: 2px solid rgb(32, 149, 0);\n"
"font-family:B Nazanin, Arial;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color:white;\n"
"background-color:rgb(0, 89, 3);\n"
"border-radius:20%;\n"
"border: 2px solid rgb(0, 89, 3);\n"
"font-family:B Nazanin, Arial;\n"
"}")
        self.add_customer.setObjectName("add_customer")
        self.add_customer.clicked.connect(self.addCustomer)
        self.add_seller = QtWidgets.QPushButton(self.centralwidget)
        self.add_seller.setGeometry(QtCore.QRect(200, 580, 121, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(11)
        self.add_seller.setFont(font)
        self.add_seller.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"background-color: rgb(32, 149, 0);\n"
"border-radius:20%;\n"
"border: 2px solid rgb(32, 149, 0);\n"
"font-family:B Nazanin, Arial;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color:white;\n"
"background-color:rgb(0, 89, 3);\n"
"border-radius:20%;\n"
"border: 2px solid rgb(0, 89, 3);\n"
"font-family:B Nazanin, Arial;\n"
"}")
        self.add_seller.setObjectName("add_seller")
        self.add_seller.clicked.connect(self.addSeller)
        self.customer_deleted = QtWidgets.QLabel(self.centralwidget)
        self.customer_deleted.setGeometry(QtCore.QRect(500, 500, 201, 51))
        font = QtGui.QFont()
        font.setFamily("B nazanin")
        font.setPointSize(18)
        self.customer_deleted.setFont(font)
        self.customer_deleted.setStyleSheet("color:red;\n"
"font-family:B nazanin, Arial;")
        self.customer_deleted.setText("")
        self.customer_deleted.setAlignment(QtCore.Qt.AlignCenter)
        self.customer_deleted.setObjectName("customer_deleted")
        self.seller_deleted = QtWidgets.QLabel(self.centralwidget)
        self.seller_deleted.setGeometry(QtCore.QRect(70, 500, 221, 51))
        font = QtGui.QFont()
        font.setFamily("B nazanin")
        font.setPointSize(18)
        self.seller_deleted.setFont(font)
        self.seller_deleted.setStyleSheet("color:red;\n"
"font-family:B nazanin, Arial;")
        self.seller_deleted.setText("")
        self.seller_deleted.setAlignment(QtCore.Qt.AlignCenter)
        self.seller_deleted.setObjectName("seller_deleted")
        AdminPage.setCentralWidget(self.centralwidget)
        self.AdminPage = AdminPage

        "require database"
        #نمایش تمام مشتری ها
        customers = open('customer_data.txt', 'r')
        customers = customers.readlines()
        for i in customers:
            if i == 'ï»؟\n':
                customers.remove('ï»؟\n')
        customers = [customer.replace(' ','') for customer in customers]
        customers = [customer.replace('\n','').split(',') for customer in customers]

        info=[]
        for i in range(len(customers)):
            if customers[i][2] not in info and customers[i][4] not in info:
                info.append([customers[i][2],customers[i][4],customers[i][7]])
        for i in info:
            item = ' - '.join(str(x) for x in i)
            self.customers_list.addItem(item)
        #نمیش تمام فروشندگان
        sellers = open('seller_data.txt', 'r')
        sellers = sellers.readlines()
        for i in sellers:
            if i == 'ï»؟\n':
                sellers.remove('ï»؟\n')
        sellers = [seller.replace(' ','') for seller in sellers]
        sellers = [seller.replace('\n','').split(',') for seller in sellers]
        #print(sellers)
        info=[]
        for i in range(len(sellers)):
            if sellers[i][2] not in info and sellers[i][4] not in info:
                info.append([sellers[i][2],sellers[i][4],sellers[i][5]])
        for i in info:
            item = ' - '.join(str(x) for x in i)
            self.sellers_list.addItem(item)

        self.retranslateUi(AdminPage)
        QtCore.QMetaObject.connectSlotsByName(AdminPage)

    def delcustomer(self):
        item = self.customers_list.currentItem()
        txt = item.text()
        listed = txt.split(" - ")
        #print(listed)
        with open('customer_data.txt','r') as file:
            lines = file.readlines()
            for i in lines:
                if i == 'ï»؟\n':
                    lines.remove('ï»؟\n')
            lines = [line.replace('\n','').split(',') for line in lines]
            lines2 = lines
            #print(lines)
            for i in range(len(lines)):
                lines[i][2] = lines[i][2].replace(' ','')
                if listed[0] == lines[i][2]:
                    lines2 = [lines[i] for i in range(len(lines)) if lines[i][2] != listed[0]]
                    fileW = open('customer_data.txt','a')
                    fileW.truncate(0)
                    for i in range(len(lines2)):
                        fileW.write('\n'+','.join(lines2[i]))
                    fileW.close()
        with open('customer_wallet.txt','r') as cwfile:
            lines = cwfile.readlines()
            lines = [line.replace('\n','').split(':') for line in lines]
            lines2 = lines
            #print(lines)
            for i in range(len(lines)):
                if listed[0] == lines[i][0]:
                    lines2 = [lines[i] for i in range(len(lines)) if lines[i][0] != listed[0]]
                    cwfileW = open('customer_wallet.txt','a')
                    cwfileW.truncate(0)
                    for i in range(len(lines2)):
                        cwfileW.write(':'.join(lines2[i])+'\n')
                    cwfileW.close()
        self.customer_deleted.setText('مشتری حذف شد')
    def delseller(self):
        item = self.sellers_list.currentItem()
        txt = item.text()
        listed = txt.split(" - ")
        #print(listed)
        listed[0] = listed[0].replace(' ', '')
        #print(listed[0])
        with open('seller_data.txt','r') as file:
            lines = file.readlines()
            for i in lines:
                if i == 'ï»؟\n':
                    lines.remove('ï»؟\n')
            lines = [line.replace('\n','').split(',') for line in lines]
            lines2 = lines
            #print(lines)
            for i in range(len(lines)):
                lines[i][2] = lines[i][2].replace(' ','')
                if listed[0] == lines[i][2]:
                    lines2 = [lines[i] for i in range(len(lines)) if lines[i][2] != listed[0]]
                    file = open('seller_data.txt','a')
                    file.truncate(0)
                    for i in range(len(lines2)):
                        file.write(','.join(lines2[i]))
                        self.seller_deleted.setText('فروشنده حذف شد')

    def addCustomer(self):
        self.customerSignup = QtWidgets.QMainWindow()
        self.ui = customer_signup.Ui_CustomerSignup()
        self.ui.setupUi(self.customerSignup)
        self.customerSignup.show()

    def addSeller(self):
        self.sellerSignup = QtWidgets.QMainWindow()
        self.ui = seller_signup.Ui_SellerSignup()
        self.ui.setupUi(self.sellerSignup)
        self.sellerSignup.show()

    def retranslateUi(self, AdminPage):
        _translate = QtCore.QCoreApplication.translate
        AdminPage.setWindowTitle(_translate("AdminPage", "Admin"))
        self.AdminPage.setWindowIcon(QIcon('Images/AdminIcon.png'))
        self.label.setText(_translate("AdminPage", "لیست فروشندگان"))
        self.label_2.setText(_translate("AdminPage", "لیست مشتریان"))
        self.delete_customer.setText(_translate("AdminPage", "حذف مشتری"))
        self.delete_seller.setText(_translate("AdminPage", "حذف فروشنده"))
        self.add_customer.setText(_translate("AdminPage", "اضافه کردن مشتری"))
        self.add_seller.setText(_translate("AdminPage", "اضافه کردن فروشنده"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminPage = QtWidgets.QMainWindow()
    ui = Ui_AdminPage()
    ui.setupUi(AdminPage)
    AdminPage.show()
    sys.exit(app.exec_())
