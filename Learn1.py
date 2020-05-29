# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from progData import *
import passCreator
import random

class Ui_LearnWindow(object):
    def setupUi(self, LearnWindow, UserID, SetName):
        self.UserID = UserID
        self.SetName = SetName
        self.read_set()

        self.LearnWindow = LearnWindow
        self.LearnWindow.setObjectName("LearnWindow")
        self.LearnWindow.resize(455, 274)
        self.gridLayout = QtWidgets.QGridLayout(self.LearnWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.LearnWindow)
        self.label.setMaximumSize(QtCore.QSize(16777215, 46))
        fontL = QtGui.QFont()
        fontL.setFamily(LOGOSTILE)
        fontL.setPointSize(18)
        self.label.setFont(fontL)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        font = QtGui.QFont()
        font.setPointSize(12)

        self.label_word = QtWidgets.QLabel(self.LearnWindow)
        self.label_word.setText("Hipo")
        self.label_word.setFont(font)
        self.gridLayout.addWidget(self.label_word, 2, 0, 1, 1)

        self.label_word2 = QtWidgets.QLabel(self.LearnWindow)
        self.label_word2.setText("Hipo")
        self.label_word2.setFont(font)
        self.gridLayout.addWidget(self.label_word2, 3, 0, 1, 1)

        self.label_word3 = QtWidgets.QLabel(self.LearnWindow)
        self.label_word3.setText("Hipo")
        self.label_word3.setFont(font)
        self.gridLayout.addWidget(self.label_word3, 4, 0, 1, 1)

        self.pushButton_check = QtWidgets.QPushButton(self.LearnWindow)
        self.pushButton_check.setObjectName("pushButton_check")
        self.pushButton_check.clicked.connect(self.check_words)
        self.gridLayout.addWidget(self.pushButton_check, 5, 1, 1, 1)

        self.comboBox_word3 = QtWidgets.QComboBox(self.LearnWindow)
        words3 = ["1","2", "3"]
        self.comboBox_word3.addItems(words3)
        self.comboBox_word3.setFont(font)
        self.gridLayout.addWidget(self.comboBox_word3, 4, 1, 1, 1)

        self.comboBox_word2 = QtWidgets.QComboBox(self.LearnWindow)
        words2 = ["1","2", "3"]
        self.comboBox_word2.addItems(words2)
        self.comboBox_word2.setFont(font)
        self.gridLayout.addWidget(self.comboBox_word2, 3, 1, 1, 1)

        self.comboBox_word1 = QtWidgets.QComboBox(self.LearnWindow)
        words1 = ["1","2", "3"]
        self.comboBox_word1.addItems(words1)
        self.comboBox_word1.setFont(font)
        self.gridLayout.addWidget(self.comboBox_word1, 2, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.LearnWindow)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.pushButton_score = QtWidgets.QPushButton(LearnWindow)
        self.pushButton_score.setObjectName("pushButton_score")
        self.pushButton_score.clicked.connect(self.show_score)
        self.gridLayout.addWidget(self.pushButton_score, 5, 0, 1, 1)

        self.retranslateUi(self.LearnWindow)
        QtCore.QMetaObject.connectSlotsByName(self.LearnWindow)

        self.set_words()


    def retranslateUi(self, LearnWindow):
        _translate = QtCore.QCoreApplication.translate
        self.LearnWindow.setWindowTitle(_translate("LearnWindow", "Dialog"))
        self.label.setText(_translate("LearnWindow", "Linguenee"))
        self.pushButton_check.setText(_translate("LearnWindow", "check"))
        start_text = "You are learing: " + self.SetName + "\nLeart it!"
        self.label_2.setText(_translate("LearnWindow", start_text))
        self.pushButton_score.setText(_translate("LearnWindow", "See scores"))

    def check_words(self):
        try:
            if self.finished():
                message_text = """Congratulations,\n You have finished this set.
                \n All socres will be 0, so you can learn this set again"""
                self.message("Congratulations!", message_text)
                self.reset_score()
            else:
                self.word_correct()
                self.set_words()

        except Exception as err:
            print("err: ", err)

    # checking if works are correct, if yes, write to set data
    def word_correct(self):
        add_to_score = 20
        list_len = 0
        while list_len < (len(self.file)):

            if self.file[list_len]== self.word_1:
                if self.comboBox_word1.currentText() == self.file[list_len]["word"]:
                    self.file[list_len]["score"] += add_to_score
                    self.message_correct("Correct!", self.file[list_len]["meaning"], self.comboBox_word1.currentText(), self.file[list_len]["word"])
                else:
                    self.file[list_len]["score"] += -5
                    self.message_correct("InCorrect!:(", self.file[list_len]["meaning"], self.comboBox_word1.currentText(), self.file[list_len]["word"])

            elif self.file[list_len] == self.word_2:
                if self.comboBox_word2.currentText() == self.file[list_len]["word"]:
                    self.file[list_len]["score"] += add_to_score
                    self.message_correct("Correct!", self.file[list_len]["meaning"], self.comboBox_word2.currentText(), self.file[list_len]["word"])
                else:
                    self.file[list_len]["score"] += -5
                    self.message_correct("InCorrect!:(", self.file[list_len]["meaning"], self.comboBox_word2.currentText(), self.file[list_len]["word"])

            elif self.file[list_len] == self.word_3:
                if self.comboBox_word3.currentText() == self.file[list_len]["word"]:
                    self.file[list_len]["score"] += add_to_score
                    self.message_correct("Correct!:)", self.file[list_len]["meaning"], self.comboBox_word3.currentText(), self.file[list_len]["word"])
                else:
                    self.file[list_len]["score"] += -5
                    self.message_correct("InCorrect!:(", self.file[list_len]["meaning"], self.comboBox_word3.currentText(), self.file[list_len]["word"])
            else:
                pass
            list_len += 1
        passCreator.edit_user_learing_set(self.UserID, self.SetName, self.file)
        print("\n      #################\n")
    # set word in window
    def set_words(self):
        self.word_1, self.word_2, self.word_3 = self.generate_words()

        # Word 1
        self.label_word.setText(self.word_1["meaning"])

        box_words_1 = self.generate_meanings()
        if self.word_1["word"] not in box_words_1:
            box_words_1[random.choice(range(0, 4))] = self.word_1["word"]
        self.comboBox_word1.clear()
        self.comboBox_word1.addItems(box_words_1)

        # Word 2
        self.label_word2.setText(self.word_2["meaning"])

        box_words_2 = self.generate_meanings()
        if self.word_2["meaning"] not in box_words_2:
            box_words_2[random.choice(range(0, 4))] = self.word_2["word"]
        self.comboBox_word2.clear()
        self.comboBox_word2.addItems(box_words_2)

        # Word 3
        self.label_word3.setText(self.word_3["meaning"])

        box_words_3 = self.generate_meanings()
        if self.word_3["word"] not in box_words_3:
            box_words_3[random.choice(range(0, 4))] = self.word_3["word"]
        self.comboBox_word3.clear()
        self.comboBox_word3.addItems(box_words_3)

    def generate_words(self):
        self.word_1 = random.choice(self.file)
        self.word_2 = random.choice(self.file)
        self.word_3 = random.choice(self.file)
        if len(self.file) > 3:
            if self.word_1 == self.word_2 or self.word_1 == self.word_3 or self.word_2 == self.word_3:
                self.word_1, self.word_2, self.word_3 = self.generate_words()
        return self.word_1, self.word_2, self.word_3

    def generate_meanings(self):
        meanings = []
        while len(meanings) < 4:
            meaning = random.choice(self.file)
            meaning = meaning["word"]
            if len(self.file) > 4:
                if meaning not in meanings:
                    meanings.append(meaning)
            else:
                meanings.append(meaning)
        return meanings

    def show_score(self):
        for f in self.file:
            print(f)

    def read_set(self):
        userDir = USERFILESDIR + "\\" + self.UserID + "\\u_sets"
        self.file = passCreator.open_list_file(userDir , self.SetName)

    def finished(self):
        for f in self.file:
            if f["score"] < 100:
                return(False)
        return(True)

    def reset_score(self):
        list_len = 0
        while list_len < (len(self.file)):
            self.file[list_len]["score"] = 0
            list_len +=1

    def message(self, msg, msg_text):
        self.NewUserMsg = QMessageBox()
        self.NewUserMsg.setIcon(QMessageBox.Information)
        self.NewUserMsg.setText(msg_text)
        self.NewUserMsg.setWindowTitle(msg)
        self.NewUserMsg.setStandardButtons(QMessageBox.Ok)
        returnValue = self.NewUserMsg.exec()

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
    ui.setupUi(LearnWindow, "Olek99", "Fruits")
    LearnWindow.show()
    sys.exit(app.exec_())
"""
