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

from PIL import Image, ExifTags
from os import listdir,remove
from os.path import isfile

global script_directory
script_directory = os.getcwd()

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Fenêtre 'Série view'")

        self.centralWidget = QtWidgets.QWidget()
        self.centralLayout = QtWidgets.QVBoxLayout()

            # Top layout
        self.topLayout = QtWidgets.QHBoxLayout()
                # Affichage des séries
        self.SeriesLayout = QtWidgets.QScrollArea()
        self.SeriesListWidget = QtWidgets.QWidget()
        self.SeriesListLayout = QtWidgets.QVBoxLayout()

        self.SeriesLayout.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy(1))
        self.SeriesLayout.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy(1))

        list_series = {}
        for i in range(20) :
            list_series[i] = QtWidgets.QPushButton()
            list_series[i].setText("Série "+str(i))
            self.SeriesListLayout.addWidget(list_series[i])

        self.SeriesListWidget.setLayout(self.SeriesListLayout)
        self.SeriesLayout.setWidget(self.SeriesListWidget)
        self.topLayout.addWidget(self.SeriesLayout)

                # Affichage des images
        self.ImageWidget = QtWidgets.QWidget()
##        self.ImageWidget.setStyleSheet("background-color:red;")
        self.ImageVLayout = QtWidgets.QVBoxLayout()
                    # Affichage du nom de la série
        self.SerieName = QtWidgets.QLabel()
        self.SerieName.setText("Nom de la série sélectionnée")
        self.ImageVLayout.addWidget(self.SerieName)
                    # Affichage de toutes les miniatures
        self.ImageScroll = QtWidgets.QScrollArea()
        self.ImageGlayout = QtWidgets.QGridLayout()
        self.ImageGWidget = QtWidgets.QWidget()

        """
        path2pictures = 'C:\\Users\\ewenl\\Documents\\IMT Atlantique\\2A\\Projet commande entreprise\\Code\\Surf'
        listPictures = listdir(path2pictures)
        miniatures_label ={}
        miniatures_pixmap = {}
        for i in range(len(listPictures)) :
            miniatures_label[i] = QtWidgets.QLabel()
            miniatures_pixmap[i] = QtGui.QPixmap(path2pictures+'\\'+listPictures[i])
##            miniatures_pixmap[i] = QtGui.QPixmap('C:\\Users\\ewenl\\Documents\\IMT Atlantique\\2A\\Projet commande entreprise\\Code\\Surf\\23-09-21 - 12h07 - PoulpyCup-Surf - 001.jpg')
            miniatures_pixmap[i] = miniatures_pixmap[i].scaled(240,135)
            miniatures_label[i].setPixmap(miniatures_pixmap[i])
            miniatures_label[i].setScaledContents(False)
            miniatures_label[i].setGeometry(0,0,240,135)
            self.ImageGlayout.addWidget(miniatures_label[i],i//5,i%5)
        """

        path2pictures = 'C:\\Users\\ewenl\\Documents\\IMT Atlantique\\2A\\Projet commande entreprise\\Code\\Surf'
        listPictures = listdir(path2pictures)
        miniatures_label ={}
        photo_pixmap = {}
        photo_pixmap_overscaled = {}
        photo_pixmap_overscaled_cropped = {}
        photo_pixmap_scaled= {}

##        photo_pixmap = QPixmap('/home/toiture/Pictures/PINGOUIN-TORDA-1.jpg')

        for i in range(len(listPictures)) :
            miniatures_label[i] = QtWidgets.QLabel()
            photo_pixmap[i] = QtGui.QPixmap(path2pictures+'\\'+listPictures[i])
##            photo_pixmap[i] = QtGui.QPixmap('C:\\Users\\ewenl\\Documents\\IMT Atlantique\\2A\\Projet commande entreprise\\Code\\Surf\\23-09-21 - 12h07 - PoulpyCup-Surf - 001.jpg')

            #On rend d'abord la photo en temps que carré 1024x1024px (ici, on ne fait que la réduire en taille pour que son plus petit coté fasse 1024px)
            photo_pixmap_overscaled[i] = photo_pixmap[i].scaled(1024, 1024, aspectRatioMode=Qt.KeepAspectRatioByExpanding)

            #On centre le carré sur l'image, car c'est souvent au centre de la photo ce qui est intéressant
            aleft = (photo_pixmap_overscaled[i].width() - 1024) // 2
            atop = (photo_pixmap_overscaled[i].height() - 1024) // 2
            photo_pixmap_overscaled_cropped[i] = photo_pixmap_overscaled[i].copy(QtCore.QRect(aleft, atop, 1024, 1024));

            #Ensuite on la réduit de taille d'un facteur 4 avec un smooth, qui permet d'avoir un joli rendu
            photo_pixmap_scaled[i] = photo_pixmap_overscaled_cropped[i].scaled(256, 256, transformMode=Qt.SmoothTransformation)

            miniatures_label[i].setPixmap(photo_pixmap_scaled[i])
            self.ImageGlayout.addWidget(miniatures_label[i],i//5,i%5)

        self.ImageGWidget.setLayout(self.ImageGlayout)
        self.ImageScroll.setWidget(self.ImageGWidget)
        self.ImageVLayout.addWidget(self.ImageScroll)

        self.ImageWidget.setLayout(self.ImageVLayout)
        self.topLayout.addWidget(self.ImageWidget,5)

                # Affichage des stats
        self.StatsWidget = QtWidgets.QWidget()
        self.StatsWidget.setStyleSheet("background-color:blue;")
        self.topLayout.addWidget(self.StatsWidget,1)



            # Bottom layout
        self.bottomLayout = QtWidgets.QHBoxLayout()

                # Bouton précédent
        self.prev_button = QtWidgets.QPushButton(self.centralWidget)
        self.prev_button.setText("prev")
        self.bottomLayout.addWidget(self.prev_button)

                # Zone miniatures
        self.zoneMiniatures = QtWidgets.QWidget()
        self.zoneMiniatures.setStyleSheet("background-color:green;")
        self.bottomLayout.addWidget(self.zoneMiniatures,5)

                # Bouton suivant
        self.next_button = QtWidgets.QPushButton(self.centralWidget)
        self.next_button.setText("next")
        self.bottomLayout.addWidget(self.next_button)



        self.centralLayout.addLayout(self.topLayout)
        self.centralLayout.addLayout(self.bottomLayout)

        self.centralWidget.setLayout(self.centralLayout)
        self.setCentralWidget(self.centralWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

