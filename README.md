# Projet Avifaune

Ce projet sera une application qui permettra de détecter des oiseaux sur des photos.

# Les fonctions du python_scriptse

Pour commencer, voici une description des différents paramètres qui seront utilisés par la suite :
 - series: dict est de la forme {id_serie: {folder: file_path, statistics: {name_photo1: {...}, name_photo2: {...}}}}, ex : {1: {"folder": "C:\Users\toiture\Pictures\Pingouins Torda", statistics: {"pingouin1.jpg": {"pingouins": 1, "mouettes": 0}}}}

## GUI Functions
#### GUI Principal
setup_ui() : Fonction qui initialise toute l'interface de l'application. A n'utiliser qu'au démarrage de l'application

#### GUI Bindings pour Fichier
switch_to_file_menu() : Fonction qui change la fenetre principale pour faire apparaître les widgets de la vue de fichier

update_file_menu(series: dict) : Fonction qui met à jour les widgets de la vue de fichier

#### GUI Bindings pour Série
switch_to_serie_menu() : Fonction qui change la fenêtre principale pour faire apparaître les widgets de la vue de série

update_serie_menu(id_serie: int, series: dict) : Fonction qui met à jour les widgets de la vue de série

update_serie_statistique(id_serie: int, series: dict) : Fonction qui met à jour les widgets de la partie de droite de statistique dans la vue de série

refresh_photos_from_serie(id_serie: int, series: dict) : Fonction qui met à jour la partie centrale et du bas de photos dans la vue de série

#### GUI Bindings pour Photo
switch_to_photo_menu() : Fonction qui change la fenêtre principale pour faire apparaître les widgets de la vue de photo

update_photo_menu(name_photo: str, id_serie: int, series: dict) : Fonction qui met à jour les widgets de la vue de photo

show_photo(name_photo: str, id_serie: int, series: dict) : Fonction qui change la photo en cours de visualisation par la photo photo_name

## MAIN FUNCTIONS

#### Menu déroulant Fichier
Bouton Fichier->Ouvrir -> open_folder(folder_path: str)

Bouton Fichier->Exporter les statistiques -> export_stats()

#### Menu déroulant Série
Bouton Série->Détection automatique des oiseaux -> detect_oizos()

#### Tous les menus
Clique sur une série sur menu de gauche -> open_serie(id_serie: int)

#### Menu Série
Clique sur une photo de la série en bas ou au milieu -> open_photo(name_photo: str)

#### Menu Photo
Clique sur une photo de la série en bas -> open_photo(name_photo: str)
Clique sur flèche droite -> open_next_photo()
Clique sur flèche gauche -> open_previous_photo()


#https://blog.aaronhktan.com/posts/2018/05/14/pyqt5-pyinstaller-executable
