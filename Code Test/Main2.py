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
        self.setWindowTitle("Fenêtre test_ui")

        self.centralWidget = QtWidgets.QWidget()
        self.centralLayout = QtWidgets.QVBoxLayout()

            # Top layout
        self.topLayout = QtWidgets.QVBoxLayout()
                # Affichage des séries
        self.SeriesLayout = QtWidgets.QScrollArea()

        self.SeriesListWidget = QtWidgets.QWidget()
        self.SeriesListLayout = QtWidgets.QVBoxLayout()

        self.serie1 = QtWidgets.QPushButton()
        self.serie1.setText("Série 1")
        self.SeriesListLayout.addWidget(self.serie1)
        self.serie2 = QtWidgets.QPushButton()
        self.serie2.setText("Série 2")
        self.SeriesListLayout.addWidget(self.serie2)
        self.serie3 = QtWidgets.QPushButton()
        self.serie3.setText("Série 3")
        self.SeriesListLayout.addWidget(self.serie3)
        self.serie4 = QtWidgets.QPushButton()
        self.serie4.setText("Série 4")
        self.SeriesListLayout.addWidget(self.serie4)
        self.serie5 = QtWidgets.QPushButton()
        self.serie5.setText("Série 5")
        self.SeriesListLayout.addWidget(self.serie5)
        self.serie6 = QtWidgets.QPushButton()
        self.serie6.setText("Série 6")
        self.SeriesListLayout.addWidget(self.serie6)
        self.serie7 = QtWidgets.QPushButton()
        self.serie7.setText("Série 7")
        self.SeriesListLayout.addWidget(self.serie7)
        self.serie8 = QtWidgets.QPushButton()
        self.serie8.setText("Série 8")
        self.SeriesListLayout.addWidget(self.serie8)
        self.serie9 = QtWidgets.QPushButton()
        self.serie9.setText("Série 9")
        self.SeriesListLayout.addWidget(self.serie9)

        self.SeriesListWidget.setLayout(self.SeriesListLayout)
        self.SeriesLayout.setWidget(self.SeriesListWidget)
        self.topLayout.addWidget(self.SeriesLayout)

                # Affichage des images
        self.ImageWidget = QtWidgets.QWidget()
        self.ImageWidget.setStyleSheet("background-color:red;")
        self.topLayout.addWidget(self.ImageWidget)

                # Affichage des images
        self.StatsWidget = QtWidgets.QWidget()
        self.StatsWidget.setStyleSheet("background-color:blue;")
        self.topLayout.addWidget(self.StatsWidget)



            # Bottom layout
        self.bottomLayout = QtWidgets.QHBoxLayout()

                # Bouton précédent
        self.prev_button = QtWidgets.QPushButton(self.centralWidget)
        self.prev_button.setText("prev")
        self.bottomLayout.addWidget(self.prev_button)

                # Zone miniatures
        self.zoneMiniatures = QtWidgets.QWidget()
        self.zoneMiniatures.setStyleSheet("background-color:green;")
        self.bottomLayout.addWidget(self.zoneMiniatures)

                # Bouton suivant
        self.next_button = QtWidgets.QPushButton(self.centralWidget)
        self.next_button.setText("next")
        self.bottomLayout.addWidget(self.next_button)


        self.centralLayout.addLayout(self.topLayout)
        self.centralLayout.addLayout(self.bottomLayout)

##            # Central widget
##        self.centralWidget = QWidget()
##
##        self.Label = QLabel("Hello, World")
##        self.Label.setAlignment(Qt.AlignCenter)
##
##            # All layouts
##        self.centralLayout = QGridLayout()
##        self.centralLayout.addWidget(self.Label,0,1,1,1)
##
##            # Content
##        self.blank = QWidget()
##        self.blank.setStyleSheet("background-color: rgb(255, 255, 255);")
##        self.blank.setObjectName("blank")
##        self.blank.setMinimumHeight(500)
##        self.blank.setMinimumWidth(500)
##
##        self.prev_button = QtWidgets.QPushButton(self.centralWidget)
##        self.prev_button.setText("prev")
##        self.next_widget = QWidget()
##        self.next_button = QtWidgets.QPushButton(self.centralWidget)
##        self.next_button.setText("next")
##
##        self.centralLayout.addWidget(self.prev_button,1,0)
##        self.centralLayout.addWidget(self.blank,1,1)
##        self.centralLayout.addWidget(self.next_button,1,2)
##
##        self.centralLayout.setRowStretch(0,0)
##        self.centralLayout.setRowStretch(1,3)
##        self.centralLayout.setColumnStretch(1,2)
##
        self.centralWidget.setLayout(self.centralLayout)
        self.setCentralWidget(self.centralWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

