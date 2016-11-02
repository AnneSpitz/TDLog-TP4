#!/usr/bin/python
# -*- coding: utf-8 -*-

# /////////////////////////////////////////////////////
#
# TP3 du module de Techniques de Développement LOGiciel
#
# Groupe 3
# TP réalisé par RIU Clément et SPITZ Anne
#
# Rendu le 26 octobre 2016
#
# /////////////////////////////////////////////////////


import sys
from PyQt4 import QtGui, QtCore
import pandas

import game
import customExceptions

"""
class MyMainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        self.a = QtGui.QStatusBar(self)
        self.form_widget = Example(self)
        self.setCentralWidget(self.form_widget)


class Example(QtGui.QWidget):
    def __init__(self, parent):
        super(Example, self).__init__()

        #self.a = QtGui.QStatusBar(self)
        self.initUI()




    def initUI(self):

        grid = QtGui.QGridLayout()
        self.setLayout(grid)


        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QtGui.QPushButton(name)
            button.clicked.connect(self.buttonClicked)
            grid.addWidget(button, *position)
        #grid.addWidget(self.a)
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

    def buttonClicked(self,parent):

        sender = self.sender()
        self.a.showMessage(sender.text() + ' was pressed')
"""
"""
class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.setLayout(self.a)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QtGui.QPushButton(name)
            button.clicked.connect(self.buttonClicked)
            self.a.addWidget(button, *position)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('TRY HARD')
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')





        class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
"""
"""
def main():
    app = QtGui.QApplication(sys.argv)
    foo = MyMainWindow()
    ex = Example(foo)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


"""
"""
class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.setLayout(self.a)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QtGui.QPushButton(name)
            button.clicked.connect(self.buttonClicked)
            self.a.addWidget(button, *position)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('TRY HARD')
        self.show()"""


# class MyMainWindow(QtGui.QMainWindow):
#     def __init__(self, parent=None):
#         super(MyMainWindow, self).__init__(parent)
#         self.form_widget = FormWidget(self)
#         self.setCentralWidget(self.form_widget)
#         self.initUI()
#
#     def initUI(self):
#         # """
#         # btn1 = QtGui.QPushButton("Button 1", self)
#         # btn1.move(30, 50)
#         #
#         # btn2 = QtGui.QPushButton("Button 2", self)
#         # btn2.move(150, 50)
#         #
#         # btn1.clicked.connect(self.buttonClicked)
#         # btn2.clicked.connect(self.buttonClicked)
#         # """
#         self.statusBar()
#
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Event sender')
#         self.show()
#
#
#     def buttonClicked(self):
#         sender = self.sender()
#         self.statusBar().showMessage(sender.text() + ' was pressed')
#
#
#
# class FormWidget(QtGui.QWidget):
#     def __init__(self, parent):
#         super(FormWidget, self).__init__(parent)
#         #self.layout = QtGui.QVBoxLayout(self)
#         self.initButton(parent)
#
#     def initButton(self, parent):
#         grid = QtGui.QGridLayout()
#         self.setLayout(grid)
#
#
#         names = ['Cls', 'Bck', '', 'Close',
#                  '7', '8', '9', '/',
#                  '4', '5', '6', '*',
#                  '1', '2', '3', '-',
#                  '0', '.', '=', '+']
#
#         positions = [(i, j) for i in range(5) for j in range(4)]
#
#         for position, name in zip(positions, names):
#
#             if name == '':
#                 continue
#             button = QtGui.QPushButton(name)
#             button.clicked.connect(parent.buttonClicked)
#             grid.addWidget(button, *position)
#
#     #self.statusBar()
#
#         self.setGeometry(300, 300, 290, 150)
#
#
# def main():
#     app = QtGui.QApplication(sys.argv)
#     foo = MyMainWindow()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()





class Menu(QtGui.QWidget):
    # """
    # Demande le nombre de joueur et leur noms.
    # :return: une list contenant le nombre de joueur, et leur noms.
    # """
    #
    # nombreJoueur = 0
    #
    # # On demande un nombre de joueur entre 1 et 2.
    # while nombreJoueur not in {"1", "2"}:
    #     nombreJoueur = input("Partie à combien de joueurs ?\n1/2")
    #
    # if nombreJoueur == "1":
    #     nomJoueur1 = input("Comment vous appellez-vous ?\n")
    #     nomJoueur2 = "GLaDOS"  # Nom par défaut de l'IA.
    # else:
    #     nomJoueur1 = input("Nom du joueur 1 :\n")
    #     nomJoueur2 = input("Nom du joueur 2 :\n")
    #
    # return [nombreJoueur, nomJoueur1, nomJoueur2]
    def __init__(self):
        super(Menu, self).__init__()

        self.initUI()

    def initUI(self):
        self.but_nombre_joueur()

        self.but_noms_joueurs()

        self.but_partie_aleat_chargee()

        self.but_lance_partie()

        self.setGeometry(200, 200, 320, 300)
        self.setWindowTitle('Menu du jeu')
        self.show()

    def but_lance_partie(self):
        self.boutton_debut_partie = QtGui.QPushButton('LANCER LA PARTIE', self)
        self.boutton_debut_partie.setEnabled(False)
        self.boutton_debut_partie.move(100, 250)
        self.boutton_debut_partie.clicked.connect(self.lancement_partie)

    def lancement_partie(self):
        print("YAY")

    def but_nombre_joueur(self):
        self.nombre_joueur = 0
        self.boutton_nombre_joueur = QtGui.QPushButton('Nombre de joueur', self)
        self.boutton_nombre_joueur.move(20, 20)
        self.boutton_nombre_joueur.clicked.connect(self.demande_nombre_joueur)

        self.nombre = QtGui.QLineEdit(self)
        self.nombre.setReadOnly(True)
        self.nombre.move(180, 22)

    def but_noms_joueurs(self):
        self.nom_j1_ok = False
        self.nom_j2_ok = False

        self.boutton_nom_joueur_1 = QtGui.QPushButton('Nom joueur 1', self)
        self.boutton_nom_joueur_1.move(20, 70)
        self.boutton_nom_joueur_1.setEnabled(False)
        self.boutton_nom_joueur_1.clicked.connect(self.demande_nom_joueur_1)

        self.nom_joueur_1 = QtGui.QLineEdit(self)
        self.nom_joueur_1.setReadOnly(True)
        self.nom_joueur_1.move(180, 72)

        self.boutton_nom_joueur_2 = QtGui.QPushButton('Nom joueur 2', self)
        self.boutton_nom_joueur_2.move(20, 110)
        self.boutton_nom_joueur_2.setEnabled(False)
        self.boutton_nom_joueur_2.clicked.connect(self.demande_nom_joueur_2)

        self.nom_joueur_2 = QtGui.QLineEdit(self)
        self.nom_joueur_2.setReadOnly(True)
        self.nom_joueur_2.move(180, 112)

    def but_partie_aleat_chargee(self):
        self.boutton_chargement_csv = QtGui.QPushButton('Charger un fichier', self)
        self.boutton_chargement_csv.move(20, 160)
        self.boutton_chargement_csv.setEnabled(False)
        self.boutton_chargement_csv.clicked.connect(self.cherche_fichier)

        self.chargement_csv = QtGui.QLineEdit(self)
        self.chargement_csv.setReadOnly(True)
        self.chargement_csv.move(180, 162)

        self.boutton_taille_partie = QtGui.QPushButton('Génération aléatoire', self)
        self.boutton_taille_partie.move(20, 200)
        self.boutton_taille_partie.setEnabled(False)
        self.boutton_taille_partie.clicked.connect(self.genere_aleatoire)

        self.taille_partie= QtGui.QLineEdit(self)
        self.taille_partie.setReadOnly(True)
        self.taille_partie.move(180, 202)

    def genere_aleatoire(self):
        self.boutton_chargement_csv.setEnabled(False)
        text, ok = QtGui.QInputDialog.getText(self, 'Génération aléatoire',
                                              'Taille de la grille ? (Entier impaire):')

        if ok:
            try :
                text_int = int(text)
            except ValueError:
                self.taille_partie.setText("Entier requis")
            else:
                if text_int % 2 == 1:

                    self.taille_partie.setText(text)
                    self.boutton_taille_partie.setEnabled(False)
                    self.boutton_debut_partie.setEnabled(True)
                    self.taille = text_int


    def cherche_fichier(self):
        self.genere_aleatoire()

    def demande_nombre_joueur(self):

        text, ok = QtGui.QInputDialog.getText(self, 'Nombre de joueur',
                                              'Nombre de joueur (1/2):')
        if text not in {"1", "2"}:
            ok = False
            self.nombre.setText("Entrer 1 ou 2 !")
        if ok:
            self.nombre.setText(text)
            self.boutton_nombre_joueur.setEnabled(False)
            self.nombre_joueur = int(text)

            self.boutton_nom_joueur_1.setEnabled(True)
            if self.nombre_joueur == 2:
                self.boutton_nom_joueur_2.setEnabled(True)


    # def nom_joueur(self):
    #     if self.nombre_joueur == 1:
    #         self.bouton_joueur_1 = QtGui.QPushButton('Joueur 1', self)
    #         self.bouton_joueur_1.move(40, 20)
    #         self.bouton_joueur_1.clicked.connect(self.demande_nom_joueur)
    #
    def demande_nom_joueur_1(self):

        text, ok = QtGui.QInputDialog.getText(self, 'Nom joueur',
                                                  'Nom du joueur 1 :')
        if ok:

            self.boutton_nom_joueur_1.setEnabled(False)
            nom_joueur_1 = text
            self.nom_joueur_1.setText(nom_joueur_1)
            self.nom_j1_ok = True

        if self.nombre_joueur == 1:
            nom_joueur_2 = "Glados"
            self.nom_joueur_2.setText(nom_joueur_2)
            self.nom_j2_ok = True

        if self.nom_j1_ok and self.nom_j2_ok:
            self.boutton_chargement_csv.setEnabled(True)
            self.boutton_taille_partie.setEnabled(True)

    def demande_nom_joueur_2(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Nom joueur',
                                                  'Nom du joueur 2 :')
        if ok :
            self.boutton_nom_joueur_2.setEnabled(False)
            nom_joueur_2 = text
            self.nom_joueur_2.setText(nom_joueur_2)
            self.nom_j2_ok = True

        if self.nom_j1_ok and self.nom_j2_ok:
            self.boutton_chargement_csv.setEnabled(True)
            self.boutton_taille_partie.setEnabled(True)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
