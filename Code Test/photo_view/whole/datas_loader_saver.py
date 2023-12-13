
import datas
import os

import json

def load_datas():
    print(datas.COLOR_MAGENTA, "Loading datas...", datas.COLOR_RESET)

    if os.path.isfile("datas.json"):
        with open('datas.json') as f:
            datas_: dict = json.load(f)
            print("Opened datas file")

            if datas_.get("series") != None:
                datas.set_series(datas_["series"])
                print(datas.COLOR_BLACK, "Loaded series : ", datas.get_series(), datas.COLOR_RESET)
            
            if datas_.get("stats") != None:
                datas.set_stats(datas_["stats"])
                print(datas.COLOR_BLACK, "Loaded stats : ", datas.get_stats(), datas.COLOR_RESET)
            
            if datas_.get("species") != None:
                datas.set_species(datas_["species"])

                # D'accord c'est hard codé, mais isoké
                datas.set_species({
                    "0": "Bécasseau Sanderling",
                    "1": "Bernache Cravant",
                    "2": "Goéland Argenté",
                    "3": "Mouette Rieuse",
                    "4": "Pluvier Argenté",
                })
                print(datas.COLOR_BLACK, "Loaded species : ", datas.get_species(), datas.COLOR_RESET)
            
            datas.set_species({
                "0": "Bécasseau Sanderling",
                "1": "Bernache Cravant",
                "2": "Goéland Argenté",
                "3": "Mouette Rieuse",
                "4": "Pluvier Argenté",
            })
    
    else:
         print("Datas file not found. Creating it...")
         save_datas()


def save_datas():
    print(datas.COLOR_MAGENTA, "Saving datas...", datas.COLOR_RESET)

    datas_ = {
        "series": datas.get_series(),
        "stats": datas.get_stats(),
        "species": datas.get_species()
    }
    
    with open('datas.json', 'w') as f:
            json.dump(datas_, f)
        
    # NOTE : Ce serait possible aussi de sauvegarder les stats dans un dossier .torda/ dans le 
    # dossier de série. Ca ferait que les données soient cachées, mais retrouvables facilement. Aussi, 
    # si le dossier est déplacé, les stats sont conservées.
    # Point bonus : si l'application est désinstallée puis réinstallée, les stats sont encore là