# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(563, 438)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 543, 377))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">HELP:</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Okno rejestracji/logowania</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Do dokonania logowania wymagane jest podanie przez Użytkownika następujących danych: login i hasło, następnie kliknięcie przycisku “zaloguj” </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Nowy użytkownik może zostać zarejestrowany poprzez kliknięcie przycisku ”new user”, który automatycznie przekieruje go do okna rejestracji. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Po skończonej nauce użytkownik może wylogować się z aplikacji klikając przycisk log out w prawym dolnym rogu okna użytkownika. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Użytkownik ma możliwość zmienić swoje dane po wejściu w opcję ”Change user data” w lewym górnym rogu okna użytkownika. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Rejestracja </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Do dokonania Rejestracji wymagane jest podanie przez Użytkownika następujących danych: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">imię; nazwisko; login; hasło; wiek; płeć; hasło; powtórzone hasło; potwierdzenie przez Użytkownika, że zapoznał się z Regulaminem i akceptuje jego treść. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Hasło musi zawierać co najmniej 5 niepowtarzających się symboli, o czym jest informowany w momencie wpisania błędnego schematycznie hasła. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Użytkownikowi przysługuje prawo edytowania swoich danych podanych podczas Rejestracji oraz zmiany ustalonego podczas Rejestracji hasła. Edycja danych oraz zmiana hasła możliwa jest za pośrednictwem Aplikacji w zakładce Options -&gt; change user data w lewym górnym rogu okna użytkownika </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Okno zalogowanego użytkownika</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Użytkownik ma możliwość stworzenia nowego zestawu słów, modyfikacji oraz przystąpienia do nauki słów a następnie rozwiązania testu. Okno Achievements przedstawia postępy w nauce użytkownika: Ile zestawów zostało stworzonych, ile zakończonych a ilu nadal się uczy. To samo tyczy się odbytych testów wraz z procentowym wskaźnikiem ile materiału zostało zrealizowane. Okno ”new set” pozwala stworzyć nowy zestaw słów w wybranym języku. Po stworzeniu zestawu jest mozliwość jego modyfikacji, czyli dodania własnych lub gotowych słów wraz z tłumaczeniem. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Opcja nauki jak i testu</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pozwala Użytkownikowi na wybór zestawu oraz trybu przeprowadzenia nauki lub testu. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Okno modyfikacji zestawu słów</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Użytkownik po stworzeniu zestawu słów (jako pustej bazy) nadając jej język i nazwę, przechodzi do okna modyfikacja zestawu w celu dodania słów oraz ich tłumaczenia. Tak stworzony zestaw może wrzucić w tryb nauki lub testu. </span></p></body></html>"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""
