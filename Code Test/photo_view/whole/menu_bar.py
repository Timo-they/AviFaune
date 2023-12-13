


from functools import partial
import os
from ultralytics import YOLO

from PyQt5.QtWidgets import QAction, QMenu, QMainWindow, QMenuBar, QFileDialog, QMessageBox, QInputDialog

import datas

class MenuBarHandler():

    model: YOLO

    def __init__(self):
        datas.set_widget("menu_bar_handler", self)
        self.model = None

        self.build_menu_bar()

    def build_menu_bar(self):
        self.create_actions()
        self.connect_actions()
        self.add_actions()
    
    # On instancie toutes les actions possibles du menu
    def create_actions(self):
        oizo_window = datas.get_widget("oizo_window")

        # Le menu de Fichier
        self.open_folder_as_serie_action = QAction("Ajouter un dossier", oizo_window)
        # TODO : Voir si on met des tooltips pour chacun...
        self.open_folder_as_serie_action.setToolTip("Ajoute un dossier en tant que série")
        self.create_remove_serie_actions()
        self.export_global_stats_action = QAction("Exporter les statistiques", oizo_window)
        self.close_app_action = QAction("Fermer l'application", oizo_window)

        # Le menu de Série
        self.auto_detect_whole_serie_action = QAction("Effectuer la détection d'oiseaux sur la série", oizo_window)
        self.export_serie_stats_action = QAction("Exporter les statistiques de la série", oizo_window)
        self.remove_serie_action = QAction("Enlever la série", oizo_window)
        self.close_serie_action = QAction("Fermer la série", oizo_window)

        # Le menu de Photo
        self.auto_detect_photo_action = QAction("Effectuer la détection d'oiseaux sur la photo", oizo_window)
        self.remove_detect_photo_action = QAction("Réinitialiser la détection d'oiseaux sur la photo", oizo_window)
        self.close_photo_action = QAction("Fermer la photo", oizo_window)

        # Le menu d'Espèces
        self.add_specie_action = QAction("Ajouter une nouvelle espèce d'oiseaux", oizo_window)
        self.remove_specie_action = QAction("Enlever une espèce d'oiseaux", oizo_window)
        self.change_specie_color_action = QAction("Changer la couleur d'une espèce", oizo_window)

    # Ca c'est pour qu'on ai un bouton de suppression pour chaque série
    def create_remove_serie_actions(self):
        oizo_window = datas.get_widget("oizo_window")
        self.remove_serie_actions = []

        for id, path in datas.get_series().items():
            action = QAction(os.path.basename(os.path.dirname(path)), oizo_window)
            action.setToolTip(path)
            action.triggered.connect(partial(self.remove_serie, id, path))
            self.remove_serie_actions.append(action)

    # On connecte toutes les actions à leur fonction associée
    def connect_actions(self):
        # Le menu de Fichier
        self.open_folder_as_serie_action.triggered.connect(self.open_folder_as_serie)
        self.export_global_stats_action.triggered.connect(self.export_global_stats)
        self.close_app_action.triggered.connect(self.close_app)

        # Le menu de Série
        self.auto_detect_whole_serie_action.triggered.connect(self.auto_detect_whole_serie)
        self.export_serie_stats_action.triggered.connect(self.export_serie_stats)
        self.remove_serie_action.triggered.connect(self.remove_current_serie)
        self.close_serie_action.triggered.connect(self.close_serie)

        # Le menu de Photo
        self.auto_detect_photo_action.triggered.connect(self.auto_detect_photo)
        self.remove_detect_photo_action.triggered.connect(self.remove_detect_photo)
        self.close_photo_action.triggered.connect(self.close_photo)

        # Le menu d'Especes
        self.add_specie_action.triggered.connect(self.add_specie)
        self.remove_specie_action.triggered.connect(self.remove_specie)
        self.change_specie_color_action.triggered.connect(self.change_specie_color)

    # Finalement on construit tout le menu
    def add_actions(self):
        oizo_window: QMainWindow = datas.get_widget("oizo_window")
        menu_bar: QMenuBar = oizo_window.menuBar()

        # Le menu de Fichier
        self.menu_fichier: QMenu = menu_bar.addMenu("Fichier")
        self.menu_fichier.setToolTipsVisible(True)

        self.menu_fichier.addAction(self.open_folder_as_serie_action)
        self.menu_fichier_remove_serie: QMenu = self.menu_fichier.addMenu("Enlever une série")
        self.menu_fichier_remove_serie.setToolTipsVisible(True)
        for action in self.remove_serie_actions:
            self.menu_fichier_remove_serie.addAction(action)
        self.menu_fichier.addAction(self.export_global_stats_action)
        self.menu_fichier.addAction(self.close_app_action)

        # Le menu de Série
        self.menu_serie: QMenu = menu_bar.addMenu("Série")
        self.menu_serie.setToolTipsVisible(True)
        self.menu_serie.setEnabled(False)

        self.menu_serie.addAction(self.auto_detect_whole_serie_action)
        self.menu_serie.addAction(self.export_serie_stats_action)
        self.menu_serie.addAction(self.remove_serie_action)
        self.menu_serie.addAction(self.close_serie_action)

        # Le menu de Photo
        self.menu_photo: QMenu = menu_bar.addMenu("Photo")
        self.menu_photo.setToolTipsVisible(True)
        self.menu_photo.setEnabled(False)

        self.menu_photo.addAction(self.auto_detect_photo_action)
        self.menu_photo.addAction(self.remove_detect_photo_action)
        self.menu_photo.addAction(self.close_photo_action)

        # Le menu d'Espèces
        self.menu_especes: QMenu = menu_bar.addMenu("Espèces")
        self.menu_especes.setToolTipsVisible(True)

        self.menu_especes.addAction(self.add_specie_action)
        self.menu_especes.addAction(self.remove_specie_action)
        self.menu_especes.addAction(self.change_specie_color_action)

    #Quand la série actuelle ou la photo actuelle ou la liste des séries changent
    def update(self):
        # Met à jour l'accès aux menus Série et Photo
        self.menu_serie.setEnabled(datas.get_current_serie() != "")
        self.menu_photo.setEnabled(datas.get_current_photo() != "")

        # Met à jour les séries qu'on peut supprimer
        self.menu_fichier_remove_serie.clear()
        self.create_remove_serie_actions()

        for action in self.remove_serie_actions:
            self.menu_fichier_remove_serie.addAction(action)
    

    ### FICHIER ###

    def open_folder_as_serie(self):
        print("Opening a folder...")
        dialog = QFileDialog(datas.get_widget("oizo_window"))
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)

        folder = QFileDialog.getExistingDirectory(datas.get_widget("oizo_window"), "Select Directory")
        
        if folder == "":
            print("No folder chosen")
            return
        
        print("Folder chosen : " + folder + "/")

        if folder + "/" in datas.get_series().values():
            print("Folder already opened")
            oizo_window: QMainWindow = datas.get_widget("oizo_window")
            QMessageBox.question(oizo_window, "Série déjà ouverte", "La série est déjà ouverte, elle ne peut pas être ouverte une seconde fois.", QMessageBox.Ok)
            return
        
        print("Adding new folder : ", folder + "/")
        datas.add_serie(folder + "/")
    
    def remove_serie(self, id: str, path: str):
        print("Asking for deleting serie ", path)
        oizo_window: QMainWindow = datas.get_widget("oizo_window")
        confirmation = QMessageBox.question(oizo_window, "Enlever la série " + os.path.basename(os.path.dirname(path)), "Est tu certain que tu souhaites enlever la série " + os.path.basename(os.path.dirname(path)) + " ?\nLa série n'apparaitra plus dans la liste de séries, les statistiques liées à la série seront supprimées, mais le dossier associé à la série ne sera pas supprimé.", QMessageBox.Yes | QMessageBox.No)

        if confirmation == QMessageBox.Yes:
            print("Confirmed serie deletion")
            if datas.get_current_serie() == id:
                print("Unselecting serie...")
                datas.set_current_serie("")

            print("Removing serie...")
            datas.remove_serie(id)
        
        else:
            print("Aborted.")

    def export_global_stats(self):
        # TODO : Open File dialog to choose save path
        # TODO : Save stats at given path as CSV File
        print("TODO : Open File dialog to choose save path")
        print("TODO : Save stats at given path as CSV File")
    
    def close_app(self):
        print("Closing app...")
        datas.get_widget("oizo_window").close()
    
    ### SERIE ###

    def auto_detect_whole_serie(self):
        # TODO : Generate stats for every photo of the serie
        print("TODO : Generate stats for every photo of the serie")

    def export_serie_stats(self):
        # TODO : Open File dialog to choose save path
        # TODO : Save stats at given path as CSV File
        print("TODO : Open File dialog to choose save path")
        print("TODO : Save stats at given path as CSV File")

    def remove_current_serie(self):
        self.remove_serie(datas.get_current_serie(), datas.get_current_serie_path())

    def close_serie(self):
        datas.set_current_serie("")


    ### PHOTO ####

    def auto_detect_photo(self):
        #   0: Bécasseau Sanderling
        #   1: Bernache Cravant
        #   2: Goéland Argenté
        #   3: Mouette Rieuse
        #   4: Pluvier Argenté

        if self.model == None:
            self.model = YOLO("whole/best.pt")
        
        prediction = self.model.predict(datas.get_current_photo_full_path(), save=True)

        boxes_classes = prediction[0].boxes.cls.cpu()
        boxes_shapes = prediction[0].boxes.xywh.cpu()
        print(boxes_classes, boxes_shapes)

        # TODO : set stats directly when autodetect
        print("TODO : set stats directly when autodetect")

        datas.get_widget("central_photo").set_boxes(boxes_classes, boxes_shapes)

    def remove_detect_photo(self):
        # TODO : Remove stats from photo
        print("TODO : Remove stats from photo")

    def close_photo(self):
        datas.set_current_photo("")
    

    ### ESPECES ###

    def add_specie(self):
        oizo_window = datas.get_widget("oizo_window")
        # TODO : Dialog to add specie
        print("TODO : Dialog to add specie")
        text, ok = QInputDialog.getText(oizo_window, "Ajout d'une espèce", "Saisis le nom de l'espèce que tu souhaite rajouter à l'application : ")

        if ok and text != "":
            print("Adding specie", text)
            datas.add_specie(text)
        
        else:
            print("Specie adding aborted")
    
    def remove_specie(self):
        # TODO : Add menu to remove specie
        print("TODO : Add menu to remove specie")
    
    def change_specie_color(self):
        # TODO : Add menu to change the color of a specie
        print("TODO : Add menu to change the color of a specie")
    


