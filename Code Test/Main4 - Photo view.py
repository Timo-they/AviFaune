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
        self.setWindowTitle("Fenêtre 'file view'")

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
        self.ImageWidget.setStyleSheet("background-color:red;")
        self.topLayout.addWidget(self.ImageWidget,5)

                # Affichage des images
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

