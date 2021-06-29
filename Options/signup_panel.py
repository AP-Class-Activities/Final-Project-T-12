from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_SignupPanel(object):
    def setupUi(self, SignupPanel):
        SignupPanel.setObjectName("SignupPanel")
        SignupPanel.resize(800, 643)
        self.centralwidget = QtWidgets.QWidget(SignupPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.Customeradd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Customeradd_btn.setGeometry(QtCore.QRect(230, 250, 331, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.Customeradd_btn.setFont(font)
        self.Customeradd_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Customeradd_btn.setStyleSheet("QPushButton\n"
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
        self.Customeradd_btn.setObjectName("Customeradd_btn")
        self.Customeradd_btn.clicked.connect(self.gotocustomersignup)
        self.selleradd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.selleradd_btn.setGeometry(QtCore.QRect(230, 410, 331, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.selleradd_btn.setFont(font)
        self.selleradd_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selleradd_btn.setStyleSheet("QPushButton\n"
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
        self.selleradd_btn.setObjectName("selleradd_btn")
        self.selleradd_btn.clicked.connect(self.gotosellersignup)
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
        SignupPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignupPanel)
        QtCore.QMetaObject.connectSlotsByName(SignupPanel)
        self.SignupPanel = SignupPanel

    def gotocustomersignup(self):
        pass

    def gotosellersignup(self):
        pass

    def retranslateUi(self, SignupPanel):
        _translate = QtCore.QCoreApplication.translate
        SignupPanel.setWindowTitle(_translate("SignupPanel", "Sign Up"))
        SignupPanel.setWindowIcon(QIcon('Images/null.png'))
        self.Customeradd_btn.setText(_translate("SignupPanel", "مشتری"))
        self.selleradd_btn.setText(_translate("SignupPanel", "فروشنده"))
        self.label.setText(_translate("SignupPanel", "به آنلاین شاپ خوش آمدید\n"
"شیوه ثبت نام را انتخاب کنید"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignupPanel = QtWidgets.QMainWindow()
    ui = Ui_SignupPanel()
    ui.setupUi(SignupPanel)
    SignupPanel.show()
    sys.exit(app.exec_())
