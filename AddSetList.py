# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem

from progData import *
import passCreator


class Ui_Dialog(object):
    """
    Adding already created set to your list of sets
    """
    def setupUi(self, Dialog, UserID):
        self.Dialog = Dialog
        self.UserID = UserID

        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(320, 450)
        self.gridLayout = QtWidgets.QGridLayout(self.Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_set_name = QtWidgets.QLabel(self.Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_set_name.setFont(font)
        self.label_set_name.setObjectName("label_set_name")
        self.gridLayout.addWidget(self.label_set_name, 2, 0, 1, 1)

        self.comboBox_sets = QtWidgets.QComboBox(self.Dialog)
        self.comboBox_sets.setObjectName("comboBox_sets")

        available_sets = passCreator.openSetsAvailable()

        self.comboBox_sets.addItems(available_sets)
        self.gridLayout.addWidget(self.comboBox_sets, 1, 0, 1, 2)

        self.label_Linguenee = QtWidgets.QLabel(self.Dialog)
        font = QtGui.QFont()
        font.setFamily("Harrington")
        font.setPointSize(14)
        self.label_Linguenee.setFont(font)
        self.label_Linguenee.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Linguenee.setObjectName("label_Linguenee")
        self.gridLayout.addWidget(self.label_Linguenee, 0, 0, 1, 3)

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.pushButton_show = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_show.setText("Show set")
        self.pushButton_show.clicked.connect(self.show_set)
        self.gridLayout.addWidget(self.pushButton_show, 1, 2, 1, 1)

        self.pushButton_close = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_close.clicked.connect(self.close_window)
        self.gridLayout.addWidget(self.pushButton_close, 4, 2, 1, 1)

        self.pushButton_add_set = QtWidgets.QPushButton(Dialog)
        self.pushButton_add_set.setObjectName("pushButton_add_set")
        self.pushButton_add_set.clicked.connect(self.add_set_to_your_list)
        self.gridLayout.addWidget(self.pushButton_add_set, 4, 1, 1, 1)

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_add_set.setText(_translate("Dialog", "Add set to you list"))
        self.label_Linguenee.setText(_translate("Dialog", "Linguenee"))
        self.pushButton_close.setText(_translate("Dialog", "Close"))

        self.label_set_name.setText(_translate("Dialog", "Name of the set"))

    def show_set(self):
        self.current_set_name = self.comboBox_sets.currentText()

        self.label_set_name.setText(self.current_set_name)
        try:
            self.insert_values_to_the_table()
        except Exception as err:
            print(err)


    def insert_values_to_the_table(self):
        self.rowCounts = 0
        word_list_set = passCreator.open_list_file(SETSDIR, self.current_set_name) # "Karaczan1"

        row_number = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_number)
        for row in word_list_set:
            self.rowCounts += 1
            self.tableWidget.setRowCount(self.rowCounts)
            self.tableWidget.setItem(self.rowCounts -1, 0,
                                    QTableWidgetItem(row["word"]))
            self.tableWidget.setItem(self.rowCounts -1, 1,
                                    QTableWidgetItem(row["meaning"]))

    def close_window(self):
        self.Dialog.close()

    def add_set_to_your_list(self):
        try:
            print(self.current_set_name)
            sets_in_use = passCreator.open_set_in_use(self.UserID)
            print(sets_in_use)
            if (self.current_set_name in sets_in_use) == False:
                passCreator.add_words2(self.UserID, self.current_set_name)
                passCreator.add_array_of_users(self.UserID, self.current_set_name)
                self.message("Added!", "Set has been added to your list!")
            else:
                self.message("Error!", "This set is already in your list!")
        except Exception as err:
            print("err:", err)
        # add modifiing set in user dir if set is chenged

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
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog, "Admin")
    Dialog.show()
    sys.exit(app.exec_())
"""
