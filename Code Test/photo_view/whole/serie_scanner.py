

import datas
import os

def scan_serie():
    print("Scanning the serie")
    path_to_scan = datas.get_current_serie_path()
    new_photos = {}

    # TODO : Si le chemin n'existe pas faudrait supprimer la série

    files = os.listdir(path_to_scan)
    id = "0"
    
    for file in files:
        if os.path.isfile(path_to_scan + file):

            # Please add extensions that should be handled
            if os.path.splitext(file)[1] in [".jpg", ".JPG", ".jpeg", ".png"]:
                new_photos[id] = file
        
                id = str(int(id)+1)

    datas.set_photos(new_photos)

    # TODO : Juste si y'a une image qui y est plus, on supprime ses stats associées
    
    for name in datas.get_stats_serie():
        pass

