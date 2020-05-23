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
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">RULES (In Polish Language)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">REGULAMIN APLIKACJI DO NAUKI JĘZYKA „Linguenee&quot; </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1 POSTANOWIENIA OGÓLNE </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.1 Niniejszy regulamin (dalej: „Regulamin”) określa zasady, warunki i zakres korzystania z aplikacji  Linguenee stanowi regulamin w rozumieniu art. 8 ustawy z dnia 18 lipca 2002 r. o świadczeniu usług drogą elektroniczną. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.2 Właścicielem i operatorem Aplikacji, a także usługodawcą świadczonych za jej pośrednictwem usług, są Estera Stachowiak i Oleksandr Khoroshevsyi. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.3 Użytkownikiem Aplikacji w rozumieniu Regulaminu jest osoba fizyczna, która poprzez Aplikację zainstalowaną na własnych urządzeniu mobilnym korzysta z oferowanych przez Aplikację funkcjonalności (dalej: „Użytkownik”). </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.4 Usługi świadczone za pośrednictwem Aplikacji polegają w szczególności na: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.4.1 umożliwieniu Użytkownikom nauki wybranego przez niego języka. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.4.2 umożliwieniu Użytkownikom przetestowania swoich umiejętności z wybranego przez Użytkownika materiału z danego języka. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.4.3 umożliwieniu Użytkownikom nauki wybranego przez niego języka. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.4.4 informowaniu Użytkowników o produktach i usługach Operatora oraz podmiotów trzecich. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.5 Aplikacja możliwa jest do pobrania z strony Github twórców </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.6 Z chwilą pobrania i zainstalowania Aplikacji na urządzeniu Użytkownika następuje zawarcie przez niego z Operatorem umowy o świadczenie usług drogą elektroniczną w ramach korzystania z Aplikacji, w tym szczególnie usług polegających na dostępie do funkcjonalności Urządzenia. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.7 Pobranie Aplikacji jak również korzystanie z oferowanych za jej pośrednictwem podstawowych usług jest bezpłatne. Twórca aplikacji dopuszcza możliwość wprowadzenia odpłatnych, dodatkowych funkcjonalności przy dokonywaniu kolejnych aktualizacji Aplikacji lub oprogramowania Urządzenia. Odpłatne funkcjonalności Urządzenia zostaną w sposób wyraźny oznaczone, tak, aby Użytkownik miał pełną wiedzę na temat wysokości kosztów poniesionych w związku z korzystaniem z odpłatnych funkcjonalności Urządzenia. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.8 Koszty transmisji danych wymaganych do pobrania, instalacji, uruchomienia i korzystania z Aplikacji pokrywają jej Użytkownicy we własnym zakresie, na podstawie umów zawartych z operatorami telekomunikacyjnymi lub innymi dostawcami usług internetowych. Użytkownik ponosi odpowiedzialność za jakąkolwiek odpłatność z tytułu wykorzystania transmisji danych, niezbędnego do korzystania z Aplikacji. Operator zaleca Użytkownikom Aplikacji korzystanie z aplikacji lub funkcji systemu operacyjnego polegających na pomiarze ilości przesyłanych danych. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.9 Aplikacja oraz wszelkie zawarte w niej materiały i informacje oraz układ prezentowych w ramach Aplikacji treści, a także logotypy, elementy graficzne i znaki towarowe, stanowią 2 przedmiot praw wyłącznych Operatora lub jego partnerów biznesowych i podlegają ochronie prawnej. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.REJESTRACJA UŻYTKOWNIKA </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.1 W trakcie pierwszego uruchomienia Urządzenia Użytkownik zobowiązany jest przejść proces rejestracji w Aplikacji, polegającej na założeniu indywidualnego konta Użytkownika (dalej: „Rejestracja”). </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.2 Do dokonania Rejestracji wymagane jest podanie przez Użytkownika następujących danych: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.3 imię; </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.4 nazwisko </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.5 login </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.6 hasło; </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.7 wiek; </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.8 płeć; </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.9 hasło; </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.10 powtórzone hasło; </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.11 potwierdzenie przez Użytkownika, że zapoznał się z Regulaminem i akceptuje jego treść. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.12 Użytkownikowi przysługuje prawo edytowania swoich danych podanych podczas Rejestracji oraz zmiany ustalonego podczas Rejestracji hasła. Edycja danych oraz zmiana hasła możliwa jest za pośrednictwem Aplikacji w zakładce Options -&gt; change user data w lewym górnym rogu okna użytkownika </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3ZASADY KORZYSTANIA Z APLIKACJI </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.1 Użytkownicy są zobowiązani do korzystania z Aplikacji w sposób zgodny z obowiązującym prawem, Regulaminem i regulaminami sklepów, z których Aplikacja została pobrana, a także z zasadami współżycia społecznego, w tym ogólnymi zasadami korzystania z sieci Internet i aplikacji mobilnych. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.2 Użytkownicy są zobowiązani w szczególności do: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.2.1 korzystania z Aplikacji i Urządzenia w sposób niezakłócający jej funkcjonowania; </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.2.2 korzystania z Aplikacji i Urządzenia w sposób nieuciążliwy dla innych użytkowników oraz Operatora, z poszanowaniem dóbr osobistych osób trzecich i wszelkich innych przysługującym im praw; </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.2.3 korzystania z wszelkich informacji i materiałów udostępnionych za pośrednictwem Aplikacji jedynie w zakresie dozwolonego użytku. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.3 Użytkownicy są zobowiązani niezwłocznie powiadomić Operatora o każdym przypadku naruszenia ich praw w związku z korzystaniem z Aplikacji. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">4 ZAKOŃCZENIE KORZYSTANIA Z APLIKACJI </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">4.1 Użytkownicy mogą w dowolnym czasie zaprzestać korzystania z Aplikacji, w szczególności wówczas, gdy nie zaakceptują zmian wprowadzonych w Regulaminie, Polityce Prywatności lub aktualizacji Aplikacji. Zaprzestanie korzystania z Aplikacji wymaga usunięcia swojego konta oraz aplikacji z urządzenia. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">5 POLITYKA PRYWATNOŚCI </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">5.1 Administratorem danych osobowych Użytkowników Aplikacji Estera Stachowiak oraz Oleksandr Khoroshevsyi oraz zapewniają wszystkim zarejestrowanym Użytkownikom realizację uprawnień wynikających z ustawy z dnia 29 sierpnia 1997 r. o ochronie danych osobowych, w szczególności prawo wglądu do własnych danych osobowych, prawo żądania aktualizacji i usunięcia danych osobowych oraz prawo wniesienia sprzeciwu w przypadkach określonych w przepisach tej ustawy. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">5.3 Dane osobowe zbierane są w celu umożliwienia Użytkownikom korzystania z Aplikacji. Dane osobowe Użytkowników mogą ponadto służyć do weryfikacji, czy osoba rejestrująca spełnia wymagane przez Regulamin i przepisy prawne warunki. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> 5.4 Podanie danych osobowych jest dobrowolne, jednak niezbędne do prawidłowego korzystania z Aplikacji. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> 6 POSTANOWIENIA KOŃCOWE </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">6.1 W sprawach nieuregulowanych w Regulaminie zastosowanie mają odpowiednie przepisy powszechnie obowiązującego prawa, w tym zwłaszcza Kodeksu cywilnego oraz ustawy o świadczeniu usług drogą elektroniczną. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">6.2 Regulamin dostępny jest za pośrednictwem Aplikacji. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">6.3 Regulamin obowiązuje od dnia 1.06.2020 roku. </span></p></body></html>"))

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
