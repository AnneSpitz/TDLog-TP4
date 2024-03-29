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


import random
import math
import copy

import grid
import player
import outils

# Différentes combinaisons de touches possibles pour les contrôles, permet de choisir ses
# touches de contrôle, pour le moment fixé sur la deuxième combinaison.
tabDirectionAcceptable = [
    {"8": [0, -1], "4": [-1, 0], "2": [0, 1], "6": [1, 0], "7": [-1, -1], "9": [1, -1],
     "1": [-1, 1], "3": [1, 1]},
    {"z": [-1, 0], "q": [0, -1], "x": [1, 0], "d": [0, 1], "a": [-1, -1], "e": [-1, 1],
     "w": [1, -1], "c": [1, 1]}]

commandesChoisies = 1
directionAcceptable = tabDirectionAcceptable[commandesChoisies]

profondeurMax = 4  # Définie la profondeur maximle de l'algorithme de minMax.


class Game:
    def __init__(self, joueur1, joueur2, taille=0, tableauValeurs=0):
        """
        Constructeur.
        :param taille: (int) Taille de la grille.
        :param joueur1: (str) Nom du premier joueur
        :param joueur2: (str) Nom du deuxième joueur
        :param taille: (int) Définie à 0 par défaut, dans le cas où on rentre une list dans
        tableauValeurs. Si on rentre une valeur, ce sera la taille de la grille.
        :param tableauValeurs: (list) Défini à 0 par défaut, si on rentre une list dedans,
        le type ne sera plus int et la grille sera défini par tableauValeurs.
        """

        # Initialisation du joueur en train de jouer à 0.
        self.joueurCourant = 0

        # On crée la liste des joueurs.
        self.listeJoueurs = [player.Player(joueur1), player.Player(joueur2)]

        # On test si le tableau de valeurs est défini par quelque chose (par défaut défini sur
        # un int, donc si ce n'est pas le cas c'est qu'on a donné une liste en entrée) :
        if not isinstance(tableauValeurs, int):

            # Dans le cas où un tableau est donné en entrée, on constuit une grille à partir de
            # ce tableau.
            taille = len(tableauValeurs)
            self.grilleJeu = grid.Grid(taille, tableauValeurs)

        # Sinon, on crée une grille aléatoire :
        else:

            # Création d'une gille vide, qu'on remplie de valeurs aléatoires.
            self.grilleJeu = grid.Grid(taille)
            for abscisse in range(taille):
                for ordonnee in range(taille):
                    self.grilleJeu[(abscisse, ordonnee)] = random.choice(grid.point)

        # La position initiale est définie et mise à 0 : elle est déjà explorée.
        self.grilleJeu[(taille // 2, taille // 2)] = None
        self.positions = [taille // 2, taille // 2]

    def demandeDirection(self):
        """
        Demande à l'utilisateur de rentrer une touche du clavier.
        :return: une list correspondant à la touche demandée.
        """

        return input(
            "À {0} de jouer.\nAppuyez sur une touche parmi : "
            "{1}; {2}; {3}; {4}; {5}; {6}; {7}; {8}. Choisissez une case non vide.".format(
                self.listeJoueurs[self.joueurCourant].getNom(), *directionAcceptable.keys()))

    def isDirectionValide(self, direction):
        """
        Fonction qui teste si la direction demandée est compatible avec la grille actuelle.
        Appelle simplement not isDirectionNonValide.
        :param direction: (str) Direction selon laquelle on souhaite avancer.
        :return: True si la direction est correcte et qu'on peut continuer.
                 False si la direction n'est pas correcte.
        """

        return not self.isDirectionNonValide(direction)

    def isDirectionNonValide(self, direction):
        """
        Fonction qui teste si la direction demandée est incompatible avec la grille actuelle.
        /!\ Attention /!\ Cette fonction doit être employée avec not pour vérifier si on peut aller
        dans la direction demandée. Cela pour des raisons de facilité à coder la fonction.
        :param direction: (str) Direction selon laquelle on souhaite avancer.
        :return: False si la direction est correcte et qu'on peut continuer.
                 True si la direction n'est pas correcte.
        """

        # On commence par véfifier si la direction n'est pas dans les directions du tableau de
        # commandes.
        if direction not in directionAcceptable.keys():
            return True

        else:

            positionVoulue = outils.Outils.add(self.positions, directionAcceptable[direction])
            # On vérifie ensuite si la position voulue n'est pas dans le tableau :
            if positionVoulue not in self.grilleJeu:
                return True

            # Puis si la case a déjà été visitée.
            elif not isinstance(self.grilleJeu[positionVoulue], int):
                return True

            else:
                return False

    def modifieEtat(self, direction):
        """
        
        :param direction: (str) direction conforme aux directions acceptables, selon laquelle on
        souhaite se déplacer.
        :return: Rien.
        """

        # Dans l'ordre : On modifie la position du pion, on augmente le score du joueur courant,
        # on passe la position précédente à "visitée" et on change de joueur.


        self.positions = outils.Outils.add(self.positions, directionAcceptable[direction])

        positions = self.positions
        joueurCourant = self.joueurCourant

        self.listeJoueurs[joueurCourant].augmenteScore(self.grilleJeu[positions])
        self.grilleJeu[positions] = None
        self.joueurCourant = (joueurCourant + 1) % 2

        return

    def finPartie(self):
        """
        Permet de déterminer si la partie est finie ou non, c'est à dire s'il reste des
        directions acceptable avec des points à récupérer.
        :return: True si la partie est finie,
                 False sinon.
        """

        # Dans toutes les directions possibles on vérifie qu'il y en ai au moins une d'acceptable
        #  (soit non-visitée).
        for direction in directionAcceptable.values():
            positionTestee = outils.Outils.add(self.positions, direction)

            if positionTestee in self.grilleJeu and isinstance(self.grilleJeu[positionTestee], int):
                return False

        return True

    def resultatPartie(self):
        """
        Affiche le résultat de la partie et renvoie les numéro des joueurs vainqueurs.
        :return: Renvoie la liste des indices des joueurs ayant gagnés.
        """

        # Récupération des données des joueurs.
        listeJoueurs = self.listeJoueurs
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
            print("Il y a une égalité ! Les joueurs ont {} points.".format(str(scoreMaximal)))

        elif nombreGagnant == 1:
            print("{} a gagné ! Son score est de {} points.".format(nomJoueurs[listeGagnant[0]],
                                                                    scoreMaximal))

        else:
            nomGagnant = [nomJoueurs[indice] for indice in listeGagnant]
            print("Les joueurs {} ont gagné avec {} points !".format(nomGagnant, scoreMaximal))

        return listeGagnant

    def affichage(self):
        """
        Affiche l'état actuel de la partie, avec la grille, le pion, les joueurs et leurs scores.
        :return: Rien.
        """

        print("\n\n==============================================\n"
              "==============================================\n\n\n")

        self.grilleJeu.affichageGrille(self.positions)
        maxLength = max(len(self.listeJoueurs[i].getNom()) for i in {0, 1})  # Permet d'aligner
        # les ":" du scores.
        self.listeJoueurs[0].afficheJoueur(maxLength)
        self.listeJoueurs[1].afficheJoueur(maxLength)

    def writeIntoCSV(self, nomFichier):
        """
        Permet d'enregistrer la grille dans un fichier csv en appelant la fonction
        writeGridIntoCSV de la grille.
        :param nomFichier: (str) Nom du fichier dans lequel on veut écrire la grille de jeu.
        """
        self.grilleJeu.writeGridIntoCSV(nomFichier)

    def minMax(self, profondeur, isMax, indiceJoueurIA):
        """
        Applique l'algorithme de min-max à self, sur profondeur itération.
        :param profondeur: (int) Nombre d'itération maximale. Si profondeur = 0 on passe dans
           le cas de base.
        :param isMax: (bool) Si isMax est vrai on cherche le plus grand résultat, sinon le plus faible.
        :param indiceJoueurIA: (int) Indice du joueur dont on cherche le score
        :return: Renvoie le score calculer sur le moment, sous forme de int.
        """

        #  Cas de base :
        if self.finPartie() or profondeur <= 0:

            return int(self.listeJoueurs[indiceJoueurIA].getScore())

        # Récursion :
        else:

            #  isMax == True correspond à un coup de l'IA, qui doit prendre le meilleur résultat
            # possible.
            if isMax:

                valeur = - math.inf

                # On teste toute les direction qui sont valides :
                for direction in directionAcceptable:
                    if self.isDirectionValide(direction):
                        selfLocal = copy.deepcopy(self)
                        selfLocal.modifieEtat(direction)
                        # On remplace valeur si le nouveau score calculé par minMax est meilleur
                        # (plus grand), sinon on garde valeur.
                        valeur = max(valeur, selfLocal.minMax(profondeur - 1, False,
                                                              indiceJoueurIA))

                return int(valeur)

            # isMax == False correspond à un coup du joueur, il faut donc minimiser son score possible.
            else:

                valeur = math.inf

                # On teste toute les direction qui sont valides :
                for direction in directionAcceptable:
                    if self.isDirectionValide(direction):
                        selfLocal = copy.deepcopy(self)
                        selfLocal.modifieEtat(direction)
                        # On remplace valeur si le nouveau score calculé par minMax est meilleur
                        # (plus petit), sinon on garde valeur.
                        valeur = min(valeur, selfLocal.minMax(profondeur - 1, True,
                                                              indiceJoueurIA))
                return int(valeur)


    def choixDirectionIA(self):
        """
        Permet à l'IA de choisir la direction optimale, en utilisant la fonction minMax.
        :return: Renvoie la direction correspondant au score maximale sous forme de str.
        """

        # Initialisaton d'un dictionnaire de score.
        score = {}
        # On sauvegarde l'indice du joueur IA.
        indiceJoueurIA = self.joueurCourant

        # L'IA tente toutes les directions et va choisir celle dont le minMax renvoie
        # le plus grand score.
        valeurOptimale = 0
        directionChoisie = ""

        for direction in directionAcceptable:

            # On effectue une copie profonde de la self pour pouvoir travailler dessus.
            selfLocal = copy.deepcopy(self)

            if not selfLocal.isDirectionNonValide(direction):

                # On modifie la position puis on calcule la valeur du minMax.
                selfLocal.modifieEtat(direction)
                valeur = selfLocal.minMax(profondeurMax, False, indiceJoueurIA)

                # On modifie la valeurOptimale et la direction si on a une meilleure valeur.
                if valeur > valeurOptimale:
                    valeurOptimale = valeur
                    directionChoisie = direction

        return directionChoisie
