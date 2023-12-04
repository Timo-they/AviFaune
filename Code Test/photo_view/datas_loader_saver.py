
from datas import *

import json

def app_load_datas():
    print("Loading datas...")

    if os.path.isfile("datas.json"):
        with open('datas.json') as f:
            datas: dict = json.load(f)
            print("Opened datas file")

            if datas["series"] != None:
                app_set_series(datas["series"])
                print("Has serie : ", app_get_series())
            
            if datas["stats"] != None:
                app_set_stats(datas["stats"])
                print("Has serie : ", app_get_stats())

    


def app_save_datas():
    print("Saving datas...")

    datas = {
        "series": app_get_series(),
        "stats": app_get_stats()
    }
    
    with open('datas.json', 'w') as f:
        json.dump(datas, f)