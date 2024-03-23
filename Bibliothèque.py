from PyQt5 import QtCore, QtGui, QtWidgets
from defin_recto2 import*
from tkinter import messagebox
from signin import Ui_account
from Bibliothèquecarte import Ui_carte

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 650)
        MainWindow.setStyleSheet("background-color: rgb(15, 15, 15);")
        MainWindow.setWindowIcon(QtGui.QIcon(':/tout/png_of_recato/cadenaslogo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.fond = QtWidgets.QLabel(self.centralwidget)
        self.fond.setGeometry(QtCore.QRect(0, 0, 1048, 650))
        self.fond.setStyleSheet("")
        self.fond.setText("")
        self.fond.setPixmap(QtGui.QPixmap(":/tout/png_of_recato/apreçu GENERATEUR.png"))
        self.fond.setObjectName("fond")
        self.to_generateur = QtWidgets.QPushButton(self.centralwidget)
        self.to_generateur.setGeometry(QtCore.QRect(649, 0, 60, 60))
        self.to_generateur.setStyleSheet("QPushButton{\n"
                                         "background-image: url(:/tout/png_of_recato/to generateur button.png);\n"
                                         "border : none;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-image: url(:/tout/png_of_recato/hoveron/to generateur button.png);\n"
                                         "border : none;\n"
                                         "}")
        self.to_generateur.setText("")
        self.to_generateur.setObjectName("to_generateur")
        self.to_generateur.clicked.connect(self.passergenerateur)
        self.to_generateur.setProperty('class','blackbordd')
        self.to_blibiotheque = QtWidgets.QPushButton(self.centralwidget)
        self.to_blibiotheque.setGeometry(QtCore.QRect(958, 590, 60, 60))
        self.to_blibiotheque.setStyleSheet("QPushButton{\n"
                                           "background-image: url(:/tout/png_of_recato/to bibliotheque button.png);\n"
                                           "border : none;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "background-image: url(:/tout/png_of_recato/hoveron/to bibliotheque button.png);\n"
                                           "border : none;\n"
                                           "}")
        self.to_blibiotheque.setText("")
        self.to_blibiotheque.setObjectName("to_blibiotheque")
        self.to_blibiotheque.clicked.connect(self.passerbibliotheque)
        self.to_blibiotheque.setProperty('class','blackbordd')
        self.accountbutton = QtWidgets.QPushButton(self.centralwidget)
        self.accountbutton.setGeometry(QtCore.QRect(520, 10, 100, 35))
        self.accountbutton.setStyleSheet("QPushButton{\n"
                                         "background-image: url(:/tout/png_of_recato/account.png);\n"
                                         "border : none;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-image: url(:/tout/png_of_recato/hoveron/account.png);\n"
                                         "border : none;\n"
                                         "}")
        self.accountbutton.setText("")
        self.accountbutton.setObjectName("accountbutton")
        self.accountbutton.clicked.connect(self.ouvrir_settings)
        #BIBLIOTHEQUE
        self.manipuler = QtWidgets.QPushButton(self.centralwidget)
        self.manipuler.setGeometry(QtCore.QRect(190, 310, 301, 50))
        self.manipuler.setStyleSheet("QPushButton{\n"
                                     "background-image: url(:/tout/png_of_recato/manipuler_carte.png);\n"
                                     "border : none;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-image: url(:/tout/png_of_recato/hoveron/manipuler_carte.png);\n"
                                     "border : none;\n"
                                     "}")
        self.manipuler.setText("")
        self.manipuler.setObjectName("manipuler")
        self.manipuler.clicked.connect(self.ouvrir_carte)
        #GENERATEUR
        self.genererlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.genererlineEdit.setGeometry(QtCore.QRect(181, 287, 416, 50))
        self.genererlineEdit.setStyleSheet("background-image: url(:/tout/png_of_recato/password case.png);\n"
                                        "color: rgb(217, 217, 217);\n"
                                        "font:50 30pt \"Outfit Medium\";\n"
                                        "border : none;")
        self.genererlineEdit.setObjectName("genererlineEdit")
        self.generer = QtWidgets.QPushButton(self.centralwidget)
        self.generer.setGeometry(QtCore.QRect(27, 287, 154, 50))
        self.generer.setStyleSheet("QPushButton{\n"
                                   "background-image: url(:/tout/png_of_recato/generer part.png);\n"
                                   "border-color: rgb(180, 179, 179);\n"
                                   "border : none\n;"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-image: url(:/tout/png_of_recato/hoveron/generer part.png);\n"
                                   "border-color: rgb(180, 179, 179);\n"
                                   "border : none;\n"
                                   "}")
        self.generer.setText("")
        self.generer.setObjectName("generer")
        self.generer.clicked.connect(self.clicgenerer)
        self.symboles = QtWidgets.QPushButton(self.centralwidget)
        self.symboles.setGeometry(QtCore.QRect(27, 536, 204, 50))
        self.symboles.setStyleSheet("QPushButton{\n"
                                    "background-image: url(:/tout/png_of_recato/symboles.png);\n"
                                    "border : none;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-image: url(:/tout/png_of_recato/hoveron/symboles.png);\n"
                                    "border : none;\n"
                                    "}\n")
        self.symboles.setText("")
        self.symboles.setObjectName("symboles")
        self.symboles.clicked.connect(self.clicsyb)
        self.nombres = QtWidgets.QPushButton(self.centralwidget)
        self.nombres.setGeometry(QtCore.QRect(27, 370, 204, 50))
        self.nombres.setStyleSheet("QPushButton{\n"
                                   "background-image: url(:/tout/png_of_recato/nombres part.png);\n"
                                   "border : none;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-image: url(:/tout/png_of_recato/hoveron/nombres part.png);\n"
                                   "border : none;\n"
                                   "}")
        self.nombres.setText("")
        self.nombres.setObjectName("nombres")
        self.nombres.clicked.connect(self.clicnomb)
        self.lettres = QtWidgets.QPushButton(self.centralwidget)
        self.lettres.setGeometry(QtCore.QRect(27, 453, 204, 50))
        self.lettres.setStyleSheet("QPushButton{\n"
                                   "background-image: url(:/tout/png_of_recato/lettres part.png);\n"
                                   "border : none;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-image: url(:/tout/png_of_recato/hoveron/lettres part.png);\n"
                                   "border : none;\n"
                                   "}")
        self.lettres.setText("")
        self.lettres.setObjectName("lettres")
        self.lettres.clicked.connect(self.cliclet)
        self.majuscule = QtWidgets.QPushButton(self.centralwidget)
        self.majuscule.setGeometry(QtCore.QRect(276, 370, 220, 50))
        self.majuscule.setStyleSheet("QPushButton{\n"
                                     "background-image: url(:/tout/png_of_recato/maj part.png);\n"
                                     "border : none;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-image: url(:/tout/png_of_recato/hoveron/maj part.png);\n"
                                     "border : none;\n"
                                     "}")
        self.majuscule.setText("")
        self.majuscule.setObjectName("majuscule")
        self.majuscule.clicked.connect(self.clicmaj)
        self.copy = QtWidgets.QPushButton(self.centralwidget)
        self.copy.setGeometry(QtCore.QRect(27, 234, 39, 39))
        self.copy.setStyleSheet("QPushButton{\n"
                                "background-image: url(:/tout/png_of_recato/copy.png);\n"
                                "border-radius: 4px;\n"
                                "border : none;\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "background-image: url(:/tout/png_of_recato/hoveron/copy.png);\n"
                                "border-radius: 4px;\n"
                                "border : none;\n"
                                "}")
        
        self.copy.setText("")
        self.copy.setObjectName("copy")
        self.copy.clicked.connect(self.cliccopy)
        self.undo = QtWidgets.QPushButton(self.centralwidget)
        self.undo.setGeometry(QtCore.QRect(78, 234, 39, 39))
        self.undo.setStyleSheet("QPushButton{\n"
                                "background-image: url(:/tout/png_of_recato/undo.png);\n"
                                "border-radius: 4px;\n"
                                "border : none;\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "background-image: url(:/tout/png_of_recato/hoveron/undo.png);\n"
                                "border-radius: 4px;\n"
                                "border : none;\n"
                                "}")
        self.undo.setText("")
        self.undo.setObjectName("undo")
        self.undo.clicked.connect(self.clicundo)
        self.cara = QtWidgets.QLabel(self.centralwidget)
        self.cara.setGeometry(QtCore.QRect(276, 453, 226, 50))
        self.cara.setStyleSheet("QLabel{\n"
                                "background-image: url(:/tout/png_of_recato/cara.png);\n"
                                "border : none;\n"
                                "}")
        self.cara.setText("")
        self.cara.setObjectName("cara")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(444, 453, 70, 50))
        self.spinBox.setStyleSheet("QSpinBox{\n"
                                   "background-color: rgb(52, 75, 107);\n"
                                   "color: rgb(217, 217, 217);\n"
                                   "font:50 30pt \"Outfit Medium\";\n"
                                   "border : none;\n"
                                   "}")
        self.spinBox.setValue(5)
        self.spinBox.setObjectName("spinBox")
        self.croixn = QtWidgets.QPushButton(self.centralwidget)
        self.croixn.setGeometry(QtCore.QRect(184, 373, 44, 44))
        self.croixn.setStyleSheet("QPushButton{\n"
                                  "background-image: url(:/tout/png_of_recato/checked nombres.png);\n"
                                  "background-color: rgb(52, 75, 107);\n"
                                  "border : none;\n"
                                  "}")
        self.croixn.setText("")
        self.croixn.setObjectName("croixn")
        self.croixn.clicked.connect(self.clicnomb)
        self.croixs = QtWidgets.QPushButton(self.centralwidget)
        self.croixs.setGeometry(QtCore.QRect(184, 539, 44, 44))
        self.croixs.setStyleSheet("QPushButton{\n"
                                  "background-image: url(:/tout/png_of_recato/checked nombres.png);\n"
                                  "background-color: rgb(52, 75, 107);\n"
                                  "border : none;\n"
                                  "}")
        self.croixs.setText("")
        self.croixs.setObjectName("croixs")
        self.croixs.clicked.connect(self.clicsyb)
        self.croixl = QtWidgets.QPushButton(self.centralwidget)
        self.croixl.setGeometry(QtCore.QRect(184, 456, 44, 44))
        self.croixl.setStyleSheet("QPushButton{\n"
                                  "background-image: url(:/tout/png_of_recato/checked nombres.png);\n"
                                  "background-color: rgb(52, 75, 107);\n"
                                  "border : none;\n"
                                  "}")
        self.croixl.setText("")
        self.croixl.setObjectName("croixl")
        self.croixl.clicked.connect(self.cliclet)
        self.croixm = QtWidgets.QPushButton(self.centralwidget)
        self.croixm.setGeometry(QtCore.QRect(449, 373, 44, 44))
        self.croixm.setStyleSheet("QPushButton{\n"
                                  "background-image: url(:/tout/png_of_recato/checked nombres.png);\n"
                                  "background-color: rgb(52, 75, 107);\n"
                                  "border : none;\n"
                                  "}")
        self.croixm.setText("")
        self.croixm.setObjectName("croixl")
        self.croixm.clicked.connect(self.clicmaj)
        self.code_bar = QtWidgets.QLabel(self.centralwidget)
        self.code_bar.setGeometry(QtCore.QRect(186, 271, 0, 13))
        self.code_bar.setStyleSheet("background-image: url(:/tout/png_of_recato/code bar.png);\n"
                                  "background-color: rgb(52, 75, 107);\n"
                                  "border : none;")
        self.code_bar.setText("")
        self.code_bar.setObjectName("code_bar")
        self.a=(-2)
        self.memo=[]
        self.cara.hide()
        self.majuscule.hide()
        self.spinBox.hide()
        self.genererlineEdit.hide()
        self.generer.hide()
        self.symboles.hide()
        self.nombres.hide()
        self.lettres.hide()
        self.copy.hide()
        self.undo.hide()
        self.croixn.hide()
        self.croixs.hide()
        self.croixl.hide()
        self.croixm.hide()
        self.code_bar.hide()
        self.maj = True
        self.let = True
        self.syb = True
        self.nomb = True
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def ouvrir_carte(self):
        self.window = QtWidgets.QMainWindow()
        self.ui= Ui_carte()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def ouvrir_settings(self):
        self.window = QtWidgets.QMainWindow()
        self.ui= Ui_account()
        self.ui.setupUi(self.window)
        self.window.show()

    def passergenerateur(self):
        self.genererlineEdit.show()
        self.generer.show()
        self.symboles.show()
        self.nombres.show()
        self.lettres.show()
        self.copy.show()
        self.undo.show()
        self.croixn.show()
        self.croixs.show()
        self.croixl.show()
        self.croixm.show()
        self.code_bar.show()
        self.cara.show()
        self.majuscule.show()
        self.spinBox.show()
        self.manipuler.hide()

    def passerbibliotheque(self):
        self.genererlineEdit.hide()
        self.generer.hide()
        self.symboles.hide()
        self.nombres.hide()
        self.lettres.hide()
        self.copy.hide()
        self.undo.hide()
        self.croixn.hide()
        self.croixs.hide()
        self.croixl.hide()
        self.croixm.hide()
        self.code_bar.hide()
        self.cara.hide()
        self.majuscule.hide()
        self.spinBox.hide()
        self.manipuler.show()

    def clicmaj(self):
        if self.croixm.isHidden() == True:
            self.croixm.show()
        else:
            self.croixm.hide()
        if self.maj is True:
            self.maj=False
        else:
            self.maj=True

    def clicsyb(self):
        if self.croixs.isHidden() == True:
            self.croixs.show()
        else:
            self.croixs.hide()
        if self.syb is True:
            self.syb=False
        else:
            self.syb=True

    def cliclet(self):
        if self.croixl.isHidden() == True:
            self.croixl.show()
        else:
            self.croixl.hide()
        if self.let is True:
            self.let=False
        else:
            self.let=True

    def clicnomb(self):
        if self.croixn.isHidden() == True:
            self.croixn.show()
        else:
            self.croixn.hide()
        if self.nomb is True:
            self.nomb=False
        else:
            self.nomb=True

    def clicgenerer(self):
        if (self.syb==True) or (self.nomb==True) or (self.let==True) or (self.maj==True):
            self.genererlineEdit.setText(passworde(self.spinBox.value(),self.syb,self.nomb,self.let,self.maj))
            try:
                self.taille=int(412*(score(self.genererlineEdit.text())))
                if self.taille > 452:
                    self.code_bar.setGeometry(QtCore.QRect(186, 271, 452, 13))
                else:
                    self.code_bar.setGeometry(QtCore.QRect(186, 271, self.taille, 13))
            except IndexError:
                messagebox.showwarning("Input Error", "Please choose a character number !")
            if self.a < (-2):
                self.memo.clear()
            self.memo.append(self.genererlineEdit.text())
            self.a=(-2)
        else :
            messagebox.showwarning("Input Error", "Please choose at least one option !")

    def cliccopy(self):
        cb =  QtWidgets.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.genererlineEdit.text(), mode=cb.Clipboard)

    def clicundo(self):
        try:
            self.genererlineEdit.setText(self.memo[self.a])
            self.a += (-1)
            self.taille=int(412*(score(self.genererlineEdit.text())))
            self.code_bar.setGeometry(QtCore.QRect(186, 271, self.taille, 13))
        except:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CATO PSW"))

import ressources_Cglobales_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
