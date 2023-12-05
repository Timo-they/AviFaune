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
        self.ImageScroll.setWidgetResizable(True)
        self.ImageGlayout = QtWidgets.QGridLayout()
        self.ImageGWidget = QtWidgets.QWidget()

        self.path2pictures = 'C:\\Users\\ewenl\\Documents\\IMT Atlantique\\2A\\Projet commande entreprise\\Code\\Surf'
        self.listPictures = listdir(self.path2pictures)
        self.miniatures_label ={}
        self.photo_pixmap = {}
        self.photo_pixmap_overscaled = {}
        self.photo_pixmap_overscaled_cropped = {}
        self.photo_pixmap_scaled= {}
        self.n = 25
        self.i = 0
        self.add_miniatures()

        self.ImageGWidget.setLayout(self.ImageGlayout)
        self.ImageScroll.setWidget(self.ImageGWidget)
        self.ImageVLayout.addWidget(self.ImageScroll)

        self.load_button = QtWidgets.QPushButton(self.ImageWidget)
        self.load_button.setText("charger plus d'images")
        self.ImageVLayout.addWidget(self.load_button)

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


##        self.load_action = QAction("charger plus d'images")
        self.load_button.clicked.connect(self.load_more_miniatures)


    def add_miniatures(self) :

##        photo_pixmap = QPixmap('/home/toiture/Pictures/PINGOUIN-TORDA-1.jpg')

        while self.i < self.n and self.i < len(self.listPictures) :
            self.miniatures_label[self.i] = QtWidgets.QLabel()
            self.photo_pixmap[self.i] = QtGui.QPixmap(self.path2pictures+'\\'+self.listPictures[self.i])
##            photo_pixmap[i] = QtGui.QPixmap('C:\\Users\\ewenl\\Documents\\IMT Atlantique\\2A\\Projet commande entreprise\\Code\\Surf\\23-09-21 - 12h07 - PoulpyCup-Surf - 001.jpg')

            #On rend d'abord la photo en temps que carré 1024x1024px (ici, on ne fait que la réduire en taille pour que son plus petit coté fasse 1024px)
            self.photo_pixmap_overscaled[self.i] = self.photo_pixmap[self.i].scaled(1024, 1024, aspectRatioMode=Qt.KeepAspectRatioByExpanding)

            #On centre le carré sur l'image, car c'est souvent au centre de la photo ce qui est intéressant
            aleft = (self.photo_pixmap_overscaled[self.i].width() - 1024) // 2
            atop = (self.photo_pixmap_overscaled[self.i].height() - 1024) // 2
            self.photo_pixmap_overscaled_cropped[self.i] = self.photo_pixmap_overscaled[self.i].copy(QtCore.QRect(aleft, atop, 1024, 1024));

            #Ensuite on la réduit de taille d'un facteur 4 avec un smooth, qui permet d'avoir un joli rendu
            self.photo_pixmap_scaled[self.i] = self.photo_pixmap_overscaled_cropped[self.i].scaled(256, 256, transformMode=Qt.SmoothTransformation)

            self.miniatures_label[self.i].setPixmap(self.photo_pixmap_scaled[self.i])
            self.miniatures_label[self.i].setFixedSize(256,256)
            self.ImageGlayout.addWidget(self.miniatures_label[self.i],self.i//5,self.i%5)
            self.i += 1

    def load_more_miniatures(self) :
        self.n += 25
        if self.n > len(self.listPictures) :
            self.load_button.setText("Il n'y a pas plus d'images à charger")
        else :
##            self.add_miniatures(self)
            while self.i < self.n and self.i < len(self.listPictures) :
                self.miniatures_label[self.i] = QtWidgets.QLabel()
                self.photo_pixmap[self.i] = QtGui.QPixmap(self.path2pictures+'\\'+self.listPictures[self.i])
    ##            photo_pixmap[i] = QtGui.QPixmap('C:\\Users\\ewenl\\Documents\\IMT Atlantique\\2A\\Projet commande entreprise\\Code\\Surf\\23-09-21 - 12h07 - PoulpyCup-Surf - 001.jpg')

                #On rend d'abord la photo en temps que carré 1024x1024px (ici, on ne fait que la réduire en taille pour que son plus petit coté fasse 1024px)
                self.photo_pixmap_overscaled[self.i] = self.photo_pixmap[self.i].scaled(1024, 1024, aspectRatioMode=Qt.KeepAspectRatioByExpanding)

                #On centre le carré sur l'image, car c'est souvent au centre de la photo ce qui est intéressant
                aleft = (self.photo_pixmap_overscaled[self.i].width() - 1024) // 2
                atop = (self.photo_pixmap_overscaled[self.i].height() - 1024) // 2
                self.photo_pixmap_overscaled_cropped[self.i] = self.photo_pixmap_overscaled[self.i].copy(QtCore.QRect(aleft, atop, 1024, 1024));

                #Ensuite on la réduit de taille d'un facteur 4 avec un smooth, qui permet d'avoir un joli rendu
                self.photo_pixmap_scaled[self.i] = self.photo_pixmap_overscaled_cropped[self.i].scaled(256, 256, transformMode=Qt.SmoothTransformation)

                self.miniatures_label[self.i].setPixmap(self.photo_pixmap_scaled[self.i])
                self.miniatures_label[self.i].setFixedSize(256,256)
                self.ImageGlayout.addWidget(self.miniatures_label[self.i],self.i//5,self.i%5)
                self.i += 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

