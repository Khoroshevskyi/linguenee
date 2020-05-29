# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from progData import *
import passCreator
import random

class Ui_LearnWindow(object):
    def setupUi(self, LearnWindow1, UserID, SetName):
        self.UserID = UserID
        self.SetName = SetName
        self.read_set()

        self.LearnWindow1 = LearnWindow1
        self.LearnWindow1.setObjectName("LearnWindow1")
        self.LearnWindow1.resize(455, 274)
        self.gridLayout = QtWidgets.QGridLayout(self.LearnWindow1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.LearnWindow1)
        self.label.setMaximumSize(QtCore.QSize(16777215, 46))
        font = QtGui.QFont()
        font.setFamily(LOGOSTILE)
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        font = QtGui.QFont()
        font.setPointSize(12)

        self.label_word = QtWidgets.QLabel(self.LearnWindow1)
        self.label_word.setMinimumSize(QtCore.QSize(216, 0))
        self.label_word.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_word.setObjectName("label_word")
        self.label_word.setFont(font)
        self.gridLayout.addWidget(self.label_word, 2, 0, 1, 1)

        self.label_word2 = QtWidgets.QLabel(self.LearnWindow1)
        self.label_word2.setObjectName("label_word2")
        self.label_word2.setFont(font)
        self.gridLayout.addWidget(self.label_word2, 3, 0, 1, 1)

        self.label_word3 = QtWidgets.QLabel(self.LearnWindow1)
        self.label_word3.setObjectName("label_word3")
        self.label_word3.setFont(font)
        self.gridLayout.addWidget(self.label_word3, 4, 0, 1, 1)

        self.pushButton_check = QtWidgets.QPushButton(self.LearnWindow1)
        self.pushButton_check.setObjectName("pushButton_check")
        self.pushButton_check.clicked.connect(self.check_words)
        self.gridLayout.addWidget(self.pushButton_check, 5, 1, 1, 1)




        self.pushButton_score = QtWidgets.QPushButton(self.LearnWindow1)
        self.pushButton_score.setObjectName("pushButton_score")
        self.pushButton_score.clicked.connect(self.show_score)
        self.gridLayout.addWidget(self.pushButton_score, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.LearnWindow1)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.lineEdit_word1 = QtWidgets.QLineEdit(self.LearnWindow1)
        self.lineEdit_word1.setObjectName("lineEdit_word1")
        self.gridLayout.addWidget(self.lineEdit_word1, 2, 1, 1, 1)
        self.lineEdit_word_2 = QtWidgets.QLineEdit(self.LearnWindow1)
        self.lineEdit_word_2.setObjectName("lineEdit_word_2")
        self.gridLayout.addWidget(self.lineEdit_word_2, 3, 1, 1, 1)
        self.lineEdit_word_3 = QtWidgets.QLineEdit(self.LearnWindow1)
        self.lineEdit_word_3.setObjectName("lineEdit_word_3")
        self.gridLayout.addWidget(self.lineEdit_word_3, 4, 1, 1, 1)

        self.retranslateUi(self.LearnWindow1)
        QtCore.QMetaObject.connectSlotsByName(self.LearnWindow1)

        self.set_words()

    def retranslateUi(self, LearnWindow1):
        _translate = QtCore.QCoreApplication.translate
        self.LearnWindow1.setWindowTitle(_translate("LearnWindow1", "Dialog"))
        self.label.setText(_translate("LearnWindow1", "Linguenee"))
        self.label_word2.setText(_translate("LearnWindow1", "TextLabel"))
        self.pushButton_check.setText(_translate("LearnWindow1", "check"))
        self.label_word.setText(_translate("LearnWindow1", "Word"))
        self.label_word3.setText(_translate("LearnWindow1", "TextLabel"))
        self.pushButton_score.setText(_translate("LearnWindow1", "See scores"))
        start_text = "You are learing: " + self.SetName + "\nLeart it!"
        self.label_2.setText(_translate("LearnWindow", start_text))

    def check_words(self):
        try:
            add_to_score = 25
            list_len = 0
            while list_len < (len(self.file)):

                if self.file[list_len]== self.word_1:
                    if self.lineEdit_word1.text().lower() == self.file[list_len]["word"].lower():
                        self.file[list_len]["score"] += add_to_score
                        self.message_correct("Correct!  \n", self.file[list_len]["meaning"], self.lineEdit_word1.text(), self.file[list_len]["word"])
                    else:
                        self.file[list_len]["score"] += - 5
                        self.message_correct("Incorrect!:((  \n", self.file[list_len]["meaning"], self.lineEdit_word1.text(), self.file[list_len]["word"])

                elif self.file[list_len] == self.word_2:
                    if self.lineEdit_word_2.text().lower() == self.file[list_len]["word"].lower():
                        self.file[list_len]["score"] += add_to_score
                        self.message_correct("Correct!\n", self.file[list_len]["meaning"], self.lineEdit_word_2.text(), self.file[list_len]["word"])
                    else:
                        self.file[list_len]["score"] += -5
                        self.message_correct("Incorrect!:(( \n ", self.file[list_len]["meaning"], self.lineEdit_word_2.text(), self.file[list_len]["word"])

                elif self.file[list_len] == self.word_3:
                    if self.lineEdit_word_3.text().lower() == self.file[list_len]["word"].lower():
                        self.file[list_len]["score"] += add_to_score
                        self.message_correct("Correct!\n", self.file[list_len]["meaning"], self.lineEdit_word_3.text(), self.file[list_len]["word"])
                    else:
                        self.file[list_len]["score"] += -5
                        self.message_correct("InCorrect!:(((\n", self.file[list_len]["meaning"], self.lineEdit_word_3.text(), self.file[list_len]["word"])
                else:
                    pass
                list_len += 1
            passCreator.edit_user_learing_set(self.UserID, self.SetName, self.file)

            self.set_words()

        except Exception as err:
            print(err)
    def message_correct(self, msg, msg_text):
        print(msg)
        print(msg_text)
        print("\n")

    def set_words(self):
        self.generate_words()

        # Word 1
        self.label_word.setText(self.word_1["meaning"])
        self.lineEdit_word1.setText("")

        # Word 2
        self.label_word2.setText(self.word_2["meaning"])
        self.lineEdit_word_2.setText("")

        # Word 3
        self.label_word3.setText(self.word_3["meaning"])
        self.lineEdit_word_3.setText("")


    def generate_words(self):
        word_1 = random.choice(self.file)
        word_2 = random.choice(self.file)
        word_3 = random.choice(self.file)
        if len(self.file) > 3:
            if word_1 == word_2 or word_1 == word_3 or word_2 == word_3:
                word_1, word_2, word_3 = self.generate_words()
        self.word_1 = word_1
        self.word_2 = word_2
        self.word_3 = word_3

    def show_score(self):
        for f in self.file:
            print(f)

    def read_set(self):
        userDir = USERFILESDIR + "\\" + self.UserID + "\\u_sets"
        self.file = passCreator.open_list_file(userDir , self.SetName)

    def learned(self):
        for f in self.file:
            if f["score"] < 100:
                return(False)
        return(True)

    def message_correct(self, state, word_to_trans, answer, correct_answer):
        text = state
        text = text + "Word to translate:  " + word_to_trans
        text = text + "\n You have chosen:  " + answer
        text = text + "\n Correct answer:  " + correct_answer
        print(text, "\n")
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LearnWindow = QtWidgets.QDialog()
    ui = Ui_LearnWindow()
    ui.setupUi(LearnWindow, "","")
    LearnWindow.show()
    sys.exit(app.exec_())
"""
