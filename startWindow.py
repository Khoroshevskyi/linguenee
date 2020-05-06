from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import passCreator, register, userWindow
import sys
from progData import *

class Ui_startWindow(object):
    def setupUi(self, startWindow):
        self.startWindow = startWindow
        self.startWindow.setObjectName("startWindow")
        self.startWindow.setEnabled(True)
        self.startWindow.resize(600, 360)

        self.startWindow.setMinimumSize(QtCore.QSize(600, 360))
        self.startWindow.setMaximumSize(QtCore.QSize(600, 360))

        # name = lenguenee
        self.nameLabel = QtWidgets.QLabel(startWindow)
        self.nameLabel.setGeometry(QtCore.QRect(190, 0, 220, 91))
        font = QtGui.QFont()
        font.setFamily(LOGOSTILE)
        font.setPointSize(36)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")

        # info = ...
        self.infoLabel = QtWidgets.QLabel(startWindow)
        self.infoLabel.setEnabled(True)
        self.infoLabel.setGeometry(QtCore.QRect(30, 70, 540, 101))
        self.infoLabel.setMaximumSize(QtCore.QSize(540, 101))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.infoLabel.setFont(font)
        self.infoLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.infoLabel.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.infoLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.infoLabel.setAutoFillBackground(False)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")

        # form for buttons and logins
        self.formWidget = QtWidgets.QWidget(startWindow)
        self.formWidget.setGeometry(QtCore.QRect(150, 170, 300, 160))
        self.formWidget.setObjectName("formWidget")

        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(10, 10, 10, 8)
        self.formLayout.setSpacing(8)
        self.formLayout.setObjectName("formLayout")
        self.loginLabel = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(10)

        self.loginLabel.setFont(font)
        self.loginLabel.setObjectName("loginLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.loginLabel)

        self.loginLine = QtWidgets.QLineEdit(self.formWidget)
        self.loginLine.setFont(font)
        self.loginLine.setAutoFillBackground(True)
        self.loginLine.setText("")
        self.loginLine.setMaxLength(40)
        self.loginLine.setFrame(True)
        self.loginLine.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.loginLine.setPlaceholderText("")
        self.loginLine.setClearButtonEnabled(False)
        self.loginLine.setObjectName("loginLine")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginLine)

        self.passwordLabel = QtWidgets.QLabel(self.formWidget)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)

        self.passwordLine = QtWidgets.QLineEdit(self.formWidget)
        self.passwordLine.setFont(font)
        self.passwordLine.setInputMask("")
        self.passwordLine.setText("")
        self.passwordLine.setMaxLength(40)
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setObjectName("passwordLine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLine)

        self.cancelButton = QtWidgets.QPushButton(self.formWidget)

        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.clicked.connect(self.passwordWindowOpener)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cancelButton)

        self.LogInButton = QtWidgets.QPushButton(self.formWidget)
        self.LogInButton.setFont(font)
        self.LogInButton.setObjectName("LogInButton")
        self.LogInButton.setDefault(True)
        self.LogInButton.clicked.connect(self.userCheck)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.LogInButton)

        font.setPointSize(10)
        self.newUserButton = QtWidgets.QPushButton(self.formWidget)
        self.newUserButton.setFont(font)
        self.newUserButton.setObjectName("newUserButton")
        self.newUserButton.clicked.connect(self.userEvent)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.newUserButton)

        self.Versionlabel = QtWidgets.QLabel(startWindow)
        self.Versionlabel.setGeometry(QtCore.QRect(10, 330, 111, 20))
        self.Versionlabel.setObjectName("Versionlabel")

        self.creatorsLabel = QtWidgets.QLabel(startWindow)
        self.creatorsLabel.setGeometry(QtCore.QRect(420, 330, 171, 20))
        self.creatorsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.creatorsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.creatorsLabel.setObjectName("creatorsLabel")

        self.retranslateUi(startWindow)
        QtCore.QMetaObject.connectSlotsByName(startWindow)

    def retranslateUi(self, startWindow):
        _translate = QtCore.QCoreApplication.translate
        self.startWindow.setWindowTitle(_translate("startWindow", "Linguenee"))
        self.nameLabel.setText(_translate("startWindow", "Linguenee"))
        self.infoLabel.setText(_translate("startWindow", "The program that helps people\n"
" to learn new languages by learning new words and phrases. \n"
" Perfect tool to get better, stronger, faster in language skills"))
        self.loginLabel.setText(_translate("startWindow", "Login"))
        self.passwordLabel.setText(_translate("startWindow", "Password"))
        self.cancelButton.setText(_translate("startWindow", " Forgot password? "))
        self.newUserButton.setText(_translate("startWindow", "New user"))
        self.LogInButton.setText(_translate("startWindow", "Log in"))
        self.Versionlabel.setText(_translate("startWindow", LINGUENEEVERSION))
        self.creatorsLabel.setText(_translate("startWindow", "With love: Linguenee team <3"))

    def passwordWindowOpener(self):
        print("you forgot your password")


    def userEvent(self):
        try:
            self.startWindow.close()
            RegisterWindow = QtWidgets.QMainWindow()
            self.ui1 = register.Ui_RegisterWindow()
            self.ui1.setupUi(RegisterWindow)
            RegisterWindow.show()

        except BaseException as err:
            self.error_in_app(str(err) + " in userEvent")

    def userWindowOpener(self):
        try:
            self.startWindow.close()
            RegisterWindow1 = QtWidgets.QMainWindow()
            self.ui2 = userWindow.Ui_mainWindow(self.currentUser)
            self.ui2.setupUi(RegisterWindow1)
            RegisterWindow1.show()

        except BaseException as err:
            self.error_in_app(str(err) + " in userEvent")


    def error_in_app(self, err):
        self.errorMsg = QMessageBox()
        self.errorMsg.setIcon(QMessageBox.Critical)
        self.errorMsg.setText("Error occurred! :( \nContact the developer! ")
        self.errorMsg.setWindowTitle("Error")
        self.errorMsg.setDetailedText(err)
        self.errorMsg.setStandardButtons(QMessageBox.Ok)
        returnValue = self.errorMsg.exec()

    def userCheck(self):
        try:

            userID = passCreator.deletingEndSpace(self.loginLine.text())
            userPass = passCreator.deletingEndSpace(self.passwordLine.text())

            users = passCreator.open_list_file(HOMEDIR,"userInfoFIle.ling")
            for user in users:
                if user["login"] == userID:
                    if passCreator.verify_password(user["password"], userPass):
                        print(user)
                        exists = True
                        break
                else:
                    exists = False

        except Exception as err:
            error_in_app(err)

        if exists == True:
            print("False")
            self.currentUser = userID
            self.userWindowOpener()

            print("your login is: " + userID)
            print("your password is: " + userPass)


if __name__ == "__main__":
    try:
        global app
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle(APPSTYLE)
        startWindow = QtWidgets.QDialog()
        ui = Ui_startWindow()
        ui.setupUi(startWindow)
        startWindow.show()
        sys.exit(app.exec_())
    except Exception as err:
        print("Error: ", err)
