from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from defin_recto2 import*
from tkinter import messagebox

class Ui_carte(QFileDialog):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(600, 828)
                MainWindow.setStyleSheet("background-color: rgb(15, 15, 15);")
                MainWindow.setWindowIcon(QtGui.QIcon(':/tout/png_of_recato/cadenaslogo.png'))
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.fond = QtWidgets.QLabel(self.centralwidget)
                self.fond.setGeometry(QtCore.QRect(0, 0, 600, 828))
                self.fond.setText("")
                self.fond.setPixmap(QtGui.QPixmap(":/tout/png_of_recato/carte csv.png"))
                self.fond.setObjectName("fond")
                self.undo = QtWidgets.QPushButton(self.centralwidget)
                self.undo.setGeometry(QtCore.QRect(546, 10, 39, 39))
                self.undo.setStyleSheet("QPushButton{\n"
                                        "background-image: url(:/tout/png_of_recato/undo.png);\n"
                                        "border-radius: 4px;\n"
                                        "border: none\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-image: url(:/tout/png_of_recato/hoveron/undo.png);\n"
                                        "border-radius: 4px;\n"
                                        "border: none\n"
                                        "}")
                self.undo.setText("")
                self.undo.setObjectName("undo")
                self.undo.clicked.connect(self.clicundo)
                self.savebutton = QtWidgets.QPushButton(self.centralwidget)
                self.savebutton.setGeometry(QtCore.QRect(500, 10, 39, 39))
                self.savebutton.setStyleSheet("QPushButton{\n"
                                              "background-image: url(:/tout/png_of_recato/save.png);\n"
                                              "border-radius: 4px;\n"
                                              "border: none;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "background-image: url(:/tout/png_of_recato/hoveron/save.png);\n"
                                              "border-radius: 4px;\n"
                                              "border: none;\n"
                                              "}")
                self.savebutton.setText("")
                self.savebutton.setObjectName("savebutton")
                self.savebutton.clicked.connect(self.save)
                self.titre_carte = QtWidgets.QLineEdit(self.centralwidget)
                self.titre_carte.setGeometry(QtCore.QRect(102, 8, 370, 51))
                font = QtGui.QFont()
                font.setFamily("Oxanium")
                font.setPointSize(30)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.titre_carte.setFont(font)
                self.titre_carte.setStyleSheet("background-color: rgb(37, 53, 74);\n"
"color: rgb(86, 126, 183);\n"
"font:57 30pt \"Outfit Medium\";\n")
                self.titre_carte.setAlignment(QtCore.Qt.AlignCenter)
                self.titre_carte.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
                self.titre_carte.setObjectName("titre_carte")
                self.pseudolabel = QtWidgets.QLabel(self.centralwidget)
                self.pseudolabel.setGeometry(QtCore.QRect(10, 88, 110, 35))
                self.pseudolabel.setStyleSheet("background-image: url(:/tout/png_of_recato/pseudo.png);")
                self.pseudolabel.setText("")
                self.pseudolabel.setObjectName("pseudolabel")
                self.pseudolineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.pseudolineEdit.setGeometry(QtCore.QRect(10, 138, 580, 50))
                self.pseudolineEdit.setStyleSheet("background-color: rgb(37, 53, 74);\n"
"color: rgb(217, 217, 217);\n"
"font:50 30pt \"Outfit Medium\";\n")
                self.pseudolineEdit.setObjectName("pseudolineEdit")
                self.emaillabel = QtWidgets.QLabel(self.centralwidget)
                self.emaillabel.setGeometry(QtCore.QRect(10, 218, 72, 35))
                self.emaillabel.setStyleSheet("background-image: url(:/tout/png_of_recato/email.png);")
                self.emaillabel.setText("")
                self.emaillabel.setObjectName("emaillabel")
                self.emaillineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.emaillineEdit.setGeometry(QtCore.QRect(10, 268, 580, 50))
                self.emaillineEdit.setStyleSheet("background-color: rgb(37, 53, 74);\n"
"color: rgb(217, 217, 217);\n"
"font:50 30pt \"Outfit Medium\";\n")
                self.emaillineEdit.setObjectName("emaillineEdit")
                self.passwordlabel = QtWidgets.QLabel(self.centralwidget)
                self.passwordlabel.setGeometry(QtCore.QRect(10, 348, 116, 35))
                self.passwordlabel.setStyleSheet("background-image: url(:/tout/png_of_recato/password.png);")
                self.passwordlabel.setText("")
                self.passwordlabel.setObjectName("passwordlabel")
                self.passwordlineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.passwordlineEdit.setGeometry(QtCore.QRect(10, 398, 580, 50))
                self.passwordlineEdit.setStyleSheet("background-color: rgb(37, 53, 74);\n"
"color: rgb(217, 217, 217);\n"
"font:50 30pt \"Outfit Medium\";\n")
                self.passwordlineEdit.setObjectName("passwordlineEdit")
                self.lienlabel = QtWidgets.QLabel(self.centralwidget)
                self.lienlabel.setGeometry(QtCore.QRect(10, 478, 72, 35))
                self.lienlabel.setStyleSheet("background-image: url(:/tout/png_of_recato/lien.png);")
                self.lienlabel.setText("")
                self.lienlabel.setObjectName("lienlabel")
                self.lienlineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.lienlineEdit.setGeometry(QtCore.QRect(10, 528, 580, 50))
                self.lienlineEdit.setStyleSheet("background-color: rgb(37, 53, 74);\n"
"color: rgb(217, 217, 217);\n"
"font:50 30pt \"Outfit Medium\";\n")
                self.lienlineEdit.setObjectName("lienlineEdit")
                self.infoslabel = QtWidgets.QLabel(self.centralwidget)
                self.infoslabel.setGeometry(QtCore.QRect(10, 608, 72, 35))
                self.infoslabel.setStyleSheet("background-image: url(:/tout/png_of_recato/infos.png);")
                self.infoslabel.setText("")
                self.infoslabel.setObjectName("infoslabel")
                self.infostextEdit = QtWidgets.QTextEdit(self.centralwidget)
                self.infostextEdit.setGeometry(QtCore.QRect(10, 658, 580, 150))
                self.infostextEdit.setStyleSheet("background-color: rgb(37, 53, 74);\n"
"color: rgb(217, 217, 217);\n"
"font:50 30pt \"Outfit Medium\";\n")
                self.infostextEdit.setObjectName("infostextEdit")
                self.ouvrirButton = QtWidgets.QPushButton(self.centralwidget)
                self.ouvrirButton.setGeometry(QtCore.QRect(135, 88, 196, 35))
                self.ouvrirButton.setStyleSheet("QPushButton{\n"
                                                "background-image: url(:/tout/png_of_recato/ouvrir_fichier.png);\n"
                                                "border: none\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "background-image: url(:/tout/png_of_recato/hoveron/ouvrir_fichier.png);\n"
                                                "border: none\n"
                                                "}")
                self.ouvrirButton.setText("")
                self.ouvrirButton.setObjectName("ouvrirButton")
                self.ouvrirButton.clicked.connect(self.browsefiles)
                self.fond.raise_()
                self.undo.raise_()
                self.savebutton.raise_()
                self.titre_carte.raise_()
                self.pseudolabel.raise_()
                self.pseudolineEdit.raise_()
                self.emaillabel.raise_()
                self.emaillineEdit.raise_()
                self.passwordlabel.raise_()
                self.passwordlineEdit.raise_()
                self.lienlabel.raise_()
                self.lienlineEdit.raise_()
                self.infoslabel.raise_()
                self.infostextEdit.raise_()
                self.ouvrirButton.raise_()
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def browsefiles(self):
                self.fname=QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(), ("*.png *.rct"))
                
                try:
                        self.carte = lire_csv_recto(self.fname[0])
                        self.pseudolineEdit.setText(self.carte[0])
                        self.emaillineEdit.setText(self.carte[1])
                        self.passwordlineEdit.setText(self.carte[2])
                        self.lienlineEdit.setText(self.carte[3])
                        self.infostextEdit.setText(self.carte[4])
                        self.titre_carte.setText((os.path.basename(self.fname[0])).split('.')[0])
                except TypeError:
                       messagebox.showwarning("Input Error", "This file is empty !")
                except :
                       messagebox.showwarning("Input Error", "Please choose a .PNG file !")
        def save(self):
                enregistrer_carte((self.titre_carte.text()),(self.pseudolineEdit.text()),
                                (self.emaillineEdit.text()),(self.passwordlineEdit.text()),
                                (self.lienlineEdit.text()),(self.infostextEdit.toPlainText()))
                exit()
        def clicundo(self):
                if self.titre_carte.text() == (os.path.basename(self.fname[0])).split('.')[0]:
                        self.pseudolineEdit.setText(self.carte[0])
                        self.emaillineEdit.setText(self.carte[1])
                        self.passwordlineEdit.setText(self.carte[2])
                        self.lienlineEdit.setText(self.carte[3])
                        self.infostextEdit.setText(self.carte[4])
                else:
                      messagebox.showwarning("Input Error", "Save your card before using the undo button") 
                
                
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "CATO PSW"))
import ressources_Cglobales_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_carte()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
