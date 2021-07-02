from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_AddProduct(object):
    def setupUi(self, AddProduct, email):
        self.email = email
        AddProduct.setObjectName("AddProduct")
        AddProduct.resize(568, 600)
        self.centralwidget = QtWidgets.QWidget(AddProduct)
        self.centralwidget.setObjectName("centralwidget")
        self.product_list = QtWidgets.QListWidget(self.centralwidget)
        self.product_list.setGeometry(QtCore.QRect(130, 50, 281, 371))
        self.product_list.setObjectName("product_list")
        self.price = QtWidgets.QLineEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(130, 460, 281, 21))
        self.price.setStyleSheet("border-radius:10%;\n"
"border: 2px solid rgb(61, 135, 255);")
        self.price.setObjectName("price")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 450, 61, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(61, 135, 255);\n"
"font-family:B Nazanin, Arial;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.add_product = QtWidgets.QPushButton(self.centralwidget)
        self.add_product.setGeometry(QtCore.QRect(230, 520, 93, 28))
        self.add_product.setStyleSheet("QPushButton\n"
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
        self.add_product.setObjectName("add_product")
        self.add_product.clicked.connect(self.addproduct)
        AddProduct.setCentralWidget(self.centralwidget)
        self.AddProduct= AddProduct

        products = open('products.txt', 'r')
        products = products.readlines()
        #products = [customer.replace(' ','') for customer in products]
        products = [customer.replace('\n','').split(',') for customer in products]

        info=[]
        for i in range(len(products)):
            if products[i][0] not in info:
                info.append([products[i][0]])
        for i in info:
            item = ''.join(str(x) for x in i)
            self.product_list.addItem(item)

        self.retranslateUi(AddProduct)
        QtCore.QMetaObject.connectSlotsByName(AddProduct)

    def addproduct(self):
        price = self.price.text()
        item = self.product_list.currentItem()
        p_name = item.text()
        new_product=[p_name,self.email,price]
        new_product_str = ', '.join(new_product)
        #print(txt)
        with open('products.txt','a') as productsadd:
            productsadd.write('\n'+new_product_str)

    def retranslateUi(self, AddProduct):
        _translate = QtCore.QCoreApplication.translate
        AddProduct.setWindowTitle(_translate("AddProduct", "MainWindow"))
        self.AddProduct.setWindowIcon(QIcon('Images/null.png'))
        self.label.setText(_translate("AddProduct", "مبلغ:"))
        self.add_product.setText(_translate("AddProduct", "اضافه کردن"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddProduct = QtWidgets.QMainWindow()
    ui = Ui_AddProduct()
    ui.setupUi(AddProduct)
    AddProduct.show()
    sys.exit(app.exec_())
