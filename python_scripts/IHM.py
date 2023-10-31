
from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):

    def setupUi(self, MainWindow):
                # Définition de l'arrangement global
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")

                # Séparateurs
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

                # Espace de gauche
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

                # Espace central
        self.widget_4 = QtWidgets.QWidget(self.splitter_2)
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_4.setObjectName("widget_4")
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 400, 400))

                # Espace de droite
        self.widget_5 = QtWidgets.QWidget(self.splitter_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setGeometry(QtCore.QRect(120, 120, 71, 31))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.splitter_3)

                # Espace du haut (barre des menus)
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

        self._retranslateUi(MainWindow)
        self._createActions(MainWindow)
        self._createMenuBar(MainWindow)
        self._connectActions(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _createMenuBar(self,MainWindow) :
        self.menuBar = self.menuBar()
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1027, 26))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBar.sizePolicy().hasHeightForWidth())
        self.menuBar.setSizePolicy(sizePolicy)

            # Menu Fichier
        self.menuFichier = self.menuBar.addMenu("Fichier")
        self.menuFichier.addAction(self.action_open_folder)
        self.menuFichier.addAction(self.action_export_stats)
        self.menuFichier.addAction(self.action_close)

            # Menu Série
        self.menuSerie = self.menuBar.addMenu("Série")
        self.menuSerie.addAction(self.action_auto_detect)
        self.menuSerie.addAction(self.action_suppr_detect)
        self.menuSerie.addAction(self.action_add_photo)

            # Menu mode
        self.menuMode = self.menuBar.addMenu("Mode")
                # Menu passage mode série
        self.menuMode.addAction(self.action_mode_serie)
                # Menu passage mode photo
        self.menuMode.addAction(self.action_mode_photo)

        MainWindow.setMenuBar(self.menuBar)


    def _createActions(self, MainWindow) :
        self.action_open_folder = QtWidgets.QAction("Ouvrir un fichier",MainWindow)
        self.action_export_stats = QtWidgets.QAction("exporter les statistiques",MainWindow)
        self.action_close = QtWidgets.QAction("Close",MainWindow)

        self.action_auto_detect = QtWidgets.QAction("Détection automatique",MainWindow)
        self.action_suppr_detect = QtWidgets.QAction("Effacer la détection",MainWindow)
        self.action_add_photo = QtWidgets.QAction("Importer une photo supplémentaire",MainWindow)

        self.action_mode_serie = QtWidgets.QAction("Passage mode série",MainWindow)
        self.action_mode_photo = QtWidgets.QAction("Passage mode photo",MainWindow)


    def _connectActions(self,MainWindow) :
            # Actions pour le menu Fichier
        self.action_open_folder.triggered.connect(MainWindow.open_folder)
        self.action_export_stats.triggered.connect(MainWindow.export_stats)
        self.action_close.triggered.connect(MainWindow.close)

            # Actions pour le menu Série
        self.action_auto_detect.triggered.connect(MainWindow.auto_detect)
        self.action_suppr_detect.triggered.connect(MainWindow.suppr_detect)
        self.action_add_photo.triggered.connect(MainWindow.add_photo)

            # Actions pour le menu Photo
        self.action_mode_serie.triggered.connect(MainWindow.switch_to_serie_menu)
        self.action_mode_photo.triggered.connect(MainWindow.switch_to_photo_menu)

            # Pour les boutons
##        self.action_prev_button.clicked.connect(MainWindow.open_previous_photo)
##        self.action_next_button.clicked.connect(MainWindow.open_next_photo)

    def _retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Série 1"))
        self.pushButton_2.setText(_translate("MainWindow", "Série 2"))
        self.pushButton_3.setText(_translate("MainWindow", "Série 3"))
        self.label.setText(_translate("MainWindow", "Satistiques"))
##        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
##        self.menuSerie.setTitle(_translate("MainWindow", "Série"))
##        self.menuPhoto.setTitle(_translate("MainWindow", "Photo"))
##        self.actionOuvrir_un_dossier.setText(_translate("MainWindow", "Ouvrir un dossier"))
##        self.actionExporter_statistiques.setText(_translate("MainWindow", "Exporter statistiques "))
##        self.actionClose.setText(_translate("MainWindow", "Close"))
##        self.actionD_tection_automatique.setText(_translate("MainWindow", "Détection automatique"))
##        self.actionEffacer_la_d_tection.setText(_translate("MainWindow", "Effacer la détection "))
##        self.actionImporter_une_photo_suppl_mentaire.setText(_translate("MainWindow", "Importer une photo supplémentaire"))

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