


from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QObject, QThread, QRect, Qt, pyqtSignal, QRunnable, pyqtSlot

import datas



class ThumbnailLoader(QRunnable):

    photos: dict
    serie: int
    serie_path: str

    placeholder: QPixmap

    def __init__(self, placeholder: QPixmap) -> None:
        super().__init__()

        self.photos = datas.get_photos()
        self.serie = datas.get_current_serie()
        self.serie_path = datas.get_current_serie_path()
        self.placeholder = placeholder
        
        print("Init of ThumbnailLoader")

    
    @pyqtSlot()
    def run(self):
        print("Starting loading thread of size : ", len(self.photos))

        for id, path in self.photos.items():
            if datas.get_current_serie() == self.serie:
                icon = self.load_thumbnail(path)
                # TODO : load thumbnail

                if datas.get_current_serie() == self.serie:
                    print("Loaded pic ", path)
                    datas.get_widget("central_view").set_thumbnail_photo(icon, id, self.serie)#thumbnail_buttons[id].setIcon(icon)
                    pass
                    # TODO : Set button thumbnail
                else:
                    print(datas.COLOR_BRIGHT_RED, "ThumbnailLoader stilla active, tho changed serie")
            else:
                print(datas.COLOR_BRIGHT_RED, "ThumbnailLoader stilla active, tho changed seriee")
    
    def load_thumbnail(self, path: str) -> QPixmap:
        photo_pixmap = QPixmap(self.serie_path + path)

        #On rend d'abord la photo en temps que carré 1024x1024px (ici, on ne fait que la réduire en taille pour que son plus petit coté fasse 1024px)
        photo_pixmap_overscaled = photo_pixmap.scaled(1024, 1024, aspectRatioMode=Qt.KeepAspectRatioByExpanding)

        #On centre le carré sur l'image, car c'est souvent au centre de la photo ce qui est intéressant
        aleft = (photo_pixmap_overscaled.width() - 1024) // 2
        atop = (photo_pixmap_overscaled.height() - 1024) // 2
        photo_pixmap_overscaled_cropped = photo_pixmap_overscaled.copy(QRect(aleft, atop, 1024, 1024))

        #Ensuite on la réduit de taille d'un facteur 4 avec un smooth, qui permet d'avoir un joli rendu
        final_pixmap = photo_pixmap_overscaled_cropped.scaled(256, 256, transformMode=Qt.SmoothTransformation)

        return QIcon(final_pixmap)
