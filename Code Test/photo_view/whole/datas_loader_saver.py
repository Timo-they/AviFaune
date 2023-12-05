
import datas
import os

import json

def load_datas():
    print(datas.COLOR_MAGENTA, "Loading datas...", datas.COLOR_RESET)

    if os.path.isfile("datas.json"):
        with open('datas.json') as f:
            datas_: dict = json.load(f)
            print("Opened datas file")

            if datas_["series"] != None:
                datas.set_series(datas_["series"])
                print(datas.COLOR_BLACK, "Loaded series : ", datas.get_series(), datas.COLOR_RESET)
            
            if datas_["stats"] != None:
                datas.set_stats(datas_["stats"])
                print(datas.COLOR_BLACK, "Loaded stats : ", datas.get_stats(), datas.COLOR_RESET)


def save_datas():
    print(datas.COLOR_MAGENTA, "Saving datas...", datas.COLOR_RESET)

    datas_ = {
        "series": datas.get_series(),
        "stats": datas.get_stats()
    }
    
    with open('datas.json', 'w') as f:
            json.dump(datas_, f)