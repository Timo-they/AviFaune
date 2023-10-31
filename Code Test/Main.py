#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ewenl
#
# Created:     29/10/2023
# Copyright:   (c) ewenl 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import time
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenuBar, QAction, QFileDialog, QGridLayout, QWidget, QSizePolicy

global script_directory
script_directory = os.getcwd()

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Fenêtre test")
            # Global widget
        self.centralWidget = QWidget()

        self.Label = QLabel("Hello, World")
        self.Label.setAlignment(Qt.AlignCenter)

            # All layouts
        self.centralLayout = QGridLayout()
        self.centralLayout.addWidget(self.Label,0,1,1,1)

            # Content
        self.blank = QWidget()
        self.blank.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.blank.setObjectName("blank")
        self.blank.setMinimumHeight(500)
        self.blank.setMinimumWidth(500)

        self.prev_button = QtWidgets.QPushButton(self.centralWidget)
        self.prev_button.setText("prev")
        self.next_widget = QWidget()
        self.next_button = QtWidgets.QPushButton(self.centralWidget)
        self.next_button.setText("next")

        self.centralLayout.addWidget(self.prev_button,1,0)
        self.centralLayout.addWidget(self.blank,1,1)
        self.centralLayout.addWidget(self.next_button,1,2)

        self.centralLayout.setRowStretch(0,0)
        self.centralLayout.setRowStretch(1,3)
        self.centralLayout.setColumnStretch(1,2)

        self.centralWidget.setLayout(self.centralLayout)
        self.setCentralWidget(self.centralWidget)

        self._createActions()
        self._createMenuBar()
        self._connectActions()
        self.mode = "série"


    def _createMenuBar(self) :
        menuBar = self.menuBar()

        menuFichier = menuBar.addMenu("Fichier")
        menuFichier.addAction(self.open_folder)
        menuFichier.addAction(self.export_stats)
        menuFichier.addAction(self.close)

        menuMode = menuBar.addMenu("Mode")

        menuSerie = menuMode.addMenu("Série")
        menuSerie.addAction(self.auto_detect)
        menuSerie.addAction(self.suppr_detect)
        menuSerie.addAction(self.imp_photo_suppl)

        menuMode.addAction(self.photo)


    def _createActions(self) :
        self.open_folder = QAction("Ouvrir un fichier",self)
        self.export_stats = QAction("exporter les statistiques",self)
        self.close = QAction("Close",self)

        self.auto_detect = QAction("Détection automatique",self)
        self.suppr_detect = QAction("Effacer la détection",self)
        self.imp_photo_suppl = QAction("Importer une photo supplémentaire",self)

        self.photo = QAction("Photo",self)

    def _connectActions(self) :
            # Actions pour le menu Fichier
        self.open_folder.triggered.connect(self.Open_folder)
        self.export_stats.triggered.connect(self.Export_stats)
        self.close.triggered.connect(self.Close)

            # Actions pour le menu Série
        self.auto_detect.triggered.connect(self.Auto_detect)
        self.suppr_detect.triggered.connect(self.Suppr_detect)
        self.imp_photo_suppl.triggered.connect(self.Imp_photo_suppl)

            # Actions pour le menu Photo
        self.photo.triggered.connect(self.Photo)

            # Pour les boutons
        self.prev_button.clicked.connect(self.open_previous_photo)
        self.next_button.clicked.connect(self.open_next_photo)


    def Open_folder(self) :
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.Label.setText(file)
##        current_directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
##        Archive_r = open(str(script_directory+"/Data/Archive.txt"),"r")
##        lines = Archive_r.readlines()
##        Archive_r.close()
##        if not ((current_directory+"\n") in lines) :
##            Archive_a = open(str(script_directory+"/Data/Archive.txt"),"a")
##            Archive_a.write(current_directory+"\n")
##            Archive_a.close()
##        self.topWidget.setText(lines[-1])

    def Export_stats(self) :
        self.Label.setText("on exporte les stats")

    def Close(self) :
        self.centralWidget.setText("on ferme l'application")
        time.sleep(1)
        QMainWindow.close()

    def Auto_detect(self) :
        self.topWidget.setText("on lance l'auto détection")

    def Suppr_detect(self) :
        self.topWidget.setText("on enlève la détection")

    def Imp_photo_suppl(self) :
        self.topWidget.setText("on ajoute une photo")

    def Photo(self) :
        self.Label.setText("on passe en mode photo")

    def open_photo(self, name_photo: str) :
        return

    def open_next_photo(self) :
        self.Label.setText("image suivante")

    def open_previous_photo(self) :
        self.Label.setText("image précédente")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

