from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_SellerList(object):
    def setupUi(self, SellerList,email,product_name):
        self.email = email
        self.product_name = product_name
        SellerList.setObjectName("SellerList")
        SellerList.resize(490, 708)
        self.centralwidget = QtWidgets.QWidget(SellerList)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 391, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.sellers_list = QtWidgets.QListWidget(self.centralwidget)
        self.sellers_list.setGeometry(QtCore.QRect(55, 100, 381, 471))
        self.sellers_list.setObjectName("sellers_list")
        self.confirm = QtWidgets.QPushButton(self.centralwidget)
        self.confirm.setGeometry(QtCore.QRect(160, 630, 171, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.confirm.setFont(font)
        self.confirm.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"background-color: rgb(0, 161, 5);\n"
"border-radius:30%;\n"
"border: 2px solid rgb(0, 161, 5);\n"
"font-family:B Nazanin, Arial\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color:rgb(0, 161, 5);\n"
"background-color:white;\n"
"border-radius:30%;\n"
"border: 2px solid rgb(0, 161, 5);\n"
"font-family:B Nazanin, Arial\n"
"}")
        self.confirm.setObjectName("confirm")
        self.confirm.clicked.connect(self.buyproduct)
        self.not_enough = QtWidgets.QLabel(self.centralwidget)
        self.not_enough.setGeometry(QtCore.QRect(140, 590, 211, 21))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        self.not_enough.setFont(font)
        self.not_enough.setStyleSheet("color: red;\n"
"font-family: B Nazanin, Arial;")
        self.not_enough.setText("")
        self.not_enough.setAlignment(QtCore.Qt.AlignCenter)
        self.not_enough.setObjectName("not_enough")
        SellerList.setCentralWidget(self.centralwidget)
        self.SellerList = SellerList

        products = open('products.txt','r')
        products = products.readlines()
        #print(products)
        #products = [product.replace(' ','') for product in products]
        products = [product.replace('\n','').split(', ') for product in products]
        #print(products)
        seller_list = []
        for i in range(len(products)):
            if products[i][0] == self.product_name:
                seller_list.append([products[i][0],products[i][1],products[i][2]])
        for i in seller_list:
            item = ' - '.join(str(x) for x in i)
            self.sellers_list.addItem(item)

        self.retranslateUi(SellerList)
        QtCore.QMetaObject.connectSlotsByName(SellerList)

    def buyproduct(self):
        item = self.sellers_list.currentItem()
        txt = item.text()
        listed = txt.split(' - ')
        listed2 = listed
        #print(listed)
        customer_money = 0
        seller_money = 0
        new_info_seller = []
        new_info_customer = []
        with open('customer_wallet.txt','r') as cwallet:
            lines = cwallet.readlines()
            lines = [line.replace(' ','') for line in lines]
            lines = [line.replace('\n','').split(':') for line in lines]
            lines2 = lines
            for i in range(len(lines)):
                if lines[i][0] == self.email:
                    if int(lines[i][1]) >= int(listed[2]):
                        customer_money = int(lines[i][1])-int(listed[2])
                        eMail = lines[i][0]
                        new_info_customer.append([eMail, customer_money])
                        #lines[i].pop()
                        #lines[i].append(deposite)
                        lines2 = [lines[i] for i in range(len(lines)) if lines[i][0] != self.email]
                        cWallet = open('customer_wallet.txt','a')
                        cWallet.truncate(0)
                        new_info_customer_str = ":".join(str(x) for x in new_info_customer[0])
                        cWallet.write(new_info_customer_str+'\n')
                        for i in range(len(lines2)):
                            cWallet.write(':'.join(str(x) for x in lines2[i])+'\n')
                            #cWallet.close()
                            with open('seller_wallet.txt','r') as swallet:
                                slines = swallet.readlines()
                                slines = [sline.replace(' ','') for sline in slines]
                                slines = [sline.replace('\n','').split(':') for sline in slines]
                                slines2 = slines
                                for j in range(len(slines)):
                                    if slines[j][0] == listed[1]:
                                        seller_money = int(slines[j][1])+int(listed[2])
                                        seMail = slines[j][0]
                                        new_info_seller.append([seMail,seller_money])
                                        slines2 = [slines[i] for i in range(len(slines)) if slines[i][0] != listed[1]]
                                        new_info_seller_str = ":".join(str(x) for x in new_info_seller[0])
                                        #print(slines)
                                        #print(slines2)
                                        #print(new_info_seller)
                                        #print(new_info_customer)
                                        sWallet = open('seller_wallet.txt','a')
                                        sWallet.truncate(0)
                                        sWallet.write(new_info_seller_str+'\n')
                                        for k in range(len(slines2)):
                                            sWallet.write(':'.join(slines2[k])+'\n')
                                        sWallet.close()
                                        self.SellerList.close()
                    else:
                        self.not_enough.setText('موجودی کافی نیست')


    def retranslateUi(self, SellerList):
        _translate = QtCore.QCoreApplication.translate
        SellerList.setWindowTitle(_translate("SellerList", "Sellers"))
        self.SellerList.setWindowIcon(QIcon('Images/null.png'))
        self.label.setText(_translate("SellerList", "فروشندگان این محصول"))
        self.confirm.setText(_translate("SellerList", "تایید"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SellerList = QtWidgets.QMainWindow()
    ui = Ui_SellerList()
    ui.setupUi(SellerList)
    SellerList.show()
    sys.exit(app.exec_())
