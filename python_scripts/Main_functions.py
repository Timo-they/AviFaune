#-------------------------------------------------------------------------------
# Name:         Main_functions
# Purpose:      Fonctions utilisées par l'interface graphique
#
# Author:       Wewen
#
# Created:     28/10/2023
# Copyright:   IMT Atlantique
# Licence:     Chacalot®
#-------------------------------------------------------------------------------

# Liste des import
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from tkinter import filedialog
from tkinter import *

# Menu déroulant Fichier
##      Bouton Fichier->Ouvrir
##  Imput :
##  Ouput : folder_path[str]
def open_folder() :
    filename =  filedialog.askdirectory()
    return(root.filename)

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