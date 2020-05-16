# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import datetime
from progData import *
import passCreator


class Ui_mainWindow(object):
    """
    User  window. The main window for user, where he/she can add new sets,
    modify them, start a test, satrt learning a set or just change user data.
    """
    def __init__(self, UserID):
        self.UserID = UserID

    def setupUi(self, mainWindow):
        self.mainWindow = mainWindow

        self.mainWindow.setObjectName("mainWindow")
        self.mainWindow.resize(561, 500)
        self.centralwidget = QtWidgets.QWidget(self.mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # adding date in main window
        self.labelDate = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelDate.setFont(font)
        self.labelDate.setObjectName("labelDate")
        self.gridLayout.addWidget(self.labelDate, 2, 5, 1, 1)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.onTimeout)
        self.timer.start(1000)

        # program name lable
        self.labelLinguenee = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(LOGOSTILE)
        font.setPointSize(22)
        self.labelLinguenee.setFont(font)
        self.labelLinguenee.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLinguenee.setObjectName("labelLinguenee")
        self.gridLayout.addWidget(self.labelLinguenee, 1, 0, 1, 6)

        # user ID label
        self.labelUserID = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelUserID.setFont(font)
        self.labelUserID.setObjectName("labelUserID")
        self.gridLayout.addWidget(self.labelUserID, 2, 0, 1, 1)

        # version of the program
        self.labelVersion = QtWidgets.QLabel(self.centralwidget)
        self.labelVersion.setObjectName("labelVersion")
        self.gridLayout.addWidget(self.labelVersion, 5, 0, 1, 1)


        ### Scroll area of add new set and achivements
        # adding main information about scroll area
        self.scrollAreaUser = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaUser.setWidgetResizable(True)
        self.scrollAreaUser.setObjectName("scrollAreaUser")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -48, 228, 242))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # information about achivements and adding a new set:
        # first creating a widget
        self.tabWidgetUser = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidgetUser.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidgetUser.setFont(font)
        self.tabWidgetUser.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidgetUser.setObjectName("tabWidgetUser")

        # achivements window
        self.achivements = QtWidgets.QWidget()
        self.achivements.setObjectName("achivements")
        self.formLayout_2 = QtWidgets.QFormLayout(self.achivements)
        self.formLayout_2.setObjectName("formLayout_2")

        # a lot of different labels
        self.lebelSetQuantity1 = QtWidgets.QLabel(self.achivements)
        self.lebelSetQuantity1.setObjectName("lebelSetQuantity1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lebelSetQuantity1)

        self.labelSetQuantity2 = QtWidgets.QLabel(self.achivements)
        self.labelSetQuantity2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSetQuantity2.setText("1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelSetQuantity2)

        self.labelSetsFinished1 = QtWidgets.QLabel(self.achivements)
        self.labelSetsFinished1.setObjectName("labelSetsFinished1")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelSetsFinished1)

        self.labelSetsFinished2 = QtWidgets.QLabel(self.achivements)
        self.labelSetsFinished2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSetsFinished2.setText("1")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelSetsFinished2)

        self.labelSetsInProgress1 = QtWidgets.QLabel(self.achivements)
        self.labelSetsInProgress1.setObjectName("labelSetsInProgress1")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelSetsInProgress1)

        self.labelSetInProgress2 = QtWidgets.QLabel(self.achivements)
        self.labelSetInProgress2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSetInProgress2.setText("1")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelSetInProgress2)

        self.labelTests = QtWidgets.QLabel(self.achivements)
        self.labelTests.setObjectName("labelTests")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelTests)

        self.labelTests2 = QtWidgets.QLabel(self.achivements)
        #self.labelTests2.setObjectName("labelTests2")

        your_sets = passCreator.open_set_in_use(self.UserID)
        your_sets_string = ''
        for set in your_sets:
            your_sets_string += "  " + set + "\n"
        self.labelTests2.setText("Your Sets in use:\n" + your_sets_string )
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.labelTests2)

        # progressBar
        self.progressBar = QtWidgets.QProgressBar(self.achivements)
        self.progressBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.progressBar.setProperty("value", 57)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.progressBar)

        # add items above
        self.labelPercent = QtWidgets.QLabel(self.achivements)
        self.labelPercent.setObjectName("labelPercent")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelPercent)
        self.tabWidgetUser.addTab(self.achivements, "")

        ## 3d tab in user info
        # adding tab set
        self.sets_in_use = QtWidgets.QWidget()
        self.sets_in_use.setObjectName("sets_in_use")
        self.formLayout_10 = QtWidgets.QFormLayout(self.sets_in_use)
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_sets_use = QtWidgets.QLabel(self.sets_in_use)

        your_sets = passCreator.openUserSetList(self.UserID)
        your_sets_string = ''
        for set in your_sets:
            your_sets_string += "  " + set + "\n"

        self.label_sets_use.setText("Sets that you can modify:\n"+ your_sets_string)
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_sets_use)
        self.tabWidgetUser.addTab(self.sets_in_use, "")

        ### Creating a new set window item
        # Create new set
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayout_3 = QtWidgets.QFormLayout(self.tab)
        self.formLayout_3.setObjectName("formLayout_3")

        #  label create new set
        self.labelCreateNewSet = QtWidgets.QLabel(self.tab)
        self.labelCreateNewSet.setObjectName("labelCreateNewSet")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.labelCreateNewSet)

        # label set Name of set
        self.labelSetName = QtWidgets.QLabel(self.tab)
        self.labelSetName.setObjectName("labelSetName")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelSetName)

        # edit_line: specify name
        self.lineEditSetName = QtWidgets.QLineEdit(self.tab)
        self.lineEditSetName.setObjectName("lineEditSetName")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditSetName)

        # Label comboBox_lang_1
        self.labelLanguage1 = QtWidgets.QLabel(self.tab)
        self.labelLanguage1.setObjectName("labelLanguage1")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelLanguage1)

        # comboBox_lang_1
        self.comboBoxLanguage = QtWidgets.QComboBox(self.tab)
        self.comboBoxLanguage.setObjectName("comboBoxLanguage")
        self.language_items_1 = LANGUAGESTOLEARN
        self.comboBoxLanguage.addItems(self.language_items_1)
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBoxLanguage)

        # Label comboBox_lang_2
        self.labelLanguage2 = QtWidgets.QLabel(self.tab)
        self.labelLanguage2.setObjectName("labelLanguage2")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelLanguage2)

        # comboBox_lang_2
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.language_items_2 = LANGUAGESTOLEARN
        self.comboBox.addItems(self.language_items_2)
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox)

        # Button - create new set
        self.pushButtonCreate = QtWidgets.QPushButton(self.tab)
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.pushButtonCreate.clicked.connect(self.create_set)
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButtonCreate)

        # label after created sets
        self.labelAfterCreateSet = QtWidgets.QLabel(self.tab)
        self.labelAfterCreateSet.setObjectName("labelAfterCreateSet")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.labelAfterCreateSet)

        self.tabWidgetUser.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidgetUser, 0, 1, 1, 1)
        self.scrollAreaUser.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollAreaUser, 3, 0, 1, 2)
        # end of scorll Area Widgent Contents

        ### Scroll area for set modifier
        # main option for set modifier area
        self.scrollAreaSetModifier = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaSetModifier.setMinimumSize(QtCore.QSize(242, 148))
        self.scrollAreaSetModifier.setWidgetResizable(True)
        self.scrollAreaSetModifier.setObjectName("scrollAreaSetModifier")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 245, 146))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_4)
        self.formLayout_4.setObjectName("formLayout_4")

        # modify set label
        self.labelModifySet = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelModifySet.setFont(font)
        self.labelModifySet.setAlignment(QtCore.Qt.AlignCenter)
        self.labelModifySet.setObjectName("labelModifySet")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.labelModifySet)

        # line in modify set
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_3)

        # comboBox sets to modify
        self.comboBoxModifySet = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.comboBoxModifySet.setObjectName("comboBoxModifySet")
        sets_to_modify = passCreator.openUserSetList(self.UserID)
        #sets_to_modify = ["Numbers","Medicine","Coronavirus",]
        self.comboBoxModifySet.addItems(sets_to_modify)
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.comboBoxModifySet)

        # another invisible line
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.line)

        # button modify set
        self.pushButtonModify = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButtonModify.setObjectName("pushButtonModify")
        self.pushButtonModify.clicked.connect(self.modify_set)
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.pushButtonModify)

        # button to add set to your list
        self.ButtonAddSetToYourList = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.ButtonAddSetToYourList.setObjectName("ButtonAddSetToYourList")
        self.ButtonAddSetToYourList.clicked.connect(self.set_to_your_list)
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.ButtonAddSetToYourList)

        self.scrollAreaSetModifier.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout.addWidget(self.scrollAreaSetModifier, 4, 0, 1, 2)
        # and of scorll area set modifier

        self.scrollAreaLearn = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaLearn.setMinimumSize(QtCore.QSize(179, 149))
        self.scrollAreaLearn.setMaximumSize(QtCore.QSize(16777215, 149))
        self.scrollAreaLearn.setWidgetResizable(True)
        self.scrollAreaLearn.setObjectName("scrollAreaLearn")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 288, 147))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.formLayout_5 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_5.setObjectName("formLayout_5")
        self.labelLearnOptions = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.labelLearnOptions.setObjectName("labelLearnOptions")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelLearnOptions)

        self.comboBoxLearnSet = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBoxLearnSet.setObjectName("comboBoxLearnSet")
        list_learnig_sets = passCreator.open_set_in_use(self.UserID)
        #list_learnig_sets = ["Numbers", "Coronavirus", "Medicine"]
        self.comboBoxLearnSet.addItems(list_learnig_sets)
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBoxLearnSet)

        self.comboBoxLearnOptions = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBoxLearnOptions.setObjectName("comboBoxLearnOptions")
        list_learnig_options = ["Option 1", "Option 2"]
        self.comboBoxLearnOptions.addItems(list_learnig_options)
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBoxLearnOptions)

        self.labelLearnSet = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.labelLearnSet.setObjectName("labelLearnSet")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelLearnSet)
        self.lineLearn = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.lineLearn.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineLearn.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineLearn.setObjectName("lineLearn")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.lineLearn)
        self.pushButtonLearnLet = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButtonLearnLet.setObjectName("pushButtonLearnLet")
        self.pushButtonLearnLet.clicked.connect(self.learn)

        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pushButtonLearnLet)
        self.labelLearn = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.labelLearn.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelLearn.setFont(font)
        self.labelLearn.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelLearn.setWordWrap(False)
        self.labelLearn.setObjectName("labelLearn")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.labelLearn)
        self.scrollAreaLearn.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollAreaLearn, 3, 2, 1, 4)

        ### Test scroll Area
        # adding main engine
        self.scrollAreaTest = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaTest.setMinimumSize(QtCore.QSize(179, 148))
        self.scrollAreaTest.setMaximumSize(QtCore.QSize(16777215, 158))
        self.scrollAreaTest.setWidgetResizable(True)
        self.scrollAreaTest.setObjectName("scrollAreaTest")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 288, 146))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.formLayout_6 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_6.setObjectName("formLayout_6")

        # label test
        self.labelTest = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelTest.setFont(font)
        self.labelTest.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelTest.setObjectName("labelTest")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.labelTest)

        # added lines
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.line_5)

        # label test set
        self.labelTestSet = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelTestSet.setObjectName("labelTestSet")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelTestSet)

        # combo box in test
        self.comboBoxSetTest = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBoxSetTest.setObjectName("comboBoxSetTest")
        test_sets = passCreator.open_set_in_use(self.UserID)
        #test_sets = ["Numbers","Fuels","Animals","Genetics"]
        self.comboBoxSetTest.addItems(test_sets)
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBoxSetTest)

        # label test levels
        self.labelTestLevels = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelTestLevels.setObjectName("labelTestLevels")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelTestLevels)

        # combobox test levels
        self.comboBoxTestLevels = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBoxTestLevels.setObjectName("comboBoxTestLevels")
        test_levels = ["Easy", "Middle", "Hard"]
        self.comboBoxTestLevels.addItems(test_levels)
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBoxTestLevels)

        # button tests
        self.pushButtonTestLet = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButtonTestLet.setObjectName("pushButtonTestLet")
        self.formLayout_6.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButtonTestLet)
        self.scrollAreaTest.setWidget(self.scrollAreaWidgetContents_3)
        # add Test to grid layout
        self.gridLayout.addWidget(self.scrollAreaTest, 4, 2, 1, 4)
        # end of test area

        ### Button LogOut
        self.pushButtonLogOut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLogOut.setObjectName("pushButtonLogOut")
        self.gridLayout.addWidget(self.pushButtonLogOut, 5, 5, 1, 1)

        ### Button Cancel
        self.pushButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.pushButtonCancel.clicked.connect(self.OpenStartWindow)
        self.gridLayout.addWidget(self.pushButtonCancel, 5, 4, 1, 1)

        ### menu options
        self.mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menusdfa = QtWidgets.QMenu(self.menubar)
        self.menusdfa.setTitle("")
        self.menusdfa.setObjectName("menusdfa")
        self.mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        self.mainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(mainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionChangeUserData = QtWidgets.QAction(mainWindow)
        self.actionChangeUserData.setObjectName("actionChangeUserData")
        self.actionAdmin = QtWidgets.QAction(mainWindow)
        self.actionAdmin.setObjectName("actionAdmin")
        self.menuOptions.addAction(self.actionHelp)
        self.menuOptions.addAction(self.actionAdmin)
        self.menuOptions.addAction(self.actionChangeUserData)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menusdfa.menuAction())

        self.retranslateUi(mainWindow)
        self.tabWidgetUser.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.mainWindow.setWindowTitle(_translate("mainWindow", "Linguenee - User Window"))
        self.labelDate.setText(_translate("mainWindow", "{0}".format(self.timeNow())))

        self.labelTest.setText(_translate("mainWindow", "Test"))
        self.labelTestSet.setText(_translate("mainWindow", "Set:"))
        self.labelTestLevels.setText(_translate("mainWindow", "Levels:"))
        self.pushButtonTestLet.setText(_translate("mainWindow", "Let\'s Go"))
        self.labelModifySet.setText(_translate("mainWindow", "Modify Set:"))
        self.pushButtonModify.setText(_translate("mainWindow", "Modify"))
        self.ButtonAddSetToYourList.setText(_translate("mainWindow", "Add exsisting set to your list"))
        self.lebelSetQuantity1.setText(_translate("mainWindow", "Set quantity:"))

        self.labelSetsFinished1.setText(_translate("mainWindow", "Sets finished:"))
        self.labelSetsInProgress1.setText(_translate("mainWindow", "Sets in progress:"))
        self.labelTests.setText(_translate("mainWindow", "Tests:"))

        self.progressBar.setFormat(_translate("mainWindow", "%p%"))
        self.labelPercent.setText(_translate("mainWindow", "Percent done:"))
        self.tabWidgetUser.setTabText(self.tabWidgetUser.indexOf(self.achivements), _translate("mainWindow", "Progress"))
        self.tabWidgetUser.setTabText(self.tabWidgetUser.indexOf(self.sets_in_use), _translate("mainWindow", "Sets"))
        self.tabWidgetUser.setTabText(self.tabWidgetUser.indexOf(self.tab), _translate("mainWindow", "New set"))

        self.labelCreateNewSet.setText(_translate("mainWindow", "Create new set:"))
        self.labelSetName.setText(_translate("mainWindow", "Set Name:"))
        self.labelLanguage1.setText(_translate("mainWindow", "Language1:"))

        self.labelAfterCreateSet.setText(_translate("mainWindow", "If you want add some words to \n"
" your set  go to modify table"))
        self.labelLanguage2.setText(_translate("mainWindow", "Language2:"))
        self.pushButtonCreate.setText(_translate("mainWindow", "Create"))

        self.labelLearnOptions.setText(_translate("mainWindow", "Options:"))
        self.labelLearnSet.setText(_translate("mainWindow", "Set:"))
        self.pushButtonLearnLet.setText(_translate("mainWindow", "Let\'s Go"))
        self.labelLearn.setText(_translate("mainWindow", "Learn"))
        self.labelLinguenee.setText(_translate("mainWindow", "Linguenee"))
        self.labelVersion.setText(_translate("mainWindow", LINGUENEEVERSION))
        self.UserVar = "User: " + self.UserID
        self.labelUserID.setText(_translate("mainWindow", self.UserVar))
        self.pushButtonLogOut.setText(_translate("mainWindow", "Log out"))
        self.pushButtonCancel.setText(_translate("mainWindow", "Cancel"))
        self.menuOptions.setTitle(_translate("mainWindow", "Options"))
        self.actionHelp.setText(_translate("mainWindow", "Help"))
        self.actionChangeUserData.setText(_translate("mainWindow", "Change user data"))
        self.actionAdmin.setText(_translate("mainWindow", "Admin"))

    def OpenStartWindow(self):
        print("You want to go to start Window")
        import startWindow as s
        self.mainWindow.close()
        startWindow = QtWidgets.QDialog()
        self.ui = s.Ui_startWindow()
        self.ui.setupUi(startWindow)
        startWindow.show()

    def onTimeout(self):
        self.labelDate.setText("    {0}".format(self.timeNow()))

    def timeNow(self):
        return(datetime.datetime.now()).strftime("%H:%M:%S  %d-%m-%Y")

    def create_set(self):
        new_set_name = self.lineEditSetName.text()
        language_1 = self.comboBoxLanguage.currentText()
        language_2 = self.comboBox.currentText()
        newset = [new_set_name, language_1, language_2]
        fold_name = language_1 + "-" + language_2
        #if not exsitst
        try:
            if passCreator.set_exsists(new_set_name) == False:

                passCreator.create_user_file(self.UserID)
                passCreator.create_set_file(self.UserID, fold_name, new_set_name)
                msg = new_set_name+ " Successfully created"
                self.message(new_set_name, msg)
                # adding item to our set
                self.comboBoxModifySet.addItem(new_set_name)
                self.comboBoxSetTest.addItem(new_set_name)
                self.comboBoxLearnSet.addItem(new_set_name)

                your_sets = passCreator.openUserSetList(self.UserID)
                your_sets_string = ''
                for set in your_sets:
                    your_sets_string += "  " + set + "\n"

                self.label_sets_use.setText("Sets that you can modify:\n"+ your_sets_string)

                your_sets = passCreator.open_set_in_use(self.UserID)
                your_sets_string = ''
                for set in your_sets:
                    your_sets_string += "  " + set + "\n"
                self.labelTests2.setText("Your Sets in use:\n" + your_sets_string )

            else:
                msg = new_set_name+ " Already exsitsts"
                self.message(new_set_name, msg)
        except Exception as err:
            print(err)

    def modify_set(self):
        print("You want to modify_set")

        set_to_modify = self.comboBoxModifySet.currentText()
        if set_to_modify:
            import AddWordWindow as add
            # self.mainWindow.close()
            AddWords = QtWidgets.QDialog()
            self.uif = add.Ui_AddWords()
            self.uif.setupUi(AddWords, set_to_modify)
            AddWords.show()

    def set_to_your_list(self):
        import AddSetList as add1

        Dialog = QtWidgets.QDialog()
        self.ui1 = add1.Ui_Dialog()
        self.ui1.setupUi(Dialog, self.UserID)
        Dialog.show()

    def learn(self):
        try:
            lern_set = self.comboBoxLearnSet.currentText()
            userDir = USERFILESDIR + "\\" + self.UserID + "\\u_sets"
            file = passCreator.open_list_file(userDir , lern_set)
            for f in file:
                print(f)
        except Exception as err:
            print(err)

    def message(self, msg, msg_text):
        self.NewUserMsg = QMessageBox()
        self.NewUserMsg.setIcon(QMessageBox.Information)
        self.NewUserMsg.setText(msg_text)
        self.NewUserMsg.setWindowTitle(msg)
        self.NewUserMsg.setStandardButtons(QMessageBox.Ok)
        returnValue = self.NewUserMsg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(APPSTYLE)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow("Admin")
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
