from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import passCreator
import sys
from dateutil.relativedelta import relativedelta
import datetime
from progData import *

class Ui_RegisterWindow(object):

    def setupUi(self, RegisterWindow):
        self.RegisterWindow = RegisterWindow
        self.RegisterWindow.setObjectName("RegisterWindow")
        self.RegisterWindow.resize(374, 470)
        self.centralwidget = QtWidgets.QWidget(self.RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.MainLayout.setObjectName("MainLayout")

        # linguenee name
        self.Linguenee = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(LOGOSTILE)
        font.setPointSize(20)
        self.Linguenee.setFont(font)
        self.Linguenee.setAlignment(QtCore.Qt.AlignCenter)
        self.Linguenee.setObjectName("Linguenee")
        self.MainLayout.addWidget(self.Linguenee, 0, 0, 1, 1)

        # infoLabel
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.infoLabel.setFont(font)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.MainLayout.addWidget(self.infoLabel, 1, 0, 1, 1)

        # added scroll area to main layout
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(320, 100))
        scrollFont = QtGui.QFont()
        scrollFont .setFamily("Arial")
        scrollFont .setPointSize(10)
        self.scrollArea.setFont(scrollFont)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 354, 250))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # input Area Grid added to scroll area
        self.inputAreaGrid = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.inputAreaGrid.setObjectName("inputAreaGrid")

        # name
        self.nameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setObjectName("nameLabel")
        self.inputAreaGrid.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.nameEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.nameEdit.setObjectName("nameEdit")
        self.inputAreaGrid.addWidget(self.nameEdit, 0, 1, 1, 1)

        # surname
        self.surnameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.surnameLabel.setObjectName("surnameLabel")
        self.inputAreaGrid.addWidget(self.surnameLabel, 1, 0, 1, 1)

        self.surnameEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.surnameEdit.setObjectName("surnameEdit")
        self.inputAreaGrid.addWidget(self.surnameEdit, 1, 1, 1, 1)

        self.emailLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.emailLabel.setObjectName("emailLabel")
        self.inputAreaGrid.addWidget(self.emailLabel, 2, 0, 1, 1)

        self.emailEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.emailEdit.setObjectName("emailEdit")
        self.inputAreaGrid.addWidget(self.emailEdit, 2, 1, 1, 1)

        # age
        self.ageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ageLabel.setObjectName("ageLabel")
        self.inputAreaGrid.addWidget(self.ageLabel, 4, 0, 1, 1)

        self.date_of_birth = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.date_of_birth.setObjectName("date")
        self.date_of_birth = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        # only for age +6
        self.date_of_birth.setMaximumDate(datetime.datetime.now()- relativedelta(years=6))
        self.date_of_birth.setDisplayFormat("dd-MM-yyyy")
        self.date_of_birth.setCalendarPopup(True)

        self.inputAreaGrid.addWidget(self.date_of_birth, 4, 1, 1, 1)

        # sex
        self.sexLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sexLabel.setObjectName("sexLabel")
        self.inputAreaGrid.addWidget(self.sexLabel, 3, 0, 1, 1)

        self.sexBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.sexBox.setObjectName("sexBox")
        self.sexBox.addItem("")
        self.sexBox.addItem("")
        self.inputAreaGrid.addWidget(self.sexBox, 3, 1, 1, 1)

        # login
        self.loginLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.loginLabel.setObjectName("loginLabel")
        self.inputAreaGrid.addWidget(self.loginLabel, 5, 0, 1, 1)

        self.loginEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.loginEdit.setObjectName("loginEdit")
        self.inputAreaGrid.addWidget(self.loginEdit, 5, 1, 1, 1)

        # password 1
        self.passwordLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.passwordLabel.setObjectName("passwordLabel")
        self.inputAreaGrid.addWidget(self.passwordLabel, 6, 0, 1, 1)

        self.passwordEdit1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.passwordEdit1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit1.setObjectName("passwordEdit1")
        self.inputAreaGrid.addWidget(self.passwordEdit1, 6, 1, 1, 1)

        # password 2
        self.passwordLabel2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.passwordLabel2.setObjectName("passwordLabel2")
        self.inputAreaGrid.addWidget(self.passwordLabel2, 7, 0, 1, 1)

        self.passwordEdit2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.passwordEdit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit2.setObjectName("passwordEdit2")
        self.inputAreaGrid.addWidget(self.passwordEdit2, 7, 1, 1, 1)

        # rules check
        self.rulesBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.rulesBox.setMouseTracking(True)
        self.rulesBox.setObjectName("rulesBox")
        self.inputAreaGrid.addWidget(self.rulesBox, 8, 0, 1, 1)

        self.rulesButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        fontRulBut = QtGui.QFont()
        fontRulBut.setBold(True)
        fontRulBut.setItalic(False)
        fontRulBut.setWeight(75)
        self.rulesButton.setFont(fontRulBut)
        self.rulesButton.setObjectName("rulesButton")
        self.inputAreaGrid.addWidget(self.rulesButton, 8, 1, 1, 1)

        # end of inputAreaGrid
        # end of scroll area

        # button box to save new user
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(self.saveNewUser)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Save).setDefault(True)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Discard).clicked.connect(self.discardNewUser)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.MainLayout.addWidget(self.buttonBox, 5, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.MainLayout.addWidget(self.scrollArea, 4, 0, 1, 1)
        self.RegisterWindow.setCentralWidget(self.centralwidget)

        # menu bar
        self.menubar = QtWidgets.QMenuBar(RegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 21))
        self.menubar.setObjectName("menubar")

        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")

        self.menuSave = QtWidgets.QMenu(self.menubar)
        self.menuSave.setObjectName("menuSave")
        self.RegisterWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        self.RegisterWindow.setStatusBar(self.statusbar)

        self.actionsave = QtWidgets.QAction(RegisterWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionProgram = QtWidgets.QAction(RegisterWindow)
        self.actionProgram.setObjectName("actionProgram")
        self.actionDevelopers = QtWidgets.QAction(RegisterWindow)
        self.actionDevelopers.setObjectName("actionDevelopers")
        self.actionSpecification = QtWidgets.QAction(RegisterWindow)
        self.actionSpecification.setObjectName("actionSpecification")
        self.menuInfo.addAction(self.actionProgram)
        self.menuInfo.addAction(self.actionDevelopers)
        self.menuInfo.addAction(self.actionSpecification)
        self.menuSave.addAction(self.actionsave)
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menubar.addAction(self.menuSave.menuAction())

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        self.RegisterWindow.setWindowTitle(_translate("RegisterWindow", "User registration"))
        self.infoLabel.setText(_translate("RegisterWindow", "Linguenee registration form \n"
"Start your journey right now! \n"))
        self.Linguenee.setText(_translate("RegisterWindow", "Linguenee"))
        self.ageLabel.setText(_translate("RegisterWindow", "Birth date:"))
        self.rulesBox.setText(_translate("RegisterWindow", "I agree with the rules"))
        self.passwordLabel2.setText(_translate("RegisterWindow", "Repeat Password:"))
        self.passwordLabel.setText(_translate("RegisterWindow", "Password:"))
        self.surnameLabel.setText(_translate("RegisterWindow", "Surname:"))
        self.emailLabel.setText(_translate("RegisterWindow", "E-mail:"))
        self.nameLabel.setText(_translate("RegisterWindow", "Name:"))
        self.sexLabel.setText(_translate("RegisterWindow", "Sex:"))
        self.loginLabel.setText(_translate("RegisterWindow", "Login:"))
        self.rulesButton.setText(_translate("RegisterWindow", "Rules"))
        self.sexBox.setItemText(0, _translate("RegisterWindow", "Male"))
        self.sexBox.setItemText(1, _translate("RegisterWindow", "Female"))
        self.menuInfo.setTitle(_translate("RegisterWindow", "Info"))
        self.menuSave.setTitle(_translate("RegisterWindow", "Save"))
        self.actionsave.setText(_translate("RegisterWindow", "Save "))
        self.actionsave.setShortcut(_translate("RegisterWindow", "Ctrl+S"))
        self.actionProgram.setText(_translate("RegisterWindow", "Program"))
        self.actionDevelopers.setText(_translate("RegisterWindow", "Developers"))
        self.actionSpecification.setText(_translate("RegisterWindow", "Specification"))

    def saveNewUser(self):
        print("Button save cklicked")
        if self.rulesBox.isChecked() == True:
            try:
                userName = passCreator.deletingEndSpace(self.nameEdit.text())
                userSurname = passCreator.deletingEndSpace(self.surnameEdit.text())
                userEmail = passCreator.deletingEndSpace(self.emailEdit.text())

                userDoF = self.date_of_birth.dateTime()
                userDoF = userDoF.toString(self.date_of_birth.displayFormat())
                userSex = self.sexBox.currentText()
                userID = passCreator.deletingEndSpace(self.loginEdit.text())

                userPassword1 = passCreator.deletingEndSpace(self.passwordEdit1.text())
                userPassword2 = passCreator.deletingEndSpace(self.passwordEdit2.text())

                # checking if all fields are not empty:
                textArray = [userName, userSurname, userID, userPassword1, userEmail]
                messageArray = ["Your name", "Your surname", "Your login", "Your password", "Your Email"]
                for nr in range(len(textArray)):
                    if self.isNotEmpty(textArray[nr], messageArray[nr]) == False:
                        boolNotEmpty = False
                        break
                    else:
                        boolNotEmpty = True

                # checking if the login already exists:
                boolLoginExists = self.loginExist(userID)

                # checking if passwords are same:
                boolPasswordSame = self.samePassword(userPassword1, userPassword2)

                if boolNotEmpty and boolLoginExists and boolPasswordSame:
                    todayDate = datetime.datetime.now()
                    userInfo = {"login": userID,
                                "password": passCreator.hash_password(userPassword1),
                                "email": userEmail,
                                "name": userName,
                                "surname": userSurname,
                                "birthday": userDoF,
                                "sex": userSex,
                                "date": todayDate.strftime("%d-%m-%Y")}

                    passCreator.saveUserDataFile(userInfo)
                    self.newUserMsg(userName)
                    passCreator.create_user_file(userInfo["login"])
                    passCreator.directoryFind(SETSDIR)

                    # printing info
                    allUserData = passCreator.open_list_file(HOMEDIR,USERINFOFILE)
                    for k in allUserData:
                        print(k)


            except Exception as err:
                print("error in 'saveNewUser' function:", err)
                error_in_app(err)
        else:
            self.IncorrectData("Hey, You didn't checked chackbox with rules!")

    def loginExist(self, login):
        allUserData = passCreator.open_list_file(HOMEDIR, USERINFOFILE)
        if any(Ulogin["login"] == login for Ulogin in allUserData):
            message = "This loign already exists :/"
            self.IncorrectData(message)
            return False
        else:
            return True

    def samePassword(self, password1, password2):
        if password1 == password2:
            if len(password1) < 5:
                self.IncorrectData("Your password has to contain more than 5 symbols!")
            elif any(char.isdigit() for char in password1) == False:
                self.IncorrectData("Your password has to contain at least 1 digit")
            else:
                return True
        else:
            self.IncorrectData("Hey, You didn't enter two same passwords!")
            return False

    def isNotEmpty(self, word, item):
        if word != "":
            return True
        else:
            self.IncorrectData("You didn't fill " + item)
            return False

    def IncorrectData(self, message):
        self.incorPassMsg = QMessageBox()
        self.incorPassMsg.setIcon(QMessageBox.Critical)
        self.incorPassMsg.setText(message)
        self.incorPassMsg.setWindowTitle("Error while entering information")
        self.incorPassMsg.setStandardButtons(QMessageBox.Ok)
        returnValue = self.incorPassMsg.exec()

    def discardNewUser(self):
        self.closeMsg = QMessageBox()
        self.closeMsg.setIcon(QMessageBox.Question)
        self.closeMsg.setText("Do You want to dsicard all information you entered?")
        self.closeMsg.setWindowTitle("Exit")
        self.closeMsg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        self.closeMsg.setDefaultButton(QMessageBox.No)
        returnValue = self.closeMsg.exec()
        if returnValue == QMessageBox.Yes:
            self.openStartWindow()

    def openStartWindow(self):
        import startWindow as s
        self.RegisterWindow.close()
        startWindow = QtWidgets.QDialog()
        self.ui = s.Ui_startWindow()
        self.ui.setupUi(startWindow)
        startWindow.show()

    def error_in_app(self, err):
        self.errorMsg = QMessageBox()
        self.errorMsg.setIcon(QMessageBox.Critical)
        self.errorMsg.setText("Error occurred! :( \nContact the developer! ")
        self.errorMsg.setWindowTitle("Error")
        self.errorMsg.setDetailedText(err)
        self.errorMsg.setStandardButtons(QMessageBox.Ok)
        returnValue = self.errorMsg.exec()

    def newUserMsg(self, userName):
        self.NewUserMsg = QMessageBox()
        self.NewUserMsg.setIcon(QMessageBox.Information)
        self.NewUserMsg.setText("Congratulations, %s ! \nYou became a new user!" %userName)
        self.NewUserMsg.setWindowTitle("Congratulations")
        self.NewUserMsg.setStandardButtons(QMessageBox.Ok)
        returnValue = self.NewUserMsg.exec()
        self.openStartWindow()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(APPSTYLE)
    RegisterWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())
