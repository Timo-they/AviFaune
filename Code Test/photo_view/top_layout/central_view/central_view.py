


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from datas import *
from top_layout.central_view.scroll_area_central import *
from top_layout.central_view.central_button import *


class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)

class CentralView(QWidget):

    view_box: QVBoxLayout
    title_label: QLabel
    # thumbnails_to_load: list

    def __init__(self, parent = None):
        super().__init__(parent)
        # self.threadpool = QThreadPool()

        palette = QPalette();

        palette.setColor(QPalette.Window, QColor("#303446"));

        self.setAutoFillBackground(True); 
        self.setPalette(palette)

        app_set_widget("central_view", self)

        self.build_central_view()

    def build_central_view(self):
        self.view_box = QVBoxLayout(self)

        self.title_label = QLabel("Aucune série sélectionnée")
        self.view_box.addWidget(self.title_label)
        print(self)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        self.view_box.addWidget(separator)

        scroll = ScrollAreaCentral()
        scroll_widget = scroll.widget
        self.view_box.addWidget(scroll)

        intermediate_vbox = QVBoxLayout(scroll_widget)
        self.central_grid = QGridLayout()
        self.central_grid.columnCount
        self.central_grid.setContentsMargins(4, 4, 4, 4)
        intermediate_vbox.addLayout(self.central_grid)

        intermediate_vbox.addWidget(QWidget())
    
    def update(self):
        if app_get_current_serie() == "":
            self.title_label.setText("Aucune série sélectionnée")
            return

        self.title_label.setText(app_get_current_serie_path())
        
        children = []
        for i in range(self.central_grid.count()):
            child = self.central_grid.itemAt(i).widget()
            if child:
                children.append(child)
        for child in children:
            child.deleteLater()

        photo_pixmap = QPixmap("placeholder-square.jpg")

        #On rend d'abord la photo en temps que carré 1024x1024px (ici, on ne fait que la réduire en taille pour que son plus petit coté fasse 1024px)
        photo_pixmap_overscaled = photo_pixmap.scaled(1024, 1024, aspectRatioMode=Qt.KeepAspectRatioByExpanding)

        #On centre le carré sur l'image, car c'est souvent au centre de la photo ce qui est intéressant
        aleft = (photo_pixmap_overscaled.width() - 1024) // 2
        atop = (photo_pixmap_overscaled.height() - 1024) // 2
        photo_pixmap_overscaled_cropped = photo_pixmap_overscaled.copy(QRect(aleft, atop, 1024, 1024));

        #Ensuite on la réduit de taille d'un facteur 4 avec un smooth, qui permet d'avoir un joli rendu
        placeholder_pixmap_scaled = photo_pixmap_overscaled_cropped.scaled(256, 256, transformMode=Qt.SmoothTransformation)

        i = 0
        for id, path in app_get_photos().items():
            photo_pixmap: QPixmap = QPixmap(app_get_current_serie_path() + path)

            if photo_pixmap.isNull():
                photo_pixmap_scaled = placeholder_pixmap_scaled
            else:
                #On rend d'abord la photo en temps que carré 1024x1024px (ici, on ne fait que la réduire en taille pour que son plus petit coté fasse 1024px)
                photo_pixmap_overscaled = photo_pixmap.scaled(1024, 1024, aspectRatioMode=Qt.KeepAspectRatioByExpanding)

                #On centre le carré sur l'image, car c'est souvent au centre de la photo ce qui est intéressant
                aleft = (photo_pixmap_overscaled.width() - 1024) // 2
                atop = (photo_pixmap_overscaled.height() - 1024) // 2
                photo_pixmap_overscaled_cropped = photo_pixmap_overscaled.copy(QRect(aleft, atop, 1024, 1024));

                #Ensuite on la réduit de taille d'un facteur 4 avec un smooth, qui permet d'avoir un joli rendu
                photo_pixmap_scaled = photo_pixmap_overscaled_cropped.scaled(256, 256, transformMode=Qt.SmoothTransformation)
            button = CentralButton(id, path, photo_pixmap_scaled)
            #self.thumbnails_to_load.append((app_get_current_serie_path() + path, button))

            self.central_grid.addWidget(button, i//5,i%5)
            i += 1
        
        # worker = Worker(self.load_thumbnails)
        # self.threadpool.start(worker)
    
    # def load_thumbnails(self):
    #     if len(self.thumbnails_to_load) > 0:
    #         path, button = self.thumbnails_to_load.pop()

    #         photo_pixmap = QPixmap(path)

    #         #On rend d'abord la photo en temps que carré 1024x1024px (ici, on ne fait que la réduire en taille pour que son plus petit coté fasse 1024px)
    #         photo_pixmap_overscaled = photo_pixmap.scaled(1024, 1024, aspectRatioMode=Qt.KeepAspectRatioByExpanding)

    #         #On centre le carré sur l'image, car c'est souvent au centre de la photo ce qui est intéressant
    #         aleft = (photo_pixmap_overscaled.width() - 1024) // 2
    #         atop = (photo_pixmap_overscaled.height() - 1024) // 2
    #         photo_pixmap_overscaled_cropped = photo_pixmap_overscaled.copy(QRect(aleft, atop, 1024, 1024));

    #         #Ensuite on la réduit de taille d'un facteur 4 avec un smooth, qui permet d'avoir un joli rendu
    #         photo_pixmap_scaled = photo_pixmap_overscaled_cropped.scaled(256, 256, transformMode=Qt.SmoothTransformation)
            
    #         icon = QIcon(photo_pixmap_scaled)
    #         button.setIcon(icon)

    #         return self.load_thumbnails()

