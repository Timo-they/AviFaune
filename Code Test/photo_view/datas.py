
import os

# WIDGETS
global widgets_

widgets_: dict = {
    "oizo_window": None,
    "top_layout": None,
    "bottom_layout": None,
    "menu_bar_handler": None,
    "serie_view": None,
    "central_view": None,
}

def app_get_widget(name: str):
    return widgets_[name]

def app_set_widget(name: str, widget):
    widgets_[name] = widget


# SERIES
global series_

series_: dict = {}

def app_get_series():
    return series_

def app_set_series(new_series: dict):
    global series_
    series_ = new_series
    app_get_widget("serie_view").update()
    app_get_widget("menu_bar_handler").update()

def app_add_serie(path: str):
    max_id = 0

    for id in series_.keys():
        if int(id) > max_id:
            max_id = int(id)

    series_[max_id+1] = path

    print("Added ", path, " as ", max_id+1)
    app_get_widget("serie_view").update()
    app_get_widget("menu_bar_handler").update()

def app_remove_serie(id: str):
    print(series_)
    series_.pop(id)
    app_get_widget("serie_view").update()
    app_get_widget("menu_bar_handler").update()

# CURRENT SERIE
global current_serie_

current_serie_: str = ""

def app_get_current_serie() -> str:
    return current_serie_

def app_get_current_serie_name() -> str:
    return os.path.basename(os.path.dirname(series_[current_serie_]))

def app_get_current_serie_path():
    return series_[current_serie_]

def app_set_current_serie(id: str):
    global current_serie_
    current_serie_ = id
    app_get_widget("serie_view").update()
    app_get_widget("menu_bar_handler").update()
    app_get_widget("central_view").update()


# PHOTOS
global photos_

photos_: dict = {}

def app_get_photos():
    return photos_

def app_set_photos(new_photos: dict):
    global photos_
    photos_ = new_photos
    app_get_widget("central_view").update()

# CURRENT PHOTO
global current_photo_

current_photo_: str = ""

def app_get_current_photo():
    return current_photo_

def app_get_current_name():
    return photos_[current_photo_]

def app_get_current_full_path():
    return app_get_current_serie_path() + photos_[current_photo_]

def app_set_current_photo(id: str):
    global current_photo_
    current_photo_ = id


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

def app_get_stats():
    return stats_

def app_get_stats_serie():
    if not current_serie_ in stats_.keys():
        return {}
    return stats_[current_serie_]


def app_set_stats(new_stats: dict):
    global stats_
    stats_ = new_stats

def app_add_photo_stats(id_serie: str, id_photo: str, photo_stats: dict):
    stats_[id_serie][photos_[current_photo_]] = photo_stats

def app_remove_stat(id_serie: str, id_photo: str):
    del stats_[id_serie][photos_[current_photo_]]


