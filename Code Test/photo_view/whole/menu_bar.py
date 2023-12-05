


from functools import partial
import os

from PyQt5.QtWidgets import QAction, QMenu, QMainWindow, QMenuBar, QFileDialog, QMessageBox

import datas

class MenuBarHandler():

    def __init__(self):
        datas.set_widget("menu_bar_handler", self)

        self.build_menu_bar()

    def build_menu_bar(self):
        self.create_actions()
        self.connect_actions()
        self.add_actions()
    
    def create_actions(self):
        oizo_window = datas.get_widget("oizo_window")

        self.open_folder_as_serie_action = QAction("Ajouter un dossier", oizo_window)
        self.open_folder_as_serie_action.setToolTip("Ajoute un dossier en tant que série")
        self.create_remove_serie_actions()
        self.export_global_stats_action = QAction("Exporter les statistiques", oizo_window)
        self.close_app_action = QAction("Fermer l'application", oizo_window)

        self.auto_detect_whole_serie_action = QAction("Effectuer la détection d'oiseaux sur la série", oizo_window)
        self.export_serie_stats_action = QAction("Exporter les statistiques de la série", oizo_window)
        self.remove_serie_action = QAction("Enlever la série", oizo_window)
        self.close_serie_action = QAction("Fermer la série", oizo_window)

        self.auto_detect_photo_action = QAction("Effectuer la détection d'oiseaux sur la photo", oizo_window)
        self.close_photo_action = QAction("Fermer la photo", oizo_window)

    def create_remove_serie_actions(self):
        oizo_window = datas.get_widget("oizo_window")
        self.remove_serie_actions = []

        for id, path in datas.get_series().items():
            action = QAction(os.path.basename(os.path.dirname(path)), oizo_window)
            action.setToolTip(path)
            action.triggered.connect(partial(self.remove_serie, id, path))
            self.remove_serie_actions.append(action)


    def connect_actions(self):
        self.open_folder_as_serie_action.triggered.connect(self.open_folder_as_serie)
        self.close_app_action.triggered.connect(self.close_app)

        self.remove_serie_action.triggered.connect(self.remove_current_serie)
        self.close_serie_action.triggered.connect(self.close_serie)

        self.close_photo_action.triggered.connect(self.close_photo)

    def add_actions(self):
        oizo_window: QMainWindow = datas.get_widget("oizo_window")
        menu_bar: QMenuBar = oizo_window.menuBar()

        self.menu_fichier: QMenu = menu_bar.addMenu("Fichier")
        self.menu_fichier.setToolTipsVisible(True)

        self.menu_fichier.addAction(self.open_folder_as_serie_action)
        self.menu_fichier_remove_serie: QMenu = self.menu_fichier.addMenu("Enlever une série")
        self.menu_fichier_remove_serie.setToolTipsVisible(True)
        for action in self.remove_serie_actions:
            self.menu_fichier_remove_serie.addAction(action)
        self.menu_fichier.addAction(self.export_global_stats_action)
        self.menu_fichier.addAction(self.close_app_action)

        self.menu_serie: QMenu = menu_bar.addMenu("Série")
        self.menu_serie.setToolTipsVisible(True)
        self.menu_serie.setEnabled(False)

        self.menu_serie.addAction(self.auto_detect_whole_serie_action)
        self.menu_serie.addAction(self.export_serie_stats_action)
        self.menu_serie.addAction(self.remove_serie_action)
        self.menu_serie.addAction(self.close_serie_action)

        self.menu_photo: QMenu = menu_bar.addMenu("Photo")
        self.menu_photo.setToolTipsVisible(True)
        self.menu_photo.setEnabled(False)

        self.menu_photo.addAction(self.auto_detect_photo_action)
        self.menu_photo.addAction(self.close_photo_action)

    def open_folder_as_serie(self):
        print("Opening a folder...")
        dialog = QFileDialog(datas.get_widget("oizo_window"))
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)

        folder = QFileDialog.getExistingDirectory(datas.get_widget("oizo_window"), "Select Directory")
        
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
    
    def export_stats(self):
        print("Opening stats...")

    def close_app(self):
        print("Closing app...")
        datas.get_widget("oizo_window").close()
    
    def remove_current_serie(self):
        self.remove_serie(datas.get_current_serie(), datas.get_current_serie_path())

    def close_serie(self):
        datas.set_current_serie("")


    def close_photo(self):
        datas.set_current_photo("")
    

    def update(self):
        self.menu_serie.setEnabled(datas.get_current_serie() != "")
        self.menu_photo.setEnabled(datas.get_current_photo() != "")

        self.menu_fichier_remove_serie.clear()
        self.create_remove_serie_actions()

        for action in self.remove_serie_actions:
            self.menu_fichier_remove_serie.addAction(action)

