
import os
import whole.datas_loader_saver as datas_loader_saver
import whole.serie_scanner as serie_scanner

COLOR_BLACK = '\u001b[30m'
COLOR_RED = '\u001b[31m'
COLOR_GREEN = '\u001b[32m'
COLOR_YELLOW = '\u001b[33m'
COLOR_BLUE = '\u001b[34m'
COLOR_MAGENTA = '\u001b[35m'
COLOR_CYAN = '\u001b[36m'

COLOR_BRIGHT_BLACK =  '\u001b[30;1m'
COLOR_BRIGHT_RED = '\u001b[31;1m'
COLOR_BRIGHT_GREEN = '\u001b[32;1m'
COLOR_BRIGHT_YELLOW = '\u001b[33;1m'
COLOR_BRIGHT_BLUE = '\u001b[34;1m'
COLOR_BRIGHT_MAGENTA = '\u001b[35;1m'
COLOR_BRIGHT_CYAN = '\u001b[36;1m'

COLOR_RESET = '\u001b[0m'


# WIDGETS
global widgets_

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

series_: dict = {}

def get_series():
    return series_

def set_series(new_series: dict):
    print(COLOR_BLACK, "Data setting series from ", get_current_serie(), " to ", new_series, COLOR_RESET)
    global series_
    series_ = new_series

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
    set_current_serie(str(max_id+1))

def remove_serie(id: str):
    global datas_loader_saver
    print(COLOR_BRIGHT_MAGENTA, "Data removing serie ", id, COLOR_RESET)

    if get_current_serie == id:
        set_current_serie("")
    
    series_.pop(id)
    get_widget("serie_view").update()
    get_widget("menu_bar_handler").update()

    datas_loader_saver.save_datas()

# CURRENT SERIE
global current_serie_

current_serie_: str = ""

def get_current_serie() -> str:
    return current_serie_

def get_current_serie_name() -> str:
    return os.path.basename(os.path.dirname(series_[current_serie_]))

def get_current_serie_path():
    return series_[current_serie_]

def set_current_serie(new_serie: str):
    print(COLOR_BRIGHT_MAGENTA, "Data setting serie from ", get_current_serie(), " to ", new_serie, COLOR_RESET)
    global current_serie_, datas_loader_saver
    current_serie_ = new_serie

    if get_current_photo() != "":
        set_current_photo("")

    if new_serie != "":
        serie_scanner.scan_serie()

    get_widget("serie_view").update()
    get_widget("central_view").update()
    get_widget("bottom_layout").update_selected_serie()
    get_widget("menu_bar_handler").update()


# PHOTOS
global photos_

photos_: dict = {}

def get_photos():
    return photos_

def set_photos(new_photos: dict):
    print(COLOR_BLACK, "Data setting photos from ", get_photos(), " to ", new_photos, COLOR_RESET)
    global photos_
    photos_ = new_photos

# CURRENT PHOTO
global current_photo_

current_photo_: str = ""

def get_current_photo():
    return current_photo_

def get_current_photo_name():
    return photos_[current_photo_]

def get_current_photo_full_path():
    return get_current_serie_path() + photos_[current_photo_]

def set_current_photo(new_photo: str):
    last_photo = get_current_photo()
    print(COLOR_BRIGHT_MAGENTA, "Data setting photo from ", last_photo, " to ", new_photo, COLOR_RESET)
    global current_photo_
    current_photo_ = new_photo

    get_widget("bottom_layout").update_selected_photo(last_photo, new_photo)
    get_widget("top_layout").update()
    get_widget("central_view_photo").update()
    get_widget("menu_bar_handler").update()


# STATS
global stats_

stats_: dict = {}
# {
#     #ID of serie
#     0: {
#         "pingouin.png": {
#             "pingouin_count": 1
#         }
#     }
#}

def get_stats():
    return stats_

def get_stats_serie():
    if not current_serie_ in stats_.keys():
        return {}
    return stats_[current_serie_]


def set_stats(new_stats: dict):
    print(COLOR_BLACK, "Data setting photos from ", get_stats(), " to ", new_stats, COLOR_RESET)
    global stats_
    stats_ = new_stats

def add_photo_stats(id_serie: str, id_photo: str, photo_stats: dict):
    stats_[id_serie][photos_[current_photo_]] = photo_stats

def remove_stat(id_serie: str, id_photo: str):
    del stats_[id_serie][photos_[current_photo_]]
