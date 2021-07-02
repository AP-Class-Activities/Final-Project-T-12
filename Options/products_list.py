from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Options import seller_list


class Ui_Products(object):
    def setupUi(self, Products, email):
        self.email = email
        Products.setObjectName("Products")
        Products.resize(950, 776)
        self.centralwidget = QtWidgets.QWidget(Products)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(640, 70, 271, 101))
        self.label.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.buy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.buy_btn.setGeometry(QtCore.QRect(400, 690, 151, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.buy_btn.setFont(font)
        self.buy_btn.setStyleSheet("QPushButton\n"
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
        self.buy_btn.setObjectName("buy_btn")
        self.buy_btn.clicked.connect(self.buying)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 190, 271, 101))
        self.label_2.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 310, 271, 101))
        self.label_3.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(640, 430, 271, 101))
        self.label_4.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(640, 550, 271, 101))
        self.label_5.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 70, 271, 101))
        self.label_6.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 190, 271, 101))
        self.label_7.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 310, 271, 101))
        self.label_8.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(340, 430, 271, 101))
        self.label_9.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(340, 550, 271, 101))
        self.label_10.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 70, 271, 101))
        self.label_11.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 190, 271, 101))
        self.label_12.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 310, 271, 101))
        self.label_13.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(40, 430, 271, 101))
        self.label_14.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(40, 550, 271, 101))
        self.label_15.setStyleSheet("background-color:white;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"border-radius: 30%;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.pr_mobile1 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_mobile1.setGeometry(QtCore.QRect(660, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_mobile1.setFont(font)
        self.pr_mobile1.setObjectName("pr_mobile1")
        self.pr_mobile2 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_mobile2.setGeometry(QtCore.QRect(660, 230, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_mobile2.setFont(font)
        self.pr_mobile2.setObjectName("pr_mobile2")
        self.pr_mobile3 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_mobile3.setGeometry(QtCore.QRect(660, 350, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_mobile3.setFont(font)
        self.pr_mobile3.setObjectName("pr_mobile3")
        self.pr_mobile4 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_mobile4.setGeometry(QtCore.QRect(660, 470, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_mobile4.setFont(font)
        self.pr_mobile4.setObjectName("pr_mobile4")
        self.pr_mobile5 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_mobile5.setGeometry(QtCore.QRect(660, 590, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_mobile5.setFont(font)
        self.pr_mobile5.setObjectName("pr_mobile5")
        self.pr_tablet5 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_tablet5.setGeometry(QtCore.QRect(360, 590, 111, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_tablet5.setFont(font)
        self.pr_tablet5.setObjectName("pr_tablet5")
        self.pr_tablet4 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_tablet4.setGeometry(QtCore.QRect(360, 470, 121, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_tablet4.setFont(font)
        self.pr_tablet4.setObjectName("pr_tablet4")
        self.pr_tablet3 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_tablet3.setGeometry(QtCore.QRect(360, 350, 91, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_tablet3.setFont(font)
        self.pr_tablet3.setObjectName("pr_tablet3")
        self.pr_tablet2 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_tablet2.setGeometry(QtCore.QRect(360, 230, 91, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_tablet2.setFont(font)
        self.pr_tablet2.setObjectName("pr_tablet2")
        self.pr_tablet1 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_tablet1.setGeometry(QtCore.QRect(360, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_tablet1.setFont(font)
        self.pr_tablet1.setObjectName("pr_tablet1")
        self.pr_laptop1 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_laptop1.setGeometry(QtCore.QRect(60, 110, 121, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_laptop1.setFont(font)
        self.pr_laptop1.setObjectName("pr_laptop1")
        self.pr_laptop2 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_laptop2.setGeometry(QtCore.QRect(60, 230, 141, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_laptop2.setFont(font)
        self.pr_laptop2.setObjectName("pr_laptop2")
        self.pr_laptop3 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_laptop3.setGeometry(QtCore.QRect(60, 350, 151, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_laptop3.setFont(font)
        self.pr_laptop3.setObjectName("pr_laptop3")
        self.pr_laptop4 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_laptop4.setGeometry(QtCore.QRect(60, 470, 141, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_laptop4.setFont(font)
        self.pr_laptop4.setObjectName("pr_laptop4")
        self.pr_laptop5 = QtWidgets.QRadioButton(self.centralwidget)
        self.pr_laptop5.setGeometry(QtCore.QRect(70, 590, 101, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pr_laptop5.setFont(font)
        self.pr_laptop5.setObjectName("pr_laptop5")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(150, 80, 47, 14))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(750, 80, 61, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(750, 200, 61, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(750, 320, 61, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(750, 440, 61, 16))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(750, 560, 61, 16))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(150, 200, 47, 14))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(150, 320, 47, 14))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(140, 440, 61, 16))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(150, 560, 47, 14))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(440, 320, 61, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(440, 200, 61, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(440, 80, 61, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(440, 440, 61, 16))
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(440, 560, 61, 16))
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(820, 80, 71, 81))
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap("Images/A51.png"))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(820, 200, 71, 81))
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap("Images/S20.png"))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(830, 320, 71, 81))
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("Images/note20.png"))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(820, 440, 71, 81))
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap("Images/iphone12.png"))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(820, 560, 71, 81))
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("Images/mi11.png"))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(520, 80, 71, 81))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap("Images/a7.png"))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(520, 200, 71, 81))
        self.label_37.setText("")
        self.label_37.setPixmap(QtGui.QPixmap("Images/s6lite.png"))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(520, 320, 71, 81))
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap("Images/s7.png"))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(520, 440, 71, 81))
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap("Images/ipad.png"))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(520, 560, 71, 81))
        self.label_40.setText("")
        self.label_40.setPixmap(QtGui.QPixmap("Images/m10.png"))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(200, 80, 101, 71))
        self.label_41.setText("")
        self.label_41.setPixmap(QtGui.QPixmap("Images/x543.png"))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(200, 200, 101, 71))
        self.label_42.setText("")
        self.label_42.setPixmap(QtGui.QPixmap("Images/um433.png"))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setGeometry(QtCore.QRect(200, 320, 101, 71))
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap("Images/ideapad.png"))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(200, 440, 101, 71))
        self.label_44.setText("")
        self.label_44.setPixmap(QtGui.QPixmap("Images/macbook.png"))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setGeometry(QtCore.QRect(200, 560, 101, 71))
        self.label_45.setText("")
        self.label_45.setPixmap(QtGui.QPixmap("Images/x540.png"))
        self.label_45.setObjectName("label_45")
        Products.setCentralWidget(self.centralwidget)
        self.Products = Products

        self.retranslateUi(Products)
        QtCore.QMetaObject.connectSlotsByName(Products)

    def buying(self):
        all_products = [self.pr_mobile1,self.pr_mobile2,self.pr_mobile3,self.pr_mobile4,self.pr_mobile5,self.pr_tablet1,self.pr_tablet2,self.pr_tablet3,self.pr_tablet4,self.pr_tablet5,self.pr_laptop1,self.pr_laptop2,self.pr_laptop3,self.pr_laptop4,self.pr_laptop5]
        for i in range(len(all_products)):
            if all_products[i].isChecked():
                product_name = all_products[i].text()
                self.sellerList = QtWidgets.QMainWindow()
                self.ui = seller_list.Ui_SellerList()
                self.ui.setupUi(self.sellerList,self.email, product_name)
                self.sellerList.show()
                

    def retranslateUi(self, Products):
        _translate = QtCore.QCoreApplication.translate
        Products.setWindowTitle(_translate("Products", "Products"))
        self.Products.setWindowIcon(QIcon('Images/null.png'))
        self.buy_btn.setText(_translate("Products", "خرید"))
        self.pr_mobile1.setText(_translate("Products", "Galaxy A51"))
        self.pr_mobile2.setText(_translate("Products", "Galaxy S20"))
        self.pr_mobile3.setText(_translate("Products", "Galaxy Note 20"))
        self.pr_mobile4.setText(_translate("Products", "iPhone 12 mini"))
        self.pr_mobile5.setText(_translate("Products", "Mi 11 Lite"))
        self.pr_tablet5.setText(_translate("Products", "Tab M10"))
        self.pr_tablet4.setText(_translate("Products", "iPad Mini 5"))
        self.pr_tablet3.setText(_translate("Products", "Tab S7"))
        self.pr_tablet2.setText(_translate("Products", "S6 Lite"))
        self.pr_tablet1.setText(_translate("Products", "Tab A7"))
        self.pr_laptop1.setText(_translate("Products", "X543MA"))
        self.pr_laptop2.setText(_translate("Products", "UM433DA"))
        self.pr_laptop3.setText(_translate("Products", "IdeaPad S145"))
        self.pr_laptop4.setText(_translate("Products", "MacBook Pro"))
        self.pr_laptop5.setText(_translate("Products", "X540UA"))
        self.label_16.setText(_translate("Products", "Asus"))
        self.label_17.setText(_translate("Products", "Samsung"))
        self.label_18.setText(_translate("Products", "Samsung"))
        self.label_19.setText(_translate("Products", "Samsung"))
        self.label_20.setText(_translate("Products", "Apple"))
        self.label_21.setText(_translate("Products", "Xiaomi"))
        self.label_22.setText(_translate("Products", "Asus"))
        self.label_23.setText(_translate("Products", "Lenovo"))
        self.label_24.setText(_translate("Products", "Apple"))
        self.label_25.setText(_translate("Products", "Asus"))
        self.label_26.setText(_translate("Products", "Samsung"))
        self.label_27.setText(_translate("Products", "Samsung"))
        self.label_28.setText(_translate("Products", "Samsung"))
        self.label_29.setText(_translate("Products", "Apple"))
        self.label_30.setText(_translate("Products", "Lenovo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Products = QtWidgets.QMainWindow()
    ui = Ui_Products()
    ui.setupUi(Products)
    Products.show()
    sys.exit(app.exec_())
