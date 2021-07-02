from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Options import signup_panel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 606)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.about_btn = QtWidgets.QPushButton(self.centralwidget)
        self.about_btn.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.about_btn.setFont(font)
        self.about_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about_btn.setStyleSheet("QPushButton\n"
"{\n"
"color:rgb(0, 60, 255);\n"
"background-color:white;\n"
"border-radius:10%;\n"
"border: 1px solid rgb(0, 60, 255);\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color: white;\n"
"background-color: rgb(0, 60, 255);\n"
"border-radius:10%;\n"
"}")
        self.about_btn.setObjectName("about_btn")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(40, 180, 221, 51))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(16)
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setStyleSheet("QPushButton\n"
"{\n"
"color: rgb(61, 135, 255);\n"
"background-color:white;\n"
"border-radius:20%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color: white;\n"
"background-color: rgb(61, 135, 255);\n"
"border-radius:20%;\n"
"font-family: B Nazanin, Arial\n"
"}")
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.gotologin)
        self.signup_btn = QtWidgets.QPushButton(self.centralwidget)
        self.signup_btn.setGeometry(QtCore.QRect(40, 290, 221, 51))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(16)
        self.signup_btn.setFont(font)
        self.signup_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signup_btn.setStyleSheet("QPushButton\n"
"{\n"
"color: rgb(61, 135, 255);\n"
"background-color:white;\n"
"border-radius:20%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color: white;\n"
"background-color: rgb(61, 135, 255);\n"
"border-radius:20%;\n"
"font-family: B Nazanin, Arial\n"
"}")
        self.signup_btn.setObjectName("signup_btn")
        self.signup_btn.clicked.connect(self.gotosignup)
        self.signup_btn.clicked.connect(self.gotosignup)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(40, 400, 221, 51))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(16)
        self.exit_btn.setFont(font)
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_btn.setStyleSheet("QPushButton\n"
"{\n"
"color: rgb(61, 135, 255);\n"
"background-color:white;\n"
"border-radius:20%;\n"
"border: 2px solid rgb(61, 135, 255);\n"
"font-family: B Nazanin, Arial\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"color: white;\n"
"background-color: rgb(61, 135, 255);\n"
"border-radius:20%;\n"
"font-family: B Nazanin, Arial\n"
"}")
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(self.exit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 90, 501, 431))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/Main.png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 785, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def gotologin(self):
        self.loginPanel = QtWidgets.QMainWindow()
        self.ui = login_panel.Ui_LoginPanel()
        self.ui.setupUi(self.loginPanel)
        self.loginPanel.show()
        MainWindow.close()

    def gotosignup(self):
        self.signupPanel = QtWidgets.QMainWindow()
        self.ui = signup_panel.Ui_SignupPanel()
        self.ui.setupUi(self.signupPanel)
        self.signupPanel.show()

    def exit(self):
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Online Shop"))
        MainWindow.setWindowIcon(QIcon('Images/null.png'))
        self.about_btn.setText(_translate("MainWindow", "About Us"))
        self.login_btn.setText(_translate("MainWindow", "ورود"))
        self.signup_btn.setText(_translate("MainWindow", "ثبت نام"))
        self.exit_btn.setText(_translate("MainWindow", "خروج"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
