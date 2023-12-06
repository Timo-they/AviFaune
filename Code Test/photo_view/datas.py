
import os
import whole.datas_loader_saver as datas_loader_saver
import whole.serie_scanner as serie_scanner


# Les couleurs pour print dans le terminal
COLOR_BLACK = '\u001b[30m'
COLOR_RED = '\u001b[31m'
COLOR_GREEN = '\u001b[32m' # J'ai décidé que c'était pour print les titres de l'app
COLOR_YELLOW = '\u001b[33m'
COLOR_BLUE = '\u001b[34m'
COLOR_MAGENTA = '\u001b[35m'
COLOR_CYAN = '\u001b[36m'

COLOR_BRIGHT_BLACK =  '\u001b[30;1m' # J'ai décidé que c'était pour print les grosses datas (toutes les séries, toutes les stats)
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
}

def get_widget(name: str):
    return widgets_[name]

def set_widget(name: str, widget):
    widgets_[name] = widget


# SERIES
global series_

# C'est le dictionnaire avec toutes les séries enregistrées
# UNE DES DEUX DATAS SAUVEGARDEE
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

    set_current_serie(str(max_id+1))

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
    return os.path.basename(os.path.dirname(series_[current_serie_]))

def get_current_serie_path():
    return series_[current_serie_]

def set_current_serie(new_serie: str):
    global current_serie_, datas_loader_saver
    print(COLOR_BRIGHT_MAGENTA, "Data setting serie from ", get_current_serie(), " to ", new_serie, COLOR_RESET)
    
    current_serie_ = new_serie

    if get_current_photo() != "":
        set_current_photo("")

    if new_serie != "":
        serie_scanner.scan_serie()

    # Met à jour pour que la bonne série soit affichée à l'écran
    get_widget("serie_view").update()
    get_widget("central_view").update()
    get_widget("bottom_layout").update_selected_serie()
    get_widget("menu_bar_handler").update()


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

def get_current_photo_full_path():
    return get_current_serie_path() + photos_[current_photo_]

def set_current_photo(new_photo: str):
    global current_photo_
    last_photo = get_current_photo()

    print(COLOR_BRIGHT_MAGENTA, "Data setting photo from ", last_photo, " to ", new_photo, COLOR_RESET)
    current_photo_ = new_photo

    # Met à jour pour que la bonne photo soit affichée à l'écran
    get_widget("bottom_layout").update_selected_photo(last_photo, new_photo)
    get_widget("top_layout").update()
    get_widget("central_view_photo").update()
    get_widget("menu_bar_handler").update()


# STATS
global stats_

# C'est le dictionnaire avec toutes les stats enregistrées
# UNE DES DEUX DATAS SAUVEGARDEE
stats_: dict = {}
# {
#     #ID of serie
#     "0": {
#         "pingouin.png": {
#             "pingouin_count": 1
#         }
#     }
#}

def get_stats():
    return stats_

def get_stats_serie():
    stats = stats_.get(current_serie_)
    if stats == None:
        return {}
    
    return stats

def get_stats_photo():
    serie_stats = stats_.get(current_serie_)
    if serie_stats == None:
        return {}
    
    stats = serie_stats.get(current_photo_)
    if stats == None:
        return {}
    
    return stats

def set_stats(new_stats: dict):
    global datas_loader_saver, stats_
    print(COLOR_BLACK, "Data setting stats from ", get_stats(), " to ", new_stats, COLOR_RESET)
    stats_ = new_stats

    # TODO : Update UI

    datas_loader_saver.save_datas()

def add_photo_stats(id_serie: str, id_photo: str, photo_stats: dict):
    global datas_loader_saver
    print(COLOR_BRIGHT_MAGENTA, "Data adding stat for the photo ", id_photo, " of serie ", id_serie, " with stats ", photo_stats, COLOR_RESET)

    stats_[id_serie][photos_[current_photo_]] = photo_stats

    # TODO : Update UI

    datas_loader_saver.save_datas()

def remove_stat(id_serie: str, id_photo: str):
    global datas_loader_saver
    print(COLOR_BRIGHT_MAGENTA, "Data removing stat for the photo ", id_photo, " of serie ", id_serie, COLOR_RESET)

    del stats_[id_serie][photos_[current_photo_]]

    # TODO : Update UI
    
    datas_loader_saver.save_datas()
