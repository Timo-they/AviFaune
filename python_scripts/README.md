 # # # # # # # # # GUI FUNCTIONS # # # # # # # # # 

# GUI Principal
setup_ui() 

# GUI Bindings pour Fichier
switch_to_file_menu()
update_file_menu(series: dict)

# GUI Bindings pour Série
switch_to_serie_menu()
update_serie_menu(id_serie: int, series: dict)
update_serie_statistique(id_serie: int, series: dict)
refresh_photos_from_serie(id_serie: int, series: dict)

# GUI Bindings pour Photo
switch_to_photo_menu()
update_photo_menu(name_photo: str, id_serie: int, series: dict)
show_photo(name_photo: str, id_serie: int, series: dict)

 # # # # # # # # # MAIN FUNCTIONS # # # # # # # # # 

# Menu déroulant Fichier
Bouton Fichier->Ouvrir -> open_folder(folder_path: str)
Bouton Fichier->Exporter les statistiques -> export_stats()

# Menu déroulant Série
Bouton Série->Détection automatique des oiseaux -> detect_oizos()

# Tous les menus
Clique sur une série sur menu de gauche -> open_serie(id_serie: int)

# Menu Série
Clique sur une photo de la série en bas ou au milieu -> open_photo(name_photo: str)

# Menu Photo
Clique sur une photo de la série en bas -> open_photo(name_photo: str)
Clique sur flèche droite -> open_next_photo()
Clique sur flèche gauche -> open_previous_photo()
