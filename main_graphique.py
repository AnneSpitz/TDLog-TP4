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


class OutilsGraphique():
    @staticmethod
    def creeBouton(entite, nom, position_x, position_y, fonction, isEnabled=True):
        boutonCree = QtGui.QPushButton(nom, entite)
        boutonCree.move(position_x, position_y)
        boutonCree.clicked.connect(fonction)

        boutonCree.setEnabled(isEnabled)

        return boutonCree

    @staticmethod
    def creeZoneTexte(entite, position_x, position_y, readOnly=True):
        zoneTexte = QtGui.QLineEdit(entite)
        zoneTexte.setReadOnly(readOnly)
        zoneTexte.move(position_x, position_y)

        return zoneTexte


class Menu(QtGui.QWidget):
    def __init__(self):
        super(Menu, self).__init__()

        self.initUI()

    def initUI(self):
        self.creeBoutonNombreJoueur()

        self.creeBoutonsJoueurs()

        self.creeBoutonsAleatoire_CSV()

        self.creeBoutonLancementPartie()

        self.setGeometry(200, 200, 320, 300)
        self.setWindowTitle('Menu du jeu')
        self.show()

    def creeBoutonNombreJoueur(self):
        self.nombreJoueur = 0

        self.boutonNombreJoueurs=OutilsGraphique.creeBouton(self, 'Nombre de joueurs', 20, 20, self.demandeNombreJoueurs)

        self.texteNombreJoueurs = OutilsGraphique.creeZoneTexte(self, 180, 22)


    def demandeNombreJoueurs(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Nombre de joueur',
                                              'Nombre de joueur (1/2):')
        if text not in {"1", "2"}:
            ok = False
            self.texteNombreJoueurs.setText("Entrer 1 ou 2 !")
        if ok:
            self.texteNombreJoueurs.setText(text)
            self.boutonNombreJoueurs.setEnabled(False)
            self.nombreJoueur = int(text)

            self.boutonNomJoueur1.setEnabled(True)
            if self.nombreJoueur == 2:
                self.boutonNomJoueur2.setEnabled(True)

    def creeBoutonsJoueurs(self):
        self.nomJoueur1 = ""
        self.nomJoueur2 = ""

        self.boutonNomJoueur1 = OutilsGraphique.creeBouton(self, 'Nom joueur 1', 20, 70,
                                   self.demandeNomJoueur1, isEnabled=False)
        self.texteNomJoueur1 = OutilsGraphique.creeZoneTexte(self, 180, 72)

        self.boutonNomJoueur2 = OutilsGraphique.creeBouton(self, 'Nom joueur 2', 20, 110,
                                    self.demandeNomJoueur2,isEnabled=False)
        self.texteNomJoueur2 = OutilsGraphique.creeZoneTexte(self, 180, 112)


    def demandeNomJoueur1(self):

        text, ok = QtGui.QInputDialog.getText(self, 'Nom joueur',
                                              'Nom du joueur 1 :')
        if ok and text != "":
            self.boutonNomJoueur1.setEnabled(False)
            self.nomJoueur1 = text
            self.texteNomJoueur1.setText(text)

            if self.nombreJoueur == 1:
                self.nomJoueur2 = "Glados"
                self.texteNomJoueur2.setText(self.nomJoueur2)

        if self.nomJoueur1 != "" and self.nomJoueur2 != "":
            self.boutonChargementCSV.setEnabled(True)
            self.boutonTaillePartie.setEnabled(True)

    def demandeNomJoueur2(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Nom joueur',
                                              'Nom du joueur 2 :')
        if ok and text != "":
            self.boutonNomJoueur2.setEnabled(False)
            self.nomJoueur2 = text
            self.texteNomJoueur2.setText(text)

        if self.nomJoueur1 != "" and self.nomJoueur2 != "":
            self.boutonChargementCSV.setEnabled(True)
            self.boutonTaillePartie.setEnabled(True)

    def creeBoutonsAleatoire_CSV(self):
        self.chargementCSV = 0
        self.taillePartie = 0

        self.boutonChargementCSV = OutilsGraphique.creeBouton(self, 'Charger un fichier', 20, 160,
                                        self.chercheFichier, isEnabled=False)
        self.textChargementCSV = OutilsGraphique.creeZoneTexte(self, 180, 162)

        self.boutonTaillePartie = OutilsGraphique.creeBouton(self, 'Génération aléatoire', 20,
                                    200, self.generePartieAleatoire, isEnabled=False)
        self.texteTaillePartie = OutilsGraphique.creeZoneTexte(self, 180, 202)


    def generePartieAleatoire(self):
        self.boutonChargementCSV.setEnabled(False)
        reponse, ok = QtGui.QInputDialog.getText(self, 'Génération aléatoire',
                                              'Taille de la grille ? (Entier impaire):')

        if ok:
            try:
                reponseInt = int(reponse)
            except ValueError:
                self.texteTaillePartie.setText("Entier requis")
            else:
                if reponseInt % 2 == 1:
                    self.texteTaillePartie.setText(reponse)
                    self.boutonTaillePartie.setEnabled(False)
                    self.boutonDebutPartie.setEnabled(True)
                    self.taillePartie = reponseInt

    def chercheFichier(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Chargement fichier',
                                              'Entrer nom du fichier (sans extension):')

        if ok:
            text += ".csv"
            try:
                with open(text) as csvfile:

                    self.chargementCSV = pandas.readCSV(csvfile, delimiter=",", header=None)

            except FileNotFoundError:
                self.textChargementCSV.setText("Fichier non trouvé")
            else:
                self.textChargementCSV.setText(text)
                self.boutonTaillePartie.setEnabled(False)
                self.boutonChargementCSV.setEnabled(False)
                self.boutonDebutPartie.setEnabled(True)


    def creeBoutonLancementPartie(self):
        self.boutonDebutPartie = OutilsGraphique.creeBouton(self, 'LANCER LA PARTIE', 100,
                                    250, self.lancementPartie, isEnabled=False)
        

    def lancementPartie(self):
        self.boutonDebutPartie.setEnabled(False)
        partie = game.Game(self.nomJoueur1, self.nomJoueur2, taille=self.taillePartie,
                           tableauValeurs=self.chargementCSV)
        if self.nombreJoueur == 1:
            isIAPresente = True
        else:
            isIAPresente = False
        self.AffichageJeu = MyMainWindow(partie, isIAPresente)
        self.affichageJeu()

    def affichageJeu(self):
        self.AffichageJeu.show()


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
        self.formWidget = FormWidget(self, partie, isIAPresente)
        self.setCentralWidget(self.formWidget)
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

        tailleGrille = grille.getTaille()
        valeurs = [grille[(i, j)] for i in range(tailleGrille) for j in range(tailleGrille)]

        positions = [[i, j] for i in range(tailleGrille) for j in range(tailleGrille)]

        for position, valeur in zip(positions, valeurs):

            if isinstance(valeur, int):
                affichage = str(valeur)
            elif position == self.partie.positions:
                affichage = "###"
            else:
                affichage = "0"

            button = QtGui.QPushButton(affichage)
            fonctionPush1 = lambda direction: self.buttonClicked("")
            fonctionPush2 = functools.partial(fonctionPush1, "")

            button.clicked.connect(fonctionPush2)
            button.setEnabled(False)
            grid.addWidget(button, *position)

        texteLateral = [self.partie.listeJoueurs[0].getNom(), "0",
                         self.partie.listeJoueurs[1].getNom(), "0"]
        for ligne in range(4):
            texteScore = QtGui.QLineEdit(self)
            texteScore.setReadOnly(True)
            texteScore.setText(texteLateral[ligne])
            grid.addWidget(texteScore, ligne, tailleGrille + 1)

        self.gestionPositionDisponible()
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

        maximumEtIndice = outils.Outils.maxEtIndice(scoreJoueurs)
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

    def gestionPositionDisponible(self):
        if self.partie.finPartie():
            self.parent().statusBar().showMessage(self.resultatPartie())

        positions = self.partie.positions

        deplacementPossible = {}
        for deplacement in game.directionAcceptable:
            if self.partie.isDirectionValide(deplacement):
                positionPossible = tuple(
                    outils.Outils.add(positions, game.directionAcceptable[deplacement]))
                deplacementPossible[positionPossible] = deplacement

        tailleGrille = self.partie.grilleJeu.getTaille()

        for ligne in range(tailleGrille):
            for colonne in range(tailleGrille):
                valeur = self.partie.grilleJeu[(ligne, colonne)]
                if isinstance(valeur, int):
                    affichage = str(valeur)
                    style = 'QPushButton {background-color: #E8E8E8; color: black;}'
                elif [ligne, colonne] == self.partie.positions:
                    affichage = "###"
                    style = 'QPushButton {background-color: #71C5D1; color: black;}'
                else:
                    affichage = "0"
                    style = 'QPushButton {background-color: #F2F2F2; color: white;}'
                boutonLocal = self.layout().itemAtPosition(ligne, colonne)
                boutonLocal.widget().setParent(None)
                boutonLocal = QtGui.QPushButton(affichage)
                boutonLocal.setStyleSheet(style)
                fonctionPush1 = lambda direction: self.buttonClicked("")
                fonctionPush2 = functools.partial(fonctionPush1, "")

                boutonLocal.clicked.connect(fonctionPush2)
                boutonLocal.setEnabled(False)
                self.layout().addWidget(boutonLocal, ligne, colonne)

                for deplacement in deplacementPossible:
                    directionLocale = deplacementPossible[deplacement]
                    positionVoulue = outils.Outils.add(positions,
                                                game.directionAcceptable[directionLocale])
                    if [ligne, colonne] == positionVoulue:
                        boutonLocal = self.layout().itemAtPosition(ligne, colonne)
                        boutonLocal.widget().setParent(None)
                        boutonLocal = QtGui.QPushButton(
                            str(self.partie.grilleJeu[(ligne, colonne)]))
                        boutonLocal.setStyleSheet('QPushButton {background-color: #D0D0D0; color: black;}')

                        direction = deplacementPossible[(ligne, colonne)]
                        fonctionPush1 = lambda direction: self.buttonClicked(direction)
                        fonctionPush2 = functools.partial(fonctionPush1, direction)

                        boutonLocal.clicked.connect(fonctionPush2)
                        boutonLocal.setEnabled(True)
                        self.layout().addWidget(boutonLocal, ligne, colonne)

    def buttonClicked(self, direction):
        sender = self.sender()

        sender.setEnabled(False)
        sender.setText("0")

        self.partie.modifieEtat(direction)
        joueurCourant = (self.partie.joueurCourant + 1) % 2
        joueur = self.partie.listeJoueurs[joueurCourant]
        nomJoueur = joueur.getNom()
        score = joueur.getScore()
        texteScore = self.layout().itemAtPosition(joueurCourant * 2 + 1,
                                                  self.partie.grilleJeu.getTaille() + 1)
        texteScore.widget().setParent(None)

        texteScore = QtGui.QLineEdit(self)
        texteScore.setReadOnly(True)
        texteScore.setText(str(score))
        self.layout().addWidget(texteScore, joueurCourant * 2 + 1,
                                self.partie.grilleJeu.getTaille() + 1)

        joueurCourant = (self.partie.joueurCourant)
        joueur = self.partie.listeJoueurs[joueurCourant]
        nomJoueur = joueur.getNom()
        self.parent().statusBar().showMessage("À " + nomJoueur + " de jouer")
        # self.gestionPositionDisponible()
        if self.isIAPresente and not self.partie.finPartie():
            self.parent().statusBar().showMessage(nomJoueur + " réfléchit")
            directionIA = self.partie.choixDirectionIA()
            print(directionIA)
            self.partie.modifieEtat(directionIA)
            joueurCourant = (self.partie.joueurCourant + 1) % 2
            joueur = self.partie.listeJoueurs[joueurCourant]
            nomJoueur = joueur.getNom()
            score = joueur.getScore()
            texteScore = self.layout().itemAtPosition(joueurCourant * 2 + 1,
                                                      self.partie.grilleJeu.getTaille() + 1)
            texteScore.widget().setParent(None)

            texteScore = QtGui.QLineEdit(self)
            texteScore.setReadOnly(True)
            texteScore.setText(str(score))
            self.layout().addWidget(texteScore, joueurCourant * 2 + 1,
                                    self.partie.grilleJeu.getTaille() + 1)

            joueurCourant = (self.partie.joueurCourant)
            joueur = self.partie.listeJoueurs[joueurCourant]
            nomJoueur = joueur.getNom()
            self.parent().statusBar().showMessage("À " + nomJoueur + " de jouer")
            self.gestionPositionDisponible()
        else:
            self.gestionPositionDisponible()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
