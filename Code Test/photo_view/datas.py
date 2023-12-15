
import os
import whole.datas_loader_saver as datas_loader_saver
import whole.serie_scanner as serie_scanner


# Les couleurs pour print dans le terminal
COLOR_BLACK = '\u001b[30m' # J'ai décidé que c'était pour print les grosses datas (toutes les séries, toutes les stats)
COLOR_RED = '\u001b[31m'
COLOR_GREEN = '\u001b[32m' # J'ai décidé que c'était pour print les titres de l'app
COLOR_YELLOW = '\u001b[33m'
COLOR_BLUE = '\u001b[34m'
COLOR_MAGENTA = '\u001b[35m'
COLOR_CYAN = '\u001b[36m'

COLOR_BRIGHT_BLACK =  '\u001b[30;1m'
COLOR_BRIGHT_RED = '\u001b[31;1m' # J'ai décidé que c'était pour print les erreurs
COLOR_BRIGHT_GREEN = '\u001b[32;1m'
COLOR_BRIGHT_YELLOW = '\u001b[33;1m'
COLOR_BRIGHT_BLUE = '\u001b[34;1m' # J'ai décidé que c'était pour print les widgets
COLOR_BRIGHT_MAGENTA = '\u001b[35;1m' # J'ai décidé que c'était pour print les petites datas (changement d'id)
COLOR_BRIGHT_CYAN = '\u001b[36;1m'

COLOR_RESET = '\u001b[0m'


# WIDGETS
global widgets_

# C'est un dictionnaire qui contient tous les widgets utiles de l'application (on peut en rajouter).
# Il est rempli une fois que l'instantation de la fenêtre est finie.
widgets_: dict = {
    "oizo_window": None,
    "top_layout": None,
    "bottom_layout": None,
    "menu_bar_handler": None,
    "serie_view": None,
    "central_view": None,
    "central_view_photo": None,
    "central_photo": None,
}

def get_widget(name: str):
    if widgets_.get(name) == None:
        print(COLOR_BRIGHT_RED, "1. There is no ", name, " in ", widgets_, COLOR_RESET)
        return
    
    return widgets_[name]

def set_widget(name: str, widget):
    widgets_[name] = widget


# SERIES
global series_

# C'est le dictionnaire avec toutes les séries enregistrées
# UNE DES TROIS DATAS SAUVEGARDEE
series_: dict = {}
# {
#    "0": "/home/arthur/pingouins/",
#    "1": "/home/arthur/tortues/",
# }

def get_series():
    return series_

def set_series(new_series: dict):
    global series_
    print(COLOR_BLACK, "Data setting series from ", get_current_serie(), " to ", new_series, COLOR_RESET)

    series_ = new_series

    # Met à jour pour que la liste de série soit actualisée sur l'interface
    get_widget("serie_view").update()
    get_widget("menu_bar_handler").update()

    datas_loader_saver.save_datas()

def add_serie(path: str):
    global datas_loader_saver
    max_id = 0

    for id in series_.keys():
        if int(id) > max_id:
            max_id = int(id)

    print(COLOR_BRIGHT_MAGENTA, "Data adding serie ", path, " as ", max_id+1, COLOR_RESET)

    series_[str(max_id+1)] = path
    print(COLOR_BLACK, "Data new series ", series_, COLOR_RESET)

    # set_current_serie(str(max_id+1))

    get_widget("serie_view").update()
    get_widget("menu_bar_handler").update()

    datas_loader_saver.save_datas()

def remove_serie(id: str):
    global datas_loader_saver
    print(COLOR_BRIGHT_MAGENTA, "Data removing serie ", id, COLOR_RESET)

    if get_current_serie == id:
        set_current_serie("")
    
    series_.pop(id)
    print(COLOR_BLACK, "Data new series ", series_, COLOR_RESET)

    # Met à jour pour que la liste de série soit actualisée sur l'interface
    get_widget("serie_view").update()
    get_widget("menu_bar_handler").update()

    datas_loader_saver.save_datas()

# CURRENT SERIE
global current_serie_

# C'est l'id de la série actuellement sélectionnée
# Si l'id n'est pas "", la série est directement affichée à l'écran
# Si l'id est "", il n'y a plus de série affichée à l'écran
# C'est un str parce que json ne prend que des strings
current_serie_: str = ""
# "" -> Aucune série sélectionnée
# "0" -> Série 0 sélectionnée

def get_current_serie() -> str:
    return current_serie_

def get_current_serie_name() -> str:
    if series_.get(current_serie_) == None:
        print(COLOR_BRIGHT_RED, "2. There is no ", current_photo_, " in ", photos_, COLOR_RESET)
        return
    
    return os.path.basename(os.path.dirname(series_[current_serie_]))

def get_current_serie_path():
    if series_.get(current_serie_) == None:
        print(COLOR_BRIGHT_RED, "3. There is no ", current_photo_, " in ", photos_, COLOR_RESET)
        return
    
    return series_[current_serie_]

def set_current_serie(new_serie: str):
    global current_serie_, datas_loader_saver
    print(COLOR_BRIGHT_MAGENTA, "Data setting serie from ", get_current_serie(), " to ", new_serie, COLOR_RESET)
    
    current_serie_ = str(new_serie)

    if get_current_photo() != "":
        set_current_photo("")

    if new_serie != "":
        serie_scanner.scan_serie()

    # Met à jour pour que la bonne série soit affichée à l'écran
    get_widget("serie_view").update()
    get_widget("bottom_layout").update()
    get_widget("bottom_layout").update_selected_serie()
    get_widget("central_view").update()
    get_widget("menu_bar_handler").update()
    get_widget("stat_view").update()


# PHOTOS
global photos_

# C'est le dictionnaire avec toutes les photos de la série actuelle
# Mis à jour directement au changement de série
photos_: dict = {}
# {
#    "0": "pingouin.png",
#    "1": "pingouin1.png",
# }

def get_photos():
    return photos_

def set_photos(new_photos: dict):
    global photos_
    print(COLOR_BLACK, "Data setting photos from ", get_photos(), " to ", new_photos, COLOR_RESET)

    photos_ = new_photos

# CURRENT PHOTO
global current_photo_

# C'est l'id de la photo actuellement sélectionnée
# Si l'id n'est pas "", la photo est directement affichée à l'écran
# Si l'id est "", alors la vue de série est affichée
current_photo_: str = ""
# "" -> Aucune série sélectionnée
# "0" -> Photo 0 sélectionnée

def get_current_photo():
    return current_photo_

def get_current_photo_name():
    return photos_[current_photo_]

def get_current_photo_full_path(id_photo_to_get = None):
    if id_photo_to_get == None:
        id_photo_to_get = current_photo_
    
    if photos_.get(id_photo_to_get) == None:
        print(COLOR_BRIGHT_RED, "4. There is no ", id_photo_to_get, " in ", photos_, COLOR_RESET)
        return
    
    return get_current_serie_path() + photos_[id_photo_to_get]

def set_current_photo(new_photo: str):
    global current_photo_
    last_photo = get_current_photo()

    print(COLOR_BRIGHT_MAGENTA, "Data setting photo from ", last_photo, " to ", new_photo, COLOR_RESET)
    current_photo_ = str(new_photo)

    # Met à jour pour que la bonne photo soit affichée à l'écran
    get_widget("bottom_layout").update_selected_photo(last_photo, new_photo)
    get_widget("top_layout").update()
    get_widget("central_view_photo").update()
    get_widget("menu_bar_handler").update()
    get_widget("stat_view").update()
    get_widget("central_photo").update_boxes()


# SPECIES
global species_

BASE_SPECIES: dict = {
    "0": "Bécasseau Sanderling",
    "1": "Bernache Cravant",
    "2": "Goéland Argenté",
    "3": "Mouette Rieuse",
    "4": "Pluvier Argenté",
}

# C'est le dictionnaire avec toutes les espèces enregistrables
# UNE DES TROIS DATAS SAUVEGARDEE
species_: dict = {}
# "-1" is for "Autre" category

def get_species():
    return BASE_SPECIES | species_ | {"-1": "Autre"}

def get_only_newly_added_species():
    return species_

def get_specie_name(id_specie: str):
    return get_species()[id_specie]

def set_species(new_species: dict):
    global datas_loader_saver, species_
    last_species = get_species()
    species_ = new_species

    print(COLOR_BLACK, "Data setting species from ", last_species, " to ", get_species(), COLOR_RESET)

    get_widget("stat_view").update()
    get_widget("menu_bar_handler").update()

    datas_loader_saver.save_datas()

def add_specie(new_specie: str):
    global datas_loader_saver
    max_id = 0

    for id in get_species().keys():
        if int(id) > max_id:
            max_id = int(id)

    print(COLOR_BRIGHT_MAGENTA, "Data adding specie ", new_specie, " as ", max_id+1, COLOR_RESET)

    species_[str(max_id+1)] = new_specie
    print(COLOR_BLACK, "Data new species ", get_species(), COLOR_RESET)

    get_widget("stat_view").update()
    get_widget("menu_bar_handler").update()

    datas_loader_saver.save_datas()

def remove_specie(id_specie: str):
    global datas_loader_saver
    print(COLOR_BRIGHT_MAGENTA, "Data removing specie ", species_[id_specie], " with id : ", id_specie, COLOR_RESET)

    del species_[id_specie]

    get_widget("stat_view").update()
    get_widget("menu_bar_handler").update()

    # TODO : Remove all stats that uses that specie
    
    datas_loader_saver.save_datas()


# STATS
global stats_

# C'est le dictionnaire avec toutes les stats enregistrées
# UNE DES TROIS DATAS SAUVEGARDEE
stats_: dict = {}
# {
#     #ID of serie
#     "0": {
#         "global": {
#             "0": "1"  #ID of specie -> number of oizos
#         },
#         "pingouin.png": { # Nom image
#             "-1": { # ID box
#               "specie": "2"
#               "x": "165", # Coordinates box
#               "y": "35",
#               "w": "55",
#               "h": "250"
#               }
#         }
#     }
#}

def get_stats():
    return stats_

def get_stats_serie():
    stats = stats_.get(current_serie_)
    if stats == None:
        print("1. There is no stats for the serie ", current_serie_)
        return {}
    
    return stats

def get_stats_global_serie():
    serie_stats = stats_.get(current_serie_)
    if serie_stats == None:
        print("2. There is no stats for the serie ", current_serie_)
        return {}
    
    stats = serie_stats.get("global")
    if stats == None:
        print("3. There is no global stats for the serie")
        return {}
    
    return stats

def get_boxes_current_photo():
    serie_stats = stats_.get(current_serie_)
    if serie_stats == None:
        print("4. There is no stats for the serie ", current_serie_)
        return {}

    if photos_.get(current_photo_) == None:
        print(COLOR_BRIGHT_RED, "5. There is no ", current_photo_, " in ", photos_, COLOR_RESET)
        return {}

    stats = serie_stats.get(photos_[current_photo_])
    if stats == None:
        print("5. There is no stat for the photo ", photos_[current_photo_])
        return {}
    
    return stats

def set_stats(new_stats: dict):
    global datas_loader_saver, stats_
    print(COLOR_BLACK, "Data setting stats from ", get_stats(), " to ", new_stats, COLOR_RESET)
    stats_ = new_stats

    get_widget("stat_view").update()
    get_widget("central_view").updated_stats()

    datas_loader_saver.save_datas()

# def set_global_serie_stat(id_serie: str, id_specie: str, count: str):
#     global datas_loader_saver
#     print(COLOR_BRIGHT_MAGENTA, "Data setting stat for serie ", id_serie, ", has ", count, " of specie ", id_specie, COLOR_RESET)

#     stats_[id_serie]["global"] = count

#     get_widget("stat_view").update()

#     datas_loader_saver.save_datas()

# def set_photo_stat(id_serie: str, id_photo: str, id_specie: str, count : str):
#     global datas_loader_saver
#     print(COLOR_BRIGHT_MAGENTA, "Data adding stat for the photo ", id_photo, " of serie ", id_serie, ", has ", count, " of specie ", id_specie, COLOR_RESET)

#     serie_stats = stats_.get(current_serie_)
#     if serie_stats == None:
#         print("There is no stats for the serie ", current_serie_)
#         return {}
    
#     stats = serie_stats.get(current_photo_)
#     if stats == None:
#         print("There is no stat for the photo ", current_photo_)
#         return {}
    
#     stats_[id_serie][photos_[id_photo]][id_specie] = count
    
#     # TODO: Recalculate stat of the whole serie
#     print("TODO : Recalculate stats of the whole serie")

#     get_widget("stat_view").update()

#     datas_loader_saver.save_datas()

def set_stats_global_serie(stats: dict):
    global datas_loader_saver
    print(COLOR_BRIGHT_MAGENTA, "Data setting global for ", get_current_serie(), " to ", stats, COLOR_RESET)

    if not stats_.get(current_serie_):
        stats_[current_serie_] = {}
    
    stats_[current_serie_]["global"] = stats

    get_widget("stat_view").update()
    get_widget("central_view").updated_stats()

    datas_loader_saver.save_datas()

def add_box_photo(id_photo: str, id_specie: str, x: str, y: str, w: str, h: str, prob: float):
    global datas_loader_saver
    print(COLOR_BRIGHT_MAGENTA, "Data adding box for photo ", id_photo, " : ", id_specie, x, y, w, h, prob, COLOR_RESET)

    if not stats_.get(current_serie_):
        stats_[current_serie_] = {}
    
    if photos_.get(id_photo) == None:
        print(COLOR_BRIGHT_RED, "6. There is no ", id_photo, " in ", photos_, COLOR_RESET)
        return
    
    if not stats_[current_serie_].get(photos_[id_photo]):
        stats_[current_serie_][photos_[id_photo]] = {}

    max_id = 0

    for id in stats_[current_serie_][photos_[id_photo]].keys():
        if int(id) > max_id:
            max_id = int(id)
    
    print(COLOR_BRIGHT_MAGENTA, "Data adding box ", id_specie, x, y, w, h, prob, " as ", max_id+1, COLOR_RESET)

    stats_[current_serie_][photos_[id_photo]][str(max_id+1)] = {
        "specie": str(id_specie),
        "x": str(x),
        "y": str(y),
        "w": str(w),
        "h": str(h),
        "prob": str(prob)
    }
    
    calculate_serie_stats()

    get_widget("stat_view").update()
    get_widget("central_photo").update_boxes()
    get_widget("central_view").updated_stats()

    datas_loader_saver.save_datas()

def remove_stats_current_photo(id_photo_to_remove_stats = None):
    global datas_loader_saver

    if id_photo_to_remove_stats == None:
        id_photo_to_remove_stats = current_photo_

    print(COLOR_BRIGHT_MAGENTA, "Data removing stats for the photo ", id_photo_to_remove_stats, " of serie ", current_serie_, COLOR_RESET)
    
    if photos_.get(id_photo_to_remove_stats) == None:
        print(COLOR_BRIGHT_RED, "7. There is no ", id_photo_to_remove_stats, " in ", photos_, COLOR_RESET)
        return
    
    if stats_.get(current_serie_) and stats_[current_serie_].get(photos_[id_photo_to_remove_stats]):
        del stats_[current_serie_][photos_[id_photo_to_remove_stats]]

    calculate_serie_stats()

    get_widget("stat_view").update()
    get_widget("central_photo").update_boxes()
    get_widget("central_view").updated_stats()
    
    datas_loader_saver.save_datas()

def calculate_serie_stats():
    print(COLOR_BRIGHT_MAGENTA, "Data calculating global for ", get_current_serie(), "...", COLOR_RESET)
    global_ = {}

    for photo_name, boxes in get_stats_serie().items():
        if photo_name == "global":
            continue
            
        for id, box in boxes.items():
            if box["specie"] in global_.keys():
                global_[box["specie"]] = str(int(global_[box["specie"]]) + 1)
            
            else:
                global_[box["specie"]] = 1
    
    set_stats_global_serie(global_)

    
