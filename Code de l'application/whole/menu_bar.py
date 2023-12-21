


from functools import partial
import os
import csv

from ultralytics import YOLO

# import torch
# import torchvision.transforms as transforms

# import onnxruntime
# import numpy as np
# from PIL import Image

# from onnxruntime import InferenceSession
# from PIL import Image, ImageOps
# from opyv8 import Predictor
# from pathlib import Path
# import numpy as np

from PyQt5.QtWidgets import QAction, QMenu, QMainWindow, QMenuBar, QFileDialog, QMessageBox, QInputDialog

import datas

class MenuBarHandler():

    # model: YOLO

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
        self.open_folder_as_serie_action = QAction("Ajouter une série", oizo_window)
        # TODO : Voir si on met des tooltips pour chacun...
        # self.open_folder_as_serie_action.setToolTip("Ajoute un dossier en tant que série")
        self.create_remove_serie_actions()
        self.close_app_action = QAction("Fermer l'application", oizo_window)

        # Le menu Exporter
        self.export_global_stats_action = QAction("Tout exporter", oizo_window)

        # Le menu de Détection d'oiseaux
        self.auto_detect_whole_serie_action = QAction("Effectuer la détection d'oiseaux sur la série", oizo_window)
        self.remove_detect_whole_serie_action = QAction("Réinitialiser la détection d'oiseaux sur la série", oizo_window)
        self.auto_detect_photo_action = QAction("Effectuer la détection d'oiseaux sur la photo", oizo_window)
        self.remove_detect_photo_action = QAction("Réinitialiser la détection d'oiseaux sur la photo", oizo_window)

        # Le menu d'Espèces
        self.add_specie_action = QAction("Ajouter une nouvelle espèce d'oiseaux", oizo_window)
        self.create_remove_specie_actions()

    # Ca c'est pour qu'on ai un bouton de suppression pour chaque série
    def create_remove_serie_actions(self):
        oizo_window = datas.get_widget("oizo_window")
        self.remove_serie_actions = []

        for id, path in datas.get_series().items():
            action = QAction(os.path.basename(os.path.dirname(path)), oizo_window)
            action.setToolTip(path)
            action.triggered.connect(partial(self.remove_serie, id, path))
            self.remove_serie_actions.append(action)
    
    def create_remove_specie_actions(self):
        oizo_window = datas.get_widget("oizo_window")
        self.remove_specie_actions = []

        for id, nom in datas.get_species().items():
            action = QAction(nom, oizo_window)
            action.setToolTip(nom)

            if id in datas.BASE_SPECIES.keys() or id == "-1":
                action.setDisabled(True)

            action.triggered.connect(partial(self.remove_specie, id, nom))
            self.remove_specie_actions.append(action)

    # On connecte toutes les actions à leur fonction associée
    def connect_actions(self):
        # Le menu de Fichier
        self.open_folder_as_serie_action.triggered.connect(self.open_folder_as_serie)
        self.close_app_action.triggered.connect(self.close_app)

        # Le menu exporter
        self.export_global_stats_action.triggered.connect(self.export_global_stats)

        # Le menu de Détection d'oiseaux
        self.auto_detect_whole_serie_action.triggered.connect(self.auto_detect_whole_serie)
        self.remove_detect_whole_serie_action.triggered.connect(self.remove_detect_whole_serie)
        self.auto_detect_photo_action.triggered.connect(self.auto_detect_photo)
        self.remove_detect_photo_action.triggered.connect(self.remove_detect_photo)

        # Le menu d'Especes
        self.add_specie_action.triggered.connect(self.add_specie)

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
        self.menu_fichier.addAction(self.close_app_action)

        # Le menu Exporter
        self.menu_export: QMenu = menu_bar.addMenu("Exporter")
        self.menu_export.setToolTipsVisible(True)

        self.menu_export.addAction(self.export_global_stats_action)

        # Le menu de Détection d'oiseaux
        self.menu_detection: QMenu = menu_bar.addMenu("Détection d'oiseaux")
        self.menu_detection.setToolTipsVisible(True)

        self.menu_detection.addAction(self.auto_detect_whole_serie_action)
        self.menu_detection.addAction(self.remove_detect_whole_serie_action)
        self.menu_detection.addAction(self.auto_detect_photo_action)
        self.menu_detection.addAction(self.remove_detect_photo_action)

        # Le menu d'Espèces
        self.menu_especes: QMenu = menu_bar.addMenu("Espèces")
        self.menu_especes.setToolTipsVisible(True)

        self.menu_especes.addAction(self.add_specie_action)
        self.remove_specie_menu: QMenu = self.menu_especes.addMenu("Enlever une espèce")
        self.remove_specie_menu.setToolTipsVisible(True)
        for action in self.remove_specie_actions:
            self.remove_specie_menu.addAction(action)
    
    #Quand la série actuelle ou la photo actuelle ou la liste des séries changent
    def update(self):
        # Met à jour l'accès aux actions de détecction
        self.auto_detect_whole_serie_action.setDisabled(datas.get_current_serie() == "")
        self.remove_detect_whole_serie_action.setDisabled(datas.get_current_serie() == "")
        self.auto_detect_photo_action.setDisabled(datas.get_current_photo() == "")
        self.remove_detect_photo_action.setDisabled(datas.get_current_photo() == "")
        
        # Met à jour les séries qu'on peut supprimer
        self.menu_fichier_remove_serie.clear()
        self.create_remove_serie_actions()
        self.remove_specie_menu.clear()
        self.create_remove_specie_actions()

        for action in self.remove_serie_actions:
            self.menu_fichier_remove_serie.addAction(action)
        
        for action in self.remove_specie_actions:
            self.remove_specie_menu.addAction(action)
    

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
        confirmation = QMessageBox.question(oizo_window, "Enlever la série " + os.path.basename(os.path.dirname(path)), "Êtes-vous certain de vouloir enlever cette série ?" + os.path.basename(os.path.dirname(path)) + " ?\nLa série n'apparaitra plus dans la liste de séries, les statistiques liées à la série seront supprimées, mais le dossier associé à la série ne sera pas supprimé.", QMessageBox.Yes | QMessageBox.No)

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
        # Display the save file dialog
        file_dialog = QFileDialog(datas.get_widget("oizo_window"))
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Fichiers CSV (*.csv);;Tous les fichiers (*)")

        if file_dialog.exec_() == QFileDialog.Accepted:
            selected_file = file_dialog.selectedFiles()[0]
            print(f"Selected file: {selected_file}")
            
            with open(selected_file, 'w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file)
                
                liste = [""]
                for id_serie, path_serie in datas.get_series().items():
                    liste.append(os.path.basename(os.path.dirname(path_serie)))

                liste.append("Total")

                writer.writerow(liste)

                liste = []
                for id_specie, name_specie in datas.get_species().items():
                    liste.append(name_specie)

                    for id_serie, path_serie in datas.get_series().items():
                        global_stats = datas.get_stats_global_serie(id_serie)
                        if global_stats.get(id_specie):
                            liste.append(int(global_stats[id_specie]))
                        
                        else:
                            liste.append("")

                    total = None
                    for id_serie, path_serie in datas.get_series().items():
                        global_stats = datas.get_stats_global_serie(id_serie)
                        if global_stats.get(id_specie):
                            if total == None:
                                total = 0
                            total += int(global_stats[id_specie])
                        
                    if total == None:
                        liste.append("")
                    else:
                        liste.append(total)
                    
                    writer.writerow(liste)
                    liste = []

                        



    
    def close_app(self):
        print("Closing app...")
        datas.get_widget("oizo_window").close()
    
    ### SERIE ###

    def auto_detect_whole_serie(self):
        for id, nom in datas.get_photos().items():
            self.auto_detect_photo(id, datas.get_current_photo_full_path(id))

    def remove_detect_whole_serie(self):
        for id, nom in datas.get_photos().items():
            datas.remove_stats_current_photo(id)

    def remove_current_serie(self):
        self.remove_serie(datas.get_current_serie(), datas.get_current_serie_path())

    def close_serie(self):
        datas.set_current_serie("")


    ### PHOTO ####

    def auto_detect_photo(self, id_photo = None, photo_full_path = None):
        #   0: Bécasseau Sanderling
        #   1: Bernache Cravant
        #   2: Goéland Argenté
        #   3: Mouette Rieuse
        #   4: Pluvier Argenté

        if not photo_full_path:
            photo_full_path = datas.get_current_photo_full_path()
        
        if not id_photo:
            id_photo = datas.get_current_photo()
        
        if id_photo == "":
            print(datas.COLOR_BRIGHT_RED, "Hmmm, it seems detecting on no photo won't work ", id_photo, photo_full_path, datas.COLOR_RESET)

        datas.remove_stats_current_photo(id_photo)
        print("Detecting oizooos on ", photo_full_path)

        ######### opyv8

        # model = Path("whole/best.onnx")
        # # List of classes where the index match the class id in the ONNX network
        # classes = model.parent.joinpath("classes.names").read_text().split("\n")
        # session = InferenceSession(
        #     model.as_posix(),
        #     providers=[
        #         "AzureExecutionProvider",
        #         "CPUExecutionProvider",
        #     ],
        # )

        # predictor = Predictor(session, classes)
        # img = Image.open(photo_full_path)
        # print(predictor.predict(img))

        ######### ONNX
        
        # Load the ONNX model
        # onnx_model_path = "whole/last_best.onnx"  # Replace with the actual path to your ONNX model file

        # # Create an ONNX Runtime Inference Session
        # ort_session = onnxruntime.InferenceSession(onnx_model_path)

        # # Define image transformations
        # def preprocess_image(image_path):
        #     image = Image.open(image_path).convert("RGB")
        #     image = image.resize((640, 640))  # Adjust the size based on your model's input size
        #     image = np.array(image).astype(np.float32) / 255.0
        #     image = np.transpose(image, (2, 0, 1))  # Change HWC to CHW
        #     image = np.expand_dims(image, axis=0)
        #     return image

        # # Load and preprocess the image
        # input_data = preprocess_image(photo_full_path)

        # # Perform inference
        # ort_inputs = {ort_session.get_inputs()[0].name: input_data}
        # ort_outputs = ort_session.run(None, ort_inputs)

        # print(np.array(ort_outputs).shape)

        # Process the output
        # boxes_classes = ort_outputs[0][0]
        # boxes_shapes = ort_outputs[1][0]
        # boxes_probs = ort_outputs[2][0]

        # for i in range(len(boxes_shapes)):
        #     class_, shape, prob = int(boxes_classes[i]), boxes_shapes[i], boxes_probs[i]
        #     # Process the results as needed
        #     print(f"Class: {class_}, Shape: {shape}, Probability: {prob}")

        ######### TORCH

        # model_path = "whole/best.pt"  # Replace with the actual path to your model file
        # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # if self.model == None:
        #     self.model = torch.load(model_path, map_location=device)
        #     self.model.eval()

        # # Define image transformations
        # transform = transforms.Compose([
        #     transforms.Resize((416, 416)),  # Adjust the size based on your model's input size
        #     transforms.ToTensor(),
        # ])

        # # Load and preprocess the image
        # image = Image.open(photo_full_path).convert("RGB")
        # image_tensor = transform(image).unsqueeze(0).to(device)

        # # Perform inference
        # with torch.no_grad():
        #     prediction = self.model(image_tensor)

        # # Process the prediction
        # boxes_classes = prediction[0].boxes.cls.cpu()
        # boxes_shapes = prediction[0].boxes.xywh.cpu()
        # boxes_probs = prediction[0].boxes.conf.cpu()

        # for i in range(len(boxes_shapes)):
        #     class_, shape, prob = boxes_classes[i], boxes_shapes[i], boxes_probs[i]
        #     # Process the results as needed
        #     print(f"Class: {class_}, Shape: {shape}, Probability: {prob}")

        ######## ULTRALYTICS

        if self.model == None:
            print("Loading YOLO Model... May take a while...")
            self.model = YOLO("whole/model.pt")
        
        prediction = self.model.predict(photo_full_path, save=False)

        boxes_classes = prediction[0].boxes.cls.cpu()
        boxes_shapes = prediction[0].boxes.xywh.cpu()
        boxes_probs = prediction[0].boxes.conf.cpu()

        for i in range(len(boxes_shapes)):
            class_, shape, prob = boxes_classes[i], boxes_shapes[i], boxes_probs[i]
            datas.add_box_photo(id_photo, int(class_), int(shape[0]) - int(float(shape[2])/2), int(shape[1]) - int(float(shape[3])/2), int(shape[2]), int(shape[3]), round(float(prob), 2))

    def remove_detect_photo(self):
        datas.remove_stats_current_photo()

    def close_photo(self):
        datas.set_current_photo("")
    

    ### ESPECES ###

    def add_specie(self):
        oizo_window = datas.get_widget("oizo_window")
        text, ok = QInputDialog.getText(oizo_window, "Ajout d'une espèce", "Saisir le nom de l'espèce que vous souhaitez rajouter à l'application : ")

        if ok and text != "":
            print("Adding specie", text)
            datas.add_specie(text)
        
        else:
            print("Specie adding aborted")

    def remove_specie(self, id, nom):
        print("Asking for deleting specie ", nom)
        oizo_window: QMainWindow = datas.get_widget("oizo_window")
        confirmation = QMessageBox.question(oizo_window, "Enlever l'espèce " + nom, "Êtes-vous certain de vouloir enlever cette espèce : " + nom + " ?\nLes données statistiques associées à cette espèce seront supprimées.", QMessageBox.Yes | QMessageBox.No)

        if confirmation == QMessageBox.Yes:
            print("Confirmed specie deletion")
            print("Removing specie...")
            datas.remove_specie(id)
        
        else:
            print("Aborted.")
