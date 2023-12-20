

import time
import datetime

import datas
import os
import copy

def scan_serie():
    print("Scanning the serie")
    path_to_scan = datas.get_current_serie_path()

    if not os.path.exists(path_to_scan):
        serie = datas.get_current_serie()
        datas.set_current_serie("")
        datas.remove_serie(serie)
        return

    # TODO : limiter le nombre de photos à 500
    
    photos = {}
    photos_date = {}
    id = "0"
    
    files = os.listdir(path_to_scan)
    month = None
    
    for file in files:
        if os.path.isfile(path_to_scan + file):
            if os.path.splitext(file)[1] in  [".jpg", ".JPG", ".jpeg", ".png"]:
                date = time.ctime(os.path.getmtime(path_to_scan + file))
                photos[file] = date
    
    print(photos)
    
    for photo in range(len(photos)):

        date1 = datetime.datetime(1945,1,1,12,0,0)
        right_file = list(photos.keys())[0]
           
        for items in photos.items():
            
            date = str(items[1]).split()
            file = items[0]
                   
            year = int(date[4])
                    
            if date[1]=="Jan": month=1
            if date[1]=="Feb": month=2
            if date[1]=="Mar": month=3
            if date[1]=="Apr": month=4
            if date[1]=="May": month=5
            if date[1]=="Jun": month=6
            if date[1]=="Jul": month=7
            if date[1]=="Aug": month=8
            if date[1]=="Sep": month=9
            if date[1]=="Oct": month=10
            if date[1]=="Nov": month=11
            if date[1]=="Dec": month=12

            day = int(date[2])
            clock = date[3].split(':')
            heure = int(clock[0])
            minute = int(clock[1])
            seconde = int(clock[2])
            date2 = datetime.datetime(year,month,day,heure,minute,seconde)
                    
            if date2 > date1:
                right_file = file
                date1 = date2
            
        photos_date[id] = right_file
        id = str(int(id)+1)
        photos.pop(right_file)

    print(photos_date)
         
    datas.set_photos(photos_date)

    stats_serie = copy.deepcopy(datas.get_stats_serie())
    for name, stats_photo in stats_serie.items():
        if (not name in datas.get_photos().values()):
            if name != "global":
                datas.remove_stats_current_photo_from_name(name)

