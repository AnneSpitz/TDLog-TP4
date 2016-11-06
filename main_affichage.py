#!/usr/bin/python
# -*- coding: utf-8 -*-

# /////////////////////////////////////////////////////
#
# TP4 du module de Techniques de Développement LOGiciel
#
# Groupe 3
# TP réalisé par RIU Clément et SPITZ Anne
#
# /////////////////////////////////////////////////////


import sys
from PyQt4 import QtGui, QtCore
import pandas

import game
import customExceptions
import outils
import functools


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
        partie = game.Game(self.nom_joueur_1, self.nom_joueur_2, taille=self.taille_partie,
                           tableauValeurs=self.chargement_csv)
        if self.nombre_joueur == 1:
            isIAPresente = True
        else:
            isIAPresente = False
        self.Affichage_jeu = MyMainWindow(partie, isIAPresente)
        self.affichage_jeu()

    def affichage_jeu(self):
        self.Affichage_jeu.show()


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


class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, partie, isIAPresente, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self, partie, isIAPresente)
        self.setCentralWidget(self.form_widget)
        self.initUI()

    def initUI(self):
        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')


class FormWidget(QtGui.QWidget):
    def __init__(self, parent, partie, isIAPresente):
        super(FormWidget, self).__init__(parent)
        self.partie = partie
        self.isIAPresente = isIAPresente
        self.initButton()

    def initButton(self):
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        grille = self.partie.grilleJeu

        taille_grille = grille.getTaille()
        valeurs = [grille[(i, j)] for i in range(taille_grille) for j in range(taille_grille)]

        positions = [[i, j] for i in range(taille_grille) for j in range(taille_grille)]

        for position, valeur in zip(positions, valeurs):

            if isinstance(valeur, int):
                affichage = str(valeur)
            elif position == self.partie.positions:
                affichage = "###"
            else:
                affichage = "0"

            button = QtGui.QPushButton(affichage)
            fonction_push_1 = lambda direction: self.buttonClicked("")
            fonction_push_2 = functools.partial(fonction_push_1, "")

            button.clicked.connect(fonction_push_2)
            button.setEnabled(False)
            grid.addWidget(button, *position)

        texte_lateral = [self.partie.listeJoueurs[0].getNom(), "0",
                         self.partie.listeJoueurs[1].getNom(), "0"]
        for ligne in range(4):
            text_pour_score = QtGui.QLineEdit(self)
            text_pour_score.setReadOnly(True)
            text_pour_score.setText(texte_lateral[ligne])
            grid.addWidget(text_pour_score, ligne, taille_grille + 1)

        self.gestion_position_disponible()
        self.setGeometry(500, 500, 390, 350)

    def resultatPartie(self):
        """
        Affiche le résultat de la partie et renvoie les numéro des joueurs vainqueurs.
        :return: Renvoie la liste des indices des joueurs ayant gagnés.
        """

        # Récupération des données des joueurs.
        listeJoueurs = self.partie.listeJoueurs
        nombreJoueurs = len(listeJoueurs)
        scoreJoueurs = [listeJoueurs[numeroJoueur].getScore() for numeroJoueur in
                        range(nombreJoueurs)]
        nomJoueurs = [listeJoueurs[numeroJoueur].getNom() for numeroJoueur in
                      range(nombreJoueurs)]

        maximumEtIndice = outils.maxEtIndice(scoreJoueurs)
        scoreMaximal = maximumEtIndice[0]
        nombreGagnant = maximumEtIndice[1]
        listeGagnant = maximumEtIndice[2]

        # Affichage du ou des gagnants :
        if nombreGagnant == nombreJoueurs:
            texte = "Il y a une égalité ! Les joueurs ont {} points.".format(str(scoreMaximal))

        elif nombreGagnant == 1:
            texte = "{} a gagné ! Son score est de {} points.".format(nomJoueurs[listeGagnant[0]],
                                                                      scoreMaximal)
        else:
            nomGagnant = [nomJoueurs[indice] for indice in listeGagnant]
            texte = "Les joueurs {} ont gagné avec {} points !".format(nomGagnant, scoreMaximal)

        return texte

    def gestion_position_disponible(self):
        if self.partie.finPartie():
            self.parent().statusBar().showMessage(self.resultatPartie())

        positions = self.partie.positions

        deplacement_possible = {}
        for deplacement in game.directionAcceptable:
            if self.partie.isDirectionValide(deplacement):
                position_possible = tuple(
                    outils.add(positions, game.directionAcceptable[deplacement]))
                deplacement_possible[position_possible] = deplacement

        taille_grille = self.partie.grilleJeu.getTaille()

        for ligne in range(taille_grille):
            for colonne in range(taille_grille):
                valeur = self.partie.grilleJeu[(ligne, colonne)]
                if isinstance(valeur, int):
                    affichage = str(valeur)
                    style='QPushButton {background-color: #E8E8E8; color: black;}'
                elif [ligne, colonne] == self.partie.positions:
                    affichage = "###"
                    style='QPushButton {background-color: #71C5D1; color: black;}'
                else:
                    affichage = "0"
                    style='QPushButton {background-color: #F2F2F2; color: white;}'
                button_local = self.layout().itemAtPosition(ligne, colonne)
                button_local.widget().setParent(None)
                button_local = QtGui.QPushButton(affichage)
                button_local.setStyleSheet(style)
                fonction_push_1 = lambda direction: self.buttonClicked("")
                fonction_push_2 = functools.partial(fonction_push_1, "")

                button_local.clicked.connect(fonction_push_2)
                button_local.setEnabled(False)
                self.layout().addWidget(button_local, ligne, colonne)

                for deplacement in deplacement_possible:
                    direction_local = deplacement_possible[deplacement]
                    position_voulu = outils.add(positions,
                                                game.directionAcceptable[direction_local])
                    if [ligne, colonne] == position_voulu:
                        button_local = self.layout().itemAtPosition(ligne, colonne)
                        button_local.widget().setParent(None)
                        button_local = QtGui.QPushButton(
                            str(self.partie.grilleJeu[(ligne, colonne)]))
                        button_local.setStyleSheet('QPushButton {background-color: #D0D0D0; color: black;}')

                        direction = deplacement_possible[(ligne, colonne)]
                        fonction_push_1 = lambda direction: self.buttonClicked(direction)
                        fonction_push_2 = functools.partial(fonction_push_1, direction)

                        button_local.clicked.connect(fonction_push_2)
                        button_local.setEnabled(True)
                        self.layout().addWidget(button_local, ligne, colonne)

    def buttonClicked(self, direction):
        sender = self.sender()

        sender.setEnabled(False)
        sender.setText("0")

        self.partie.modifieEtat(direction)
        joueur_courant = (self.partie.joueurCourant + 1) % 2
        joueur = self.partie.listeJoueurs[joueur_courant]
        nom_joueur = joueur.getNom()
        score = joueur.getScore()
        text_score = self.layout().itemAtPosition(joueur_courant * 2 + 1,
                                                  self.partie.grilleJeu.getTaille() + 1)
        text_score.widget().setParent(None)

        text_score = QtGui.QLineEdit(self)
        text_score.setReadOnly(True)
        text_score.setText(str(score))
        self.layout().addWidget(text_score, joueur_courant * 2 + 1,
                                self.partie.grilleJeu.getTaille() + 1)

        joueur_courant = (self.partie.joueurCourant)
        joueur = self.partie.listeJoueurs[joueur_courant]
        nom_joueur = joueur.getNom()
        self.parent().statusBar().showMessage("À " + nom_joueur + " de jouer")
        # self.gestion_position_disponible()
        if self.isIAPresente and not self.partie.finPartie():
            self.parent().statusBar().showMessage(nom_joueur + " réfléchit")
            directionIA = self.partie.choixDirectionIA()
            print(directionIA)
            self.partie.modifieEtat(directionIA)
            joueur_courant = (self.partie.joueurCourant + 1) % 2
            joueur = self.partie.listeJoueurs[joueur_courant]
            nom_joueur = joueur.getNom()
            score = joueur.getScore()
            text_score = self.layout().itemAtPosition(joueur_courant * 2 + 1,
                                                      self.partie.grilleJeu.getTaille() + 1)
            text_score.widget().setParent(None)

            text_score = QtGui.QLineEdit(self)
            text_score.setReadOnly(True)
            text_score.setText(str(score))
            self.layout().addWidget(text_score, joueur_courant * 2 + 1,
                                    self.partie.grilleJeu.getTaille() + 1)

            joueur_courant = (self.partie.joueurCourant)
            joueur = self.partie.listeJoueurs[joueur_courant]
            nom_joueur = joueur.getNom()
            self.parent().statusBar().showMessage("À " + nom_joueur + " de jouer")
            self.gestion_position_disponible()
        else:
            self.gestion_position_disponible()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
