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
import outils


class Menu(QtGui.QWidget):
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

    def but_nombre_joueur(self):
        self.nombre_joueur = 0
        self.button_nombre_joueur = QtGui.QPushButton('Nombre de joueur', self)
        self.button_nombre_joueur.move(20, 20)
        self.button_nombre_joueur.clicked.connect(self.demande_nombre_joueur)

        self.text_nombre_joueur = QtGui.QLineEdit(self)
        self.text_nombre_joueur.setReadOnly(True)
        self.text_nombre_joueur.move(180, 22)

    def demande_nombre_joueur(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Nombre de joueur',
                                              'Nombre de joueur (1/2):')
        if text not in {"1", "2"}:
            ok = False
            self.text_nombre_joueur.setText("Entrer 1 ou 2 !")
        if ok:
            self.text_nombre_joueur.setText(text)
            self.button_nombre_joueur.setEnabled(False)
            self.nombre_joueur = int(text)

            self.button_nom_joueur_1.setEnabled(True)
            if self.nombre_joueur == 2:
                self.button_nom_joueur_2.setEnabled(True)

    def but_noms_joueurs(self):
        self.nom_joueur_1 = ""
        self.nom_joueur_2 = ""

        self.button_nom_joueur_1 = QtGui.QPushButton('Nom joueur 1', self)
        self.button_nom_joueur_1.move(20, 70)
        self.button_nom_joueur_1.setEnabled(False)
        self.button_nom_joueur_1.clicked.connect(self.demande_nom_joueur_1)

        self.text_nom_joueur_1 = QtGui.QLineEdit(self)
        self.text_nom_joueur_1.setReadOnly(True)
        self.text_nom_joueur_1.move(180, 72)

        self.button_nom_joueur_2 = QtGui.QPushButton('Nom joueur 2', self)
        self.button_nom_joueur_2.move(20, 110)
        self.button_nom_joueur_2.setEnabled(False)
        self.button_nom_joueur_2.clicked.connect(self.demande_nom_joueur_2)

        self.text_nom_joueur_2 = QtGui.QLineEdit(self)
        self.text_nom_joueur_2.setReadOnly(True)
        self.text_nom_joueur_2.move(180, 112)

    def demande_nom_joueur_1(self):

        text, ok = QtGui.QInputDialog.getText(self, 'Nom joueur',
                                              'Nom du joueur 1 :')
        if ok and text != "":
            self.button_nom_joueur_1.setEnabled(False)
            self.nom_joueur_1 = text
            self.text_nom_joueur_1.setText(text)

            if self.nombre_joueur == 1:
                self.nom_joueur_2 = "Glados"
                self.text_nom_joueur_2.setText(self.nom_joueur_2)

        if self.nom_joueur_1 != "" and self.nom_joueur_2 != "":
            self.button_chargement_csv.setEnabled(True)
            self.button_taille_partie.setEnabled(True)

    def demande_nom_joueur_2(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Nom joueur',
                                              'Nom du joueur 2 :')
        if ok and text != "":
            self.button_nom_joueur_2.setEnabled(False)
            self.nom_joueur_2 = text
            self.text_nom_joueur_2.setText(text)

        if self.nom_joueur_1 != "" and self.nom_joueur_2 != "":
            self.button_chargement_csv.setEnabled(True)
            self.button_taille_partie.setEnabled(True)

    def but_partie_aleat_chargee(self):
        self.chargement_csv = 0
        self.taille_partie = 0

        self.button_chargement_csv = QtGui.QPushButton('Charger un fichier', self)
        self.button_chargement_csv.move(20, 160)
        self.button_chargement_csv.setEnabled(False)
        self.button_chargement_csv.clicked.connect(self.cherche_fichier)

        self.text_chargement_csv = QtGui.QLineEdit(self)
        self.text_chargement_csv.setReadOnly(True)
        self.text_chargement_csv.move(180, 162)

        self.button_taille_partie = QtGui.QPushButton('Génération aléatoire', self)
        self.button_taille_partie.move(20, 200)
        self.button_taille_partie.setEnabled(False)
        self.button_taille_partie.clicked.connect(self.genere_aleatoire)

        self.text_taille_partie = QtGui.QLineEdit(self)
        self.text_taille_partie.setReadOnly(True)
        self.text_taille_partie.move(180, 202)

    def genere_aleatoire(self):
        self.button_chargement_csv.setEnabled(False)
        text, ok = QtGui.QInputDialog.getText(self, 'Génération aléatoire',
                                              'Taille de la grille ? (Entier impaire):')

        if ok:
            try:
                text_int = int(text)
            except ValueError:
                self.text_taille_partie.setText("Entier requis")
            else:
                if text_int % 2 == 1:
                    self.text_taille_partie.setText(text)
                    self.button_taille_partie.setEnabled(False)
                    self.button_debut_partie.setEnabled(True)
                    self.taille_partie = text_int

    def cherche_fichier(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Chargement fichier',
                                              'Entrer nom du fichier (sans extension):')

        if ok:
            text += ".csv"
            try:
                with open(text) as csvfile:

                    self.chargement_csv = pandas.read_csv(csvfile, delimiter=",", header=None)

            except FileNotFoundError:
                self.text_chargement_csv.setText("Fichier non trouvé")
            else:
                self.text_chargement_csv.setText(text)
                self.button_taille_partie.setEnabled(False)
                self.button_chargement_csv.setEnabled(False)
                self.button_debut_partie.setEnabled(True)



    def but_lance_partie(self):
        self.button_debut_partie = QtGui.QPushButton('LANCER LA PARTIE', self)
        self.button_debut_partie.setEnabled(False)
        self.button_debut_partie.move(100, 250)
        self.button_debut_partie.clicked.connect(self.lancement_partie)


    def lancement_partie(self):
        self.button_debut_partie.setEnabled(False)
        partie = game.Game(self.nom_joueur_1, self.nom_joueur_2,taille=self.taille_partie, tableauValeurs=self.chargement_csv)
        partie.affichage()
        if self.nombre_joueur == 1:
            isIAPresente = True
        else:
            isIAPresente = False

        #gestionJeu(partie, isIAPresente)



def gestionTour(partie, isIAPresente):
    """
    Va cherche la direction auprès du joueur (en demandant aux humains et en appelant
    choixDirectionIA pour l'IA). Puis modifie l'état de la partie.
    :param partie: (Game) Partie sur laquelle on travaille.
    :param isIAPresente: (bool) True s'il y a une IA dans la partie.
    :return: Rien.
    """

    # S'il y a une IA, et que c'est à elle de jouer, on appelle la choixDirectionIA.
    if isIAPresente and partie.joueurCourant == 1:
        print("{} refléchit...".format(partie.listeJoueurs[1].getNom()))
        direction = partie.choixDirectionIA()
    else:
        direction = partie.demandeDirection()
        # On demande la direction tant que celle-ci n'est pas valide.
        while partie.isDirectionNonValide(direction):
            direction = partie.demandeDirection()

    # Une fois qu'on a la direction on modifie l'état.
    partie.modifieEtat(direction)

    return None


def gestionJeu(partie, isIAPresente):
    """
    Va appeller gestionTour tant que la partie n'est pas finie, puis afficher le résultat via
    resultatPartie.
    :param partie: (Game) Partie sur laquelle on travaille.
    :param isIAPresente: (bool) True s'il y a une IA dans la partie.
    :return: Renvoie le return de resultatPartie.
    """

    while not partie.finPartie():
        gestionTour(partie, isIAPresente)
        partie.affichage()

    return partie.resultatPartie()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
