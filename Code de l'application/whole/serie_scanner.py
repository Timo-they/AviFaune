

import datas
import os
import copy

def scan_serie():
    print("Scanning the serie")
    path_to_scan = datas.get_current_serie_path()
    new_photos = {}

    if not os.path.exists(path_to_scan):
        serie = datas.get_current_serie()
        datas.set_current_serie("")
        datas.remove_serie(serie)
        return

    files = os.listdir(path_to_scan)
    id = "0"
    
    for file in files:
        if os.path.isfile(path_to_scan + file):

            # Please add extensions that should be handled
            if os.path.splitext(file)[1] in [".jpg", ".JPG", ".jpeg", ".png"]:
                new_photos[id] = file
        
                id = str(int(id)+1)
        
        # TODO : limiter le nombre de photos à 500

    datas.set_photos(new_photos)

    stats_serie = copy.deepcopy(datas.get_stats_serie())
    for name, stats_photo in stats_serie.items():
        if (not name in datas.get_photos().values()):
            if name != "global":
                datas.remove_stats_current_photo_from_name(name)

