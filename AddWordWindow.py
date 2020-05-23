# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from progData import *
import passCreator

class Ui_AddWords(object):
    """
    Class for adding new words to set
    """
    def setupUi(self, AddWords, setName):
        self.setName = setName
        self.AddWords = AddWords
        self.AddWords.setObjectName("AddWords")
        self.AddWords.resize(422, 560)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.AddWords)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.lineEdit_meaning = QtWidgets.QLineEdit(self.AddWords)
        self.lineEdit_meaning.setObjectName("lineEdit_meaning")
        self.gridLayout_2.addWidget(self.lineEdit_meaning, 5, 1, 1, 1)

        self.lineEdit_word = QtWidgets.QLineEdit(self.AddWords)
        self.lineEdit_word.setObjectName("lineEdit_word")
        self.gridLayout_2.addWidget(self.lineEdit_word, 5, 0, 1, 1)

        self.label_delete = QtWidgets.QLabel(self.AddWords)
        self.label_delete.setObjectName("label_delete")
        self.gridLayout_2.addWidget(self.label_delete, 6, 0, 1, 1)

        self.label_word_add = QtWidgets.QLabel(self.AddWords)
        self.label_word_add.setAlignment(QtCore.Qt.AlignCenter)
        self.label_word_add.setObjectName("label_word_add")
        self.gridLayout_2.addWidget(self.label_word_add, 4, 0, 1, 1)

        self.pushButton_add_word = QtWidgets.QPushButton(self.AddWords)
        self.pushButton_add_word.setObjectName("pushButton_add_word")
        self.pushButton_add_word.clicked.connect(self.add_word)
        self.gridLayout_2.addWidget(self.pushButton_add_word, 5, 2, 1, 1)

        self.labe_info = QtWidgets.QLabel(self.AddWords)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.labe_info.setFont(font)
        self.labe_info.setAlignment(QtCore.Qt.AlignCenter)
        self.labe_info.setObjectName("labe_info")
        self.gridLayout_2.addWidget(self.labe_info, 1, 0, 1, 3)

        self.pushButton_delete = QtWidgets.QPushButton(self.AddWords)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_delete.clicked.connect(self.delete_row)
        self.gridLayout_2.addWidget(self.pushButton_delete, 6, 1, 1, 1)

        self.label_linguenee = QtWidgets.QLabel(self.AddWords)
        font = QtGui.QFont()
        font.setFamily("Harrington")
        font.setPointSize(18)
        self.label_linguenee.setFont(font)
        self.label_linguenee.setAlignment(QtCore.Qt.AlignCenter)
        self.label_linguenee.setObjectName("label_linguenee")
        self.gridLayout_2.addWidget(self.label_linguenee, 0, 0, 1, 3)

        self.label_set_name = QtWidgets.QLabel(self.AddWords)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_set_name.setFont(font)
        self.label_set_name.setObjectName("label_set_name")
        self.gridLayout_2.addWidget(self.label_set_name, 2, 0, 1, 1)

        self.label_meaning_add = QtWidgets.QLabel(self.AddWords)
        self.label_meaning_add.setAlignment(QtCore.Qt.AlignCenter)
        self.label_meaning_add.setObjectName("label_meaning_add")
        self.gridLayout_2.addWidget(self.label_meaning_add, 4, 1, 1, 1)

        self.tableWidget = QtWidgets.QTableWidget(self.AddWords)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.insert_values_to_the_table()

        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableWidget, 3, 0, 1, 3)
        self.pushButton_Save = QtWidgets.QPushButton(self.AddWords)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.pushButton_Save.clicked.connect(self.seve_set)
        self.gridLayout_2.addWidget(self.pushButton_Save, 7, 1, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(self.AddWords)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout_2.addWidget(self.pushButton_cancel, 7, 2, 1, 1)

        self.retranslateUi(self.AddWords)
        QtCore.QMetaObject.connectSlotsByName(self.AddWords)

    def retranslateUi(self, AddWords):
        _translate = QtCore.QCoreApplication.translate
        self.AddWords.setWindowTitle(_translate("AddWords", "Dialog"))
        self.label_delete.setText(_translate("AddWords", "Delete selected_words:"))
        self.label_word_add.setText(_translate("AddWords", "Word"))
        self.pushButton_add_word.setText(_translate("AddWords", "Add"))
        self.labe_info.setText(_translate("AddWords", "Window for modifiing set"))
        self.pushButton_delete.setText(_translate("AddWords", "Delete"))
        self.label_linguenee.setText(_translate("AddWords", "Linguenee"))
        self.label_set_name.setText(_translate("AddWords", self.setName))
        self.label_meaning_add.setText(_translate("AddWords", "Meaning"))
        self.tableWidget.setSortingEnabled(True)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AddWords", "Word"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AddWords", "Meaning"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_Save.setText(_translate("AddWords", "Save"))
        self.pushButton_cancel.setText(_translate("AddWords", "Cancel"))

    def insert_values_to_the_table(self):
        self.rowCounts = 0
        word_list_set = passCreator.open_list_file(SETSDIR, self.setName)
        '''
        word_list_set = [{"word":10, "meaning": 11},
                        {"word":20, "meaning": 21},
                        {"word":'30dfghgfdsvbgfredfgbgfvgfd', "meaning": 31},
                        {"word": 40, "meaning": 41}]
        '''
        row_number = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_number)
        for row in word_list_set:
            print(row)
            self.rowCounts += 1
            self.tableWidget.setRowCount(self.rowCounts)
            self.tableWidget.setItem(self.rowCounts -1, 0,
                                    QTableWidgetItem(row["word"]))
            self.tableWidget.setItem(self.rowCounts -1, 1,
                                    QTableWidgetItem(row["meaning"]))

    def delete_row(self):
        try:
            row = self.tableWidget.selectedIndexes()
            if row:
                del_array = set()
                for i in row:
                    del_array.add(i.row())

                del_array = sorted(del_array, reverse=True)
                for delete in del_array:
                    print(delete)
                    self.tableWidget.removeRow(delete)
                    self.rowCounts -= 1
        except Exception as err:
            print(err)

    def add_word(self):
        try:
            new_word = self.lineEdit_word.text()
            new_meaning = self.lineEdit_meaning.text()
            print(new_word, new_meaning)
            self.rowCounts += 1

            self.tableWidget.setRowCount(self.rowCounts)
            self.tableWidget.setItem(self.rowCounts - 1, 0,
                                        QTableWidgetItem(new_word))
            self.tableWidget.setItem(self.rowCounts - 1, 1,
                                        QTableWidgetItem(new_meaning))
        except Exception as err:
            print(err)

    def seve_set(self):
        try:
            words_set = []
            for k in range(self.rowCounts):
                word ={"word": self.tableWidget.item(k, 0).text(),
                        "meaning": self.tableWidget.item(k, 1).text()
                        }
                words_set.append(word)
            passCreator.save_set(words_set, self.setName)

            # adding files with 0 scores to user file in learning
            dir = passCreator.directoryFind(SETSDIR)
            file_name = self.setName + '.info'
            users = passCreator.open_list_file(dir, file_name)
            print(users)
            print(words_set)
            for user in users:
                passCreator.add_words_user_use(user, self.setName, words_set)
                passCreator.add_words_user_test(user, self.setName, words_set)
                print(user)
                print(self.setName)
                print(words_set)

            self.message("Seved!", "Set has been seved!")
        except Exception as err:
            print(err)

    def message(self, msg, msg_text):
        self.NewUserMsg = QMessageBox()
        self.NewUserMsg.setIcon(QMessageBox.Information)
        self.NewUserMsg.setText(msg_text)
        self.NewUserMsg.setWindowTitle(msg)
        self.NewUserMsg.setStandardButtons(QMessageBox.Ok)
        returnValue = self.NewUserMsg.exec()

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(APPSTYLE)
    AddWords = QtWidgets.QDialog()
    ui = Ui_AddWords()
    ui.setupUi(AddWords, "Fruits")
    AddWords.show()
    sys.exit(app.exec_())
"""
