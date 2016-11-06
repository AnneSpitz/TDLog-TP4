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
from PyQt4 import QtGui
import pandas

import game
import customExceptions
import outils
import functools


class OutilsGraphique():
    """
    Classe d'outils nécessaire à la création d'objet graphique, comme les boutons et les zone de
    texte.
    """

    @staticmethod
    def creeBouton(entite, nom, position_x, position_y, fonction, isEnabled=True):
        """
        Crée un QPushBouton.
        :param entite: Entité dont va dépendre le bouton.
        :param nom: (str) Nom à afficher sur le bouton.
        :param position_x: (int) Position en x du bouton.
        :param position_y: (int) Position en y du bouton.
        :param fonction: Fonction à appeler lorsque le bouton est activé.
        :param isEnabled: (bool) Détermine si le bouton doit être enabled.
        :return: Renvoie le bouton ainsi créé.
        """
        boutonCree = QtGui.QPushButton(nom, entite)
        boutonCree.move(position_x, position_y)
        boutonCree.clicked.connect(fonction)

        boutonCree.setEnabled(isEnabled)

        return boutonCree

    @staticmethod
    def creeZoneTexte(entite, position_x, position_y, readOnly=True):
        """
        Crée une QLineEdit.
        :param entite: Entité dont va dépendre la zone de texte.
        :param position_x: (int) Position en x de la zone de texte.
        :param position_y: (int) Position en y de la zone de texte.
        :param readOnly: Détermine si la zone peut être éditée directement. Par défaut mise en
        lecture seule, pour éviter les incohérences entre l'affichage et les données internes.
        :return: Renvoie la zone de texte créé.
        """
        zoneTexte = QtGui.QLineEdit(entite)
        zoneTexte.setReadOnly(readOnly)
        zoneTexte.move(position_x, position_y)

        return zoneTexte


class Menu(QtGui.QWidget):
    """
    Classe qui définie le menu du jeu.
    """

    def __init__(self):
        super(Menu, self).__init__()

        # On appelle la fonction qui crée l'interface utilisateur.
        self.initUI()

    def initUI(self):
        """
        Cette fonction crée l'interface utilisateur en appelant les fonctions qui créent les
        différents éléments (boutons et zone de texte).
        :return: Rien.
        """
        # Création des boutons et zones de texte pour les différents paramètres.
        self.creeBoutonNombreJoueur()

        self.creeBoutonsJoueurs()

        self.creeBoutonsAleatoire_CSV()

        self.creeBoutonLancementPartie()

        #  Positionnement et affichage de la fenêtre.
        self.setGeometry(200, 200, 320, 300)
        self.setWindowTitle('Menu du jeu')
        self.show()

        return

    def creeBoutonNombreJoueur(self):
        """
        Crée le paramètre nombre de joueur ainsi que le bouton et la zone de texte associés.
        :return: Rien.
        """
        self.nombreJoueur = 0

        self.boutonNombreJoueurs = OutilsGraphique.creeBouton(self, 'Nombre de joueurs', 20, 20,
                                                              self.demandeNombreJoueurs)

        self.texteNombreJoueurs = OutilsGraphique.creeZoneTexte(self, 180, 22)

        return

    def demandeNombreJoueurs(self):
        """
        Fonction appelée lorsque le bouton du nombre de joueurs est appelé. Vérifie que le nombre de
        joueurs est cohérent (1 ou 2) et enregistre et affiche le nombre.
        :return: Rien.
        """
        # On demande par une fenêtre de dialogue combien de joueurs vont jouer. text correspond à
        # la donnée rentrée et ok est True si le bouton ok est cliqué.
        text, ok = QtGui.QInputDialog.getText(self, 'Nombre de joueur',
                                              'Nombre de joueur (1/2):')
        # Vérifie que le nombre de joueurs est cohérent. Sinon on ne fait rien, à part prévenir que
        # le nombre est non cohérent.
        if text not in {"1", "2"}:
            ok = False
            self.texteNombreJoueurs.setText("Entrer 1 ou 2 !")
        if ok:
            self.texteNombreJoueurs.setText(text)  # Sinon, on affiche le nombre de joueurs.
            # Et on empêche ce nombre d'être modifié par la suite.
            self.boutonNombreJoueurs.setEnabled(False)
            self.nombreJoueur = int(text)

            # On active également les boutons de nom des joueurs en fonction du nombre de joueurs.
            self.boutonNomJoueur1.setEnabled(True)
            if self.nombreJoueur == 2:
                self.boutonNomJoueur2.setEnabled(True)

        return

    def creeBoutonsJoueurs(self):
        """
        Crée les boutons des noms des joueurs, ainsi que les paramètres et zones de texte associés.
        :return: Rien.
        """
        # Les paramètres sont initialisés à 0 pour pouvoir tester leur état dans les fonctions
        # demandeNomJoueur1 et demandeNomJoueur2.
        self.nomJoueur1 = ""
        self.nomJoueur2 = ""

        self.boutonNomJoueur1 = OutilsGraphique.creeBouton(self, 'Nom joueur 1', 20, 70,
                                                           self.demandeNomJoueur1, isEnabled=False)
        self.texteNomJoueur1 = OutilsGraphique.creeZoneTexte(self, 180, 72)

        self.boutonNomJoueur2 = OutilsGraphique.creeBouton(self, 'Nom joueur 2', 20, 110,
                                                           self.demandeNomJoueur2, isEnabled=False)
        self.texteNomJoueur2 = OutilsGraphique.creeZoneTexte(self, 180, 112)

        return

    def demandeNomJoueur1(self):
        """
        Fonction appelée quand on clique sur le bouton du nom du joueur 1.
        :return: Rien.
        """

        # On demande par une fenêtre de dialogue le nom du joueur 1. text correspond à
        # la donnée rentrée et ok est True si le bouton ok est cliqué.
        text, ok = QtGui.QInputDialog.getText(self, 'Nom joueur',
                                              'Nom du joueur 1 :')

        # Si le texte est non vide et qu'on a cliqué sur ok, on affiche le texte, empêche
        # l'utilisateur de modifier son résultat en enregistre la donnée.
        if ok and text != "":
            self.boutonNomJoueur1.setEnabled(False)
            self.nomJoueur1 = text
            self.texteNomJoueur1.setText(text)

            # Selon le nombre de joueurs, on définit le nom du joueur 2 ici ou non.
            if self.nombreJoueur == 1:
                self.nomJoueur2 = "Glados"
                self.texteNomJoueur2.setText(self.nomJoueur2)

        # Si les noms des deux joueurs ont été remplis, on permet aux joueurs de passer à la
        # création de grille.
        if self.nomJoueur1 != "" and self.nomJoueur2 != "":
            self.boutonChargementCSV.setEnabled(True)
            self.boutonTaillePartie.setEnabled(True)

        return

    def demandeNomJoueur2(self):
        """
        Fonction appelée quand on clique sur le bouton du nom du joueur 2.
        :return: Rien.
        """

        # On demande par une fenêtre de dialogue le nom du joueur 2. text correspond à
        # la donnée rentrée et ok est True si le bouton ok est cliqué.
        text, ok = QtGui.QInputDialog.getText(self, 'Nom joueur',
                                              'Nom du joueur 2 :')

        # Si le texte est non vide et qu'on a cliqué sur ok, on affiche le texte, empêche
        # l'utilisateur de modifier son résultat en enregistre la donnée.
        if ok and text != "":
            self.boutonNomJoueur2.setEnabled(False)
            self.nomJoueur2 = text
            self.texteNomJoueur2.setText(text)

        # Si les noms des deux joueurs ont été remplis, on permet aux joueurs de passer à la
        # création de grille.
        if self.nomJoueur1 != "" and self.nomJoueur2 != "":
            self.boutonChargementCSV.setEnabled(True)
            self.boutonTaillePartie.setEnabled(True)

        return

    def creeBoutonsAleatoire_CSV(self):
        """
        Crée les boutons permettant de créer la partie de manière aléatoire ou par chargement d'un
        csv, ainsi que les paramètres et zones de texte associés.
        :return: Rien.
        """
        # Les variables relatives à chargementCSV permmettent de choisir un fichier csv.
        self.chargementCSV = 0
        # Les variables relatives à taillePartie permettent de créer aléatoirement une partie.
        self.taillePartie = 0

        self.boutonChargementCSV = OutilsGraphique.creeBouton(self, 'Charger un fichier', 20, 160,
                                                              self.chercheFichier, isEnabled=False)
        self.textChargementCSV = OutilsGraphique.creeZoneTexte(self, 180, 162)

        self.boutonTaillePartie = OutilsGraphique.creeBouton(self, 'Génération aléatoire', 20,
                                                             200, self.generePartieAleatoire,
                                                             isEnabled=False)
        self.texteTaillePartie = OutilsGraphique.creeZoneTexte(self, 180, 202)

        return

    def generePartieAleatoire(self):
        """
        Fonction appelée quand on clique sur le bouton de taille partie.
        :return: Rien.
        """
        # On empêche le chargement d'un csv.
        self.boutonChargementCSV.setEnabled(False)

        # On demande par une fenêtre de dialogue la taille souhaitée. text correspond à
        # la donnée rentrée et ok est True si le bouton ok est cliqué.
        text, ok = QtGui.QInputDialog.getText(self, 'Génération aléatoire',
                                              'Taille de la grille ? (Entier impaire):')

        if ok:
            # On vérifie que la donnée est compatible (entier positif impair)
            try:
                textInt = int(text)
                if textInt <= 0:
                    raise customExceptions.TailleNegativeError
                if textInt % 2 != 1:
                    raise customExceptions.TaillePaireError

            # Si la donnée n'est pas bonne, on affiche le problème.
            except ValueError:
                self.texteTaillePartie.setText("Entier requis")

            except customExceptions.TailleNegativeError:
                self.texteTaillePartie.setText("Entier positif !")

            except customExceptions.TaillePaireError:
                self.texteTaillePartie.setText("Entier pair !")

            else:
                # Si c'est le cas, on affiche la taille requise, on affiche et sauvegarde la taille,
                # on empêche qu'elle soit modifiée et on permet le lancement de la partie.
                self.texteTaillePartie.setText(text)
                self.boutonTaillePartie.setEnabled(False)
                self.boutonDebutPartie.setEnabled(True)
                self.taillePartie = textInt

            return

    def chercheFichier(self):
        """
        Fonction appelée quand on clique sur le bouton de chargement de csv.
        :return: Rien.
        """

        # On demande par une fenêtre de dialogue le nom du fichier souhaité. text correspond à
        # la donnée rentrée et ok est True si le bouton ok est cliqué.
        text, ok = QtGui.QInputDialog.getText(self, 'Chargement fichier',
                                              'Entrer nom du fichier (sans extension):')

        if ok:
            # On rajoute manuellement l'extension du fichier, puis on essaye de l'ouvrir.
            text += ".csv"
            try:
                with open(text) as csvfile:

                    # Si ça réussi on sauvegarde le fichier.
                    self.chargementCSV = pandas.read_csv(csvfile, delimiter=",", header=None)


            except FileNotFoundError:
                self.textChargementCSV.setText("Fichier non trouvé")

            else:
                # Si le fichier est chargé, on affiche son nom, on empêche la modification de la
                # taille et du nom et autorise le lancement de la partie.
                self.textChargementCSV.setText(text)
                self.boutonTaillePartie.setEnabled(False)
                self.boutonChargementCSV.setEnabled(False)
                self.boutonDebutPartie.setEnabled(True)

        return

    def creeBoutonLancementPartie(self):
        """
        Crée le bouton permettant de lancer la partie.
        :return: Rien.
        """
        self.boutonDebutPartie = OutilsGraphique.creeBouton(self, 'LANCER LA PARTIE', 100,
                                                            250, self.lancementPartie,
                                                            isEnabled=False)
        return

    def lancementPartie(self):
        """
        Fonction appelé lorsqu'on lance la partie.
        :return: Rien.
        """
        # On désactive le bouton de lancement de partie.
        self.boutonDebutPartie.setEnabled(False)

        # On crée la partie avec les différents paramètres.
        partie = game.Game(self.nomJoueur1, self.nomJoueur2, taille=self.taillePartie,
                           tableauValeurs=self.chargementCSV)

        # On définit la présence de l'IA.
        if self.nombreJoueur == 1:
            isIAPresente = True
        else:
            isIAPresente = False

        # On crée la fenêtre de jeu.
        self.AffichageJeu = MyMainWindow(partie, isIAPresente)

        # On l'affiche.
        self.affichageJeu()

        return

    def affichageJeu(self):
        """
        Permet l'affichage d'une QMainWindow.
        :return: Rien.
        """
        # Affiche la QMainWindow du jeu.
        self.AffichageJeu.show()

        return


class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, partie, isIAPresente, parent=None):
        super(MyMainWindow, self).__init__(parent)
        # La classe contient une QGridLayout en central Widget.
        self.formWidget = FormWidget(self, partie, isIAPresente)
        self.setCentralWidget(self.formWidget)
        self.initUI()

    def initUI(self):
        """
        Fonction d'initialisation de la QMainWindow. Possède simplement une statusBar.
        :return: Rien.
        """
        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Jeu')


class FormWidget(QtGui.QWidget):
    """
    Classe centrale, aura une QGridLayout pour afficher le jeu.
    """
    def __init__(self, parent, partie, isIAPresente):
        super(FormWidget, self).__init__(parent)
        self.partie = partie
        self.isIAPresente = isIAPresente
        # On récupère les données (partie et IA) et on crée les boutons.
        self.initButton()

    def initButton(self):
        """
        Fonction qui initialise la grille centrale.
        :return: Rien.
        """
        # Les Widget sont stockés dans une QGridLayout qui sera le layout principal.
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        grille = self.partie.grilleJeu # Cette ligne permet de simplifier la lecture du code.
        tailleGrille = grille.getTaille()

        # On récupère les données de la grille pour les afficher dans le QGridLayout.
        valeurs = [grille[(i, j)] for i in range(tailleGrille) for j in range(tailleGrille)]
        positions = [[i, j] for i in range(tailleGrille) for j in range(tailleGrille)]
        for position, valeur in zip(positions, valeurs):

            # On change l'affichage en fonction de la valeur (int ou NoneType).
            if isinstance(valeur, int):
                affichage = str(valeur)
            elif position == self.partie.positions:
                affichage = "###"
            else:
                affichage = "0"

            # On crée les boutons à l'aide de functools.partials pour passer une direction en
            # paramètre, pour le moment non définie.
            button = QtGui.QPushButton(affichage)
            fonctionPush1 = lambda direction: self.buttonClicked("")
            fonctionPush2 = functools.partial(fonctionPush1, "")

            button.clicked.connect(fonctionPush2)
            button.setEnabled(False)
            grid.addWidget(button, *position)

        # On rajoute une colonne de score.
        texteLateral = [self.partie.listeJoueurs[0].getNom(), "0",
                        self.partie.listeJoueurs[1].getNom(), "0"]

        for ligne in range(4):
            texteScore = QtGui.QLineEdit(self)
            texteScore.setReadOnly(True)
            texteScore.setText(texteLateral[ligne])
            grid.addWidget(texteScore, ligne, tailleGrille + 1)

        # On initialise les boutons disponibles et leur direction avec gestionPositionDisponible.
        self.gestionPositionDisponible()
        self.setGeometry(500, 500, 390, 350)

        return

    def resultatPartie(self):
        """
        Affiche le résultat de la partie et renvoie les numéro des joueurs vainqueurs.
        :return: Renvoie le texte à afficher dans la statusBar.
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

        # Création du texte en fonction du gagnant. :
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
        """
        Fonction permettant de gérer les boutons qu'il est possible de cliquer, ainsi que la
        direction qui leur est associée.
        :return:
        """
        # Affiche le résultat de la partie si cette dernière est finie.
        if self.partie.finPartie():
            self.parent().statusBar().showMessage(self.resultatPartie())

        # On va se baser sur la position du joueur.
        positions = self.partie.positions

        # Premier bloc déterminant les cases disponibles d'accès et la direction à emprunter pour
        # les rejoindre.
        deplacementPossible = {}
        for deplacement in game.directionAcceptable:
            if self.partie.isDirectionValide(deplacement):
                positionPossible = tuple(
                    outils.Outils.add(positions, game.directionAcceptable[deplacement]))
                deplacementPossible[positionPossible] = deplacement

        tailleGrille = self.partie.grilleJeu.getTaille()

        # Deuxième bloc permettant de recréer les boutons en fonction de leur nouvel état (valeur
        # et disponibilité).
        for ligne in range(tailleGrille):
            for colonne in range(tailleGrille):
                # On récupère la valeur.
                valeur = self.partie.grilleJeu[(ligne, colonne)]

                # On définie la couleur et le texte à afficher en fonction de la valeur stockée (int
                # ou NoneType).
                if isinstance(valeur, int):
                    affichage = str(valeur)
                    style = 'QPushButton {background-color: #E8E8E8; color: black;}'
                elif [ligne, colonne] == self.partie.positions:
                    affichage = "###"
                    style = 'QPushButton {background-color: #71C5D1; color: black;}'
                else:
                    affichage = "0"
                    style = 'QPushButton {background-color: #F2F2F2; color: white;}'

                # On présuppose que la case est non accessible au joueur.
                caseJouable = False

                # On va vérifier que c'est bien le cas, en parcourant les deplacementPossible.
                for deplacement in deplacementPossible:

                    # On récupère la direction et position associées.
                    directionLocale = deplacementPossible[deplacement]
                    positionVoulue = outils.Outils.add(positions,
                                                       game.directionAcceptable[directionLocale])

                    # On vérifie que la position de la case est dans la liste des possibilités.
                    if [ligne, colonne] == positionVoulue:

                        # Si c'est le cas, on rend la case disponible.
                        boutonLocal = self.layout().itemAtPosition(ligne, colonne)
                        boutonLocal.widget().setParent(None)
                        boutonLocal = QtGui.QPushButton(
                            str(self.partie.grilleJeu[(ligne, colonne)]))
                        boutonLocal.setStyleSheet(
                            'QPushButton {background-color: #D0D0D0; color: black;}')

                        # On associe notamment la direction au bouton.
                        direction = deplacementPossible[(ligne, colonne)]
                        fonctionPush1 = lambda direction: self.buttonClicked(direction)
                        fonctionPush2 = functools.partial(fonctionPush1, direction)

                        boutonLocal.clicked.connect(fonctionPush2)
                        boutonLocal.setEnabled(True)
                        self.layout().addWidget(boutonLocal, ligne, colonne)
                        # On définie que la case est jouable.
                        caseJouable = True

                # Si la case est non jouable, on change le bouton avec sa valeur et comme étant non
                # cliquable.
                if not caseJouable:
                    boutonLocal = self.layout().itemAtPosition(ligne, colonne)
                    boutonLocal.widget().setParent(None)
                    boutonLocal = QtGui.QPushButton(affichage)
                    boutonLocal.setStyleSheet(style)
                    fonctionPush1 = lambda direction: self.buttonClicked("")
                    fonctionPush2 = functools.partial(fonctionPush1, "")

                    boutonLocal.clicked.connect(fonctionPush2)
                    boutonLocal.setEnabled(False)
                    self.layout().addWidget(boutonLocal, ligne, colonne)

        return

    def buttonClicked(self, direction):
        """
        Fonction appellée quand on clique sur les boutons de la QGridLayout.
        :param direction: (str) Direction associée au bouton cliqué.
        :return: Rien.
        """
        # On récupère le bouton.
        sender = self.sender()

        # On modifie l'état du bouton.
        sender.setEnabled(False)
        sender.setText("0")

        # On applique le changement de direction.
        self.partie.modifieEtat(direction)

        # On récupère les scores pour les modifier.
        joueurCourant = (self.partie.joueurCourant + 1) % 2
        joueur = self.partie.listeJoueurs[joueurCourant]
        score = joueur.getScore()
        texteScore = self.layout().itemAtPosition(joueurCourant * 2 + 1,
                                                  self.partie.grilleJeu.getTaille() + 1)
        texteScore.widget().setParent(None)

        texteScore = QtGui.QLineEdit(self)
        texteScore.setReadOnly(True)
        texteScore.setText(str(score))
        self.layout().addWidget(texteScore, joueurCourant * 2 + 1,
                                self.partie.grilleJeu.getTaille() + 1)


        # On modifie l'affichage de la statusBar.
        joueurCourant = (self.partie.joueurCourant)
        joueur = self.partie.listeJoueurs[joueurCourant]
        nomJoueur = joueur.getNom()
        self.parent().statusBar().showMessage("À " + nomJoueur + " de jouer")

        # S'il y a une IA, on joue son coup :
        if self.isIAPresente and not self.partie.finPartie():
            # On calcul la direction choisie par l'IA puis on applique son coup.
            self.parent().statusBar().showMessage(nomJoueur + " réfléchit")
            directionIA = self.partie.choixDirectionIA()
            self.partie.modifieEtat(directionIA)

            # On modifie l'affichage et les scores.
            joueurCourant = (self.partie.joueurCourant + 1) % 2
            joueur = self.partie.listeJoueurs[joueurCourant]
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

            # Dans les deux cas, on réinitialise l'état des cases.
            self.gestionPositionDisponible()
        else:
            self.gestionPositionDisponible()


def main():
    app = QtGui.QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
