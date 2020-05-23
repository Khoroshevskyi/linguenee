# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from progData import *
import passCreator

class Ui_TestWindow(object):
    def setupUi(self, TestWindow, UserID, SetName):
        self.UserID = UserID
        self.SetName = SetName
        self.TestWindow = TestWindow
        self.TestWindow.setObjectName("TestWindow")
        self.TestWindow.resize(455, 274)
        self.gridLayout = QtWidgets.QGridLayout(self.TestWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.TestWindow)
        self.label.setMaximumSize(QtCore.QSize(16777215, 46))
        font = QtGui.QFont()
        font.setFamily(LOGOSTILE)
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_word2 = QtWidgets.QLabel(self.TestWindow)
        self.label_word2.setObjectName("label_word2")
        self.gridLayout.addWidget(self.label_word2, 3, 0, 1, 1)

        self.pushButton_check = QtWidgets.QPushButton(self.TestWindow)
        self.pushButton_check.setObjectName("pushButton_check")
        self.gridLayout.addWidget(self.pushButton_check, 5, 1, 1, 1)

        self.label_word = QtWidgets.QLabel(self.TestWindow)
        self.label_word.setMinimumSize(QtCore.QSize(216, 0))
        self.label_word.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_word.setObjectName("label_word")
        self.gridLayout.addWidget(self.label_word, 2, 0, 1, 1)

        self.label_word3 = QtWidgets.QLabel(self.TestWindow)
        self.label_word3.setObjectName("label_word3")
        self.gridLayout.addWidget(self.label_word3, 4, 0, 1, 1)

        self.pushButton_score = QtWidgets.QPushButton(self.TestWindow)
        self.pushButton_score.setObjectName("pushButton_score")
        self.gridLayout.addWidget(self.pushButton_score, 5, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.TestWindow)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.lineEdit_word1 = QtWidgets.QLineEdit(self.TestWindow)
        self.lineEdit_word1.setObjectName("lineEdit_word1")
        self.gridLayout.addWidget(self.lineEdit_word1, 2, 1, 1, 1)

        self.lineEdit_word_2 = QtWidgets.QLineEdit(self.TestWindow)
        self.lineEdit_word_2.setObjectName("lineEdit_word_2")
        self.gridLayout.addWidget(self.lineEdit_word_2, 3, 1, 1, 1)

        self.lineEdit_word_3 = QtWidgets.QLineEdit(self.TestWindow)
        self.lineEdit_word_3.setObjectName("lineEdit_word_3")
        self.gridLayout.addWidget(self.lineEdit_word_3, 4, 1, 1, 1)

        self.retranslateUi(self.TestWindow)
        QtCore.QMetaObject.connectSlotsByName(self.TestWindow)

    def retranslateUi(self, TestWindow):
        _translate = QtCore.QCoreApplication.translate
        self.TestWindow.setWindowTitle(_translate("TestWindow", "Dialog"))
        self.label.setText(_translate("TestWindow", "Linguenee"))
        self.label_word2.setText(_translate("TestWindow", "TextLabel"))
        self.pushButton_check.setText(_translate("TestWindow", "next"))
        self.label_word.setText(_translate("TestWindow", "Word"))
        self.label_word3.setText(_translate("TestWindow", "TextLabel"))
        self.pushButton_score.setText(_translate("TestWindow", "See scores"))
        start_text = "You are taking test of:  " + self.SetName + "\nPass it!"
        self.label_2.setText(_translate("LearnWindow", start_text))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TestWindow = QtWidgets.QDialog()
    ui = Ui_TestWindow()
    ui.setupUi(TestWindow, "1","2")
    TestWindow.show()
    sys.exit(app.exec_())
"""
