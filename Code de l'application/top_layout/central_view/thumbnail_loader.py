



import time
import traceback, sys
import exifread

from PyQt5.QtGui import QPixmap, QIcon, QTransform
from PyQt5.QtCore import QObject, QThread, QRect, Qt, pyqtSignal, QRunnable, pyqtSlot

import datas



class ThumbnailLoader(QRunnable):

    photos: dict
    serie: int
    serie_path: str

    placeholder: QPixmap

    def __init__(self, placeholder: QPixmap) -> None:
        super(ThumbnailLoader, self).__init__()

        self.photos = datas.get_photos()
        self.serie = datas.get_current_serie()
        self.serie_path = datas.get_current_serie_path()
        self.placeholder = placeholder
        
        print("Init of ThumbnailLoader")

    # La fonction exécutée dans un autre thread
    @pyqtSlot()
    def run(self):
        print("Starting loading thread of size : ", len(self.photos))

        for id, path in self.photos.items():
             #icon = self.load_thumbnail(path)
            if datas.get_current_serie() == self.serie:
                icon = self.load_thumbnail(path)

                if datas.get_current_serie() == self.serie:
                    print("Loaded pic ", path)
                    datas.get_widget("central_view").set_thumbnail_photo(icon, id, self.serie)#thumbnail_buttons[id].setIcon(icon)
                    datas.get_widget("bottom_layout").set_thumbnail_photo(icon, id, self.serie)#thumbnail_buttons[id].setIcon(icon)
                    
                else:
                    print(datas.COLOR_BRIGHT_RED, "ThumbnailLoader stilla active, tho changed serie")
            else:
                print(datas.COLOR_BRIGHT_RED, "ThumbnailLoader stilla active, tho changed seriee")
    
    def load_thumbnail(self, path: str) -> QPixmap:
        photo_pixmap = QPixmap(self.serie_path + path)

        with open(self.serie_path + path, 'rb') as pix:
            tags = exifread.process_file(pix)
            rotate90 = QTransform().rotate(90)
            rotate270 = QTransform().rotate(270)

            if "Image Orientation" in tags.keys():
                val = tags["Image Orientation"].values
                if 6 in val :
                    photo_pixmap = photo_pixmap.transformed(rotate90)
                if 8 in val :
                    photo_pixmap = photo_pixmap.transformed(rotate270)

        # TODO : Si la photo ne charge pas, l'enlève des photos

        #On rend d'abord la photo en temps que carré 1024x1024px (ici, on ne fait que la réduire en taille pour que son plus petit coté fasse 1024px)
        photo_pixmap_overscaled = photo_pixmap.scaled(1024, 1024, aspectRatioMode=Qt.KeepAspectRatioByExpanding)

        #On centre le carré sur l'image, car c'est souvent au centre de la photo ce qui est intéressant
        aleft = (photo_pixmap_overscaled.width() - 1024) // 2
        atop = (photo_pixmap_overscaled.height() - 1024) // 2
        photo_pixmap_overscaled_cropped = photo_pixmap_overscaled.copy(QRect(aleft, atop, 1024, 1024))

        #Ensuite on la réduit de taille d'un facteur 4 avec un smooth, qui permet d'avoir un joli rendu
        final_pixmap = photo_pixmap_overscaled_cropped.scaled(256, 256, transformMode=Qt.SmoothTransformation)



        return QIcon(final_pixmap)



class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done