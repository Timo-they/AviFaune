#-------------------------------------------------------------------------------
# Name:         MainWindow
# Purpose:      Fonctions utilisées par l'interface graphique
#
# Author:       Wewen
#
# Created:     28/10/2023
# Copyright:   IMT Atlantique
# Licence:     Chacalot®
#-------------------------------------------------------------------------------

from PyQt5.QtWidgets import * # PyQt module for graphic components (controls, etc...)

from IHM import UiMainWindow
from pathlib import Path


    # Pour pouvoir sauvegarder les données, j'utilise des .txt qu'il faut aller lire
    # J'utilise script_directory pour accéder au dossier
import os
global script_directory
script_directory = os.getcwd()

class MainWindow(QMainWindow, UiMainWindow):

    #Données de l'application à sauvegarder entre plusieurs ouvertures
    series = {}
    id_serie = 0
    name_photo = ""
    current_directory = ""

    def __init__(self):
       super(MainWindow, self).__init__()

        # TODO : load application data

       self.setupUi(self)

                # Menu déroulant Fichier
    ##      Bouton Fichier->Ouvrir
    def Open_folder() :
        return

    ##      Bouton Fichier->Exporter les statistiques
    def export_stats() :
        script_directory = "pomme"

    ##      Bouton Fichier->Fermer l'application
    def close() :
        return

                # Menu déroulant Série
    ##      Bouton Série->Détection automatique des oiseaux
    def auto_detect() :
        return

    ##      Bouton Série->Supprimer la détection actuelle
    def suppr_detect() :
        return

    ##      Bouton Série->Ajouter photo supplémentaire à la série
    def add_photo() :
        return

    # Tous les menus
    ##      Clique sur une série sur menu de gauche
    def open_serie(id_serie: int) :
        return

    # Menu Série
    ##      Clique sur une photo de la série en bas ou au milieu
    def open_photo(name_photo: str) :
        return

    # Menu Photo
    ##      Clique sur une photo de la série en bas
    def open_photo(name_photo: str) :
        return

    ##      Clique sur flèche droite
    def open_next_photo() :
        return

    ##      Clique sur flèche gauche
    def open_previous_photo() :
        return