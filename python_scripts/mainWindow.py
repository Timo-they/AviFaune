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


class MainWindow(QMainWindow, UiMainWindow):

    #Données de l'application à sauvegarder entre plusieurs ouvertures
    series = {}
    id_serie = 0
    name_photo = ""

    def __init__(self):
       super(MainWindow, self).__init__()

        # TODO : load applciation data

       self.setupUi(self)
    
    # Menu déroulant Fichier
    ##      Bouton Fichier->Ouvrir
    def open_folder() :

        # TODO : ouvrir une fenetre de dialogue pour choisir un dossier à ouvrir

        # TODO : enregistrer le dossier dans les series

        return
    
    ##      Bouton Fichier->Exporter les statistiques
    def export_stats() :
        return

    # Menu déroulant Série
    ##      Bouton Série->Détection automatique des oiseaux
    def detect_oizos() :
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