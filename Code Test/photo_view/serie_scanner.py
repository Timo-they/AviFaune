

from datas import *


def app_scan_serie():
    path_to_scan = app_get_current_serie_path()

    # TODO
    new_photos = {}

    files = os.listdir(path_to_scan)
    id = "0"
    
    for file in files:
        if os.path.isfile(path_to_scan + file):
            #print("Found file :", file)
            if os.path.splitext(file)[1] in [".jpg", ".JPG", ".jpeg", ".png"]:
                new_photos[id] = file
        
                id = str(int(id)+1)

    app_set_photos(new_photos)

    for name in app_get_stats_serie():
        pass

