
from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_3 = QtWidgets.QSplitter(self.widget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        
        self.widget_3 = QtWidgets.QWidget(self.splitter_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        
        self.widget_4 = QtWidgets.QWidget(self.splitter_2)
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_4.setObjectName("widget_4")
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 400, 400))
   
        self.widget_5 = QtWidgets.QWidget(self.splitter_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setGeometry(QtCore.QRect(120, 0, 71, 31))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.splitter_3)
        
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.widget_2)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalLayout.addWidget(self.horizontalScrollBar)
        self.gridLayout.addWidget(self.splitter, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1027, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuS_rie = QtWidgets.QMenu(self.menubar)
        self.menuS_rie.setObjectName("menuS_rie")
        self.menuPhoto = QtWidgets.QMenu(self.menubar)
        self.menuPhoto.setObjectName("menuPhoto")
        MainWindow.setMenuBar(self.menubar)
        self.actionOuvrir_un_dossier = QtWidgets.QAction(MainWindow)
        self.actionOuvrir_un_dossier.setObjectName("actionOuvrir_un_dossier")
        self.actionExporter_statistiques = QtWidgets.QAction(MainWindow)
        self.actionExporter_statistiques.setObjectName("actionExporter_statistiques")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionD_tection_automatique = QtWidgets.QAction(MainWindow)
        self.actionD_tection_automatique.setObjectName("actionD_tection_automatique")
        self.actionEffacer_la_d_tection = QtWidgets.QAction(MainWindow)
        self.actionEffacer_la_d_tection.setObjectName("actionEffacer_la_d_tection")
        self.actionImporter_une_photo_suppl_mentaire = QtWidgets.QAction(MainWindow)
        self.actionImporter_une_photo_suppl_mentaire.setObjectName("actionImporter_une_photo_suppl_mentaire")
        self.menuFichier.addAction(self.actionOuvrir_un_dossier)
        self.menuFichier.addAction(self.actionExporter_statistiques)
        self.menuFichier.addAction(self.actionClose)
        self.menuS_rie.addAction(self.actionD_tection_automatique)
        self.menuS_rie.addAction(self.actionEffacer_la_d_tection)
        self.menuS_rie.addAction(self.actionImporter_une_photo_suppl_mentaire)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuS_rie.menuAction())
        self.menubar.addAction(self.menuPhoto.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #### GUI Bindings pour Fichier
    def switch_to_file_menu():
        return

    def update_file_menu(series: dict):
        return

    #### GUI Bindings pour Série
    def switch_to_serie_menu():
        return

    def update_serie_menu(id_serie: int, series: dict):
        return

    def update_serie_statistique(id_serie: int, series: dict):
        return

    def refresh_photos_from_serie(id_serie: int, series: dict):
        return

    #### GUI Bindings pour Photo
    def switch_to_photo_menu():
        return

    def update_photo_menu(name_photo: str, id_serie: int, series: dict):
        return

    def show_photo(name_photo: str, id_serie: int, series: dict):
        return



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Série 1"))
        self.pushButton_2.setText(_translate("MainWindow", "Série 2"))
        self.pushButton_3.setText(_translate("MainWindow", "Série 3"))
        self.label.setText(_translate("MainWindow", "Satistiques"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuS_rie.setTitle(_translate("MainWindow", "Série"))
        self.menuPhoto.setTitle(_translate("MainWindow", "Photo"))
        self.actionOuvrir_un_dossier.setText(_translate("MainWindow", "Ouvrir un dossier"))
        self.actionExporter_statistiques.setText(_translate("MainWindow", "Exporter statistiques "))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionD_tection_automatique.setText(_translate("MainWindow", "Détection automatique"))
        self.actionEffacer_la_d_tection.setText(_translate("MainWindow", "Effacer la détection "))
        self.actionImporter_une_photo_suppl_mentaire.setText(_translate("MainWindow", "Importer une photo supplémentaire"))
