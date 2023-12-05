

from functools import partial

from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QFrame, QGridLayout
from PyQt5.QtCore import pyqtSlot, QRunnable, QRect, Qt

import datas

from top_layout.central_view.scroll_area_central import ScrollAreaCentral
from top_layout.central_view.central_button import CentralButton
from top_layout.central_view.thumbnail_loader import ThumbnailLoader

class CentralView(QWidget):

    view_box: QVBoxLayout
    title_label: QLabel

    thumbnail_buttons: dict

    def __init__(self, parent = None):
        super().__init__(parent)

        self.thumbnail_buttons = {}

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#303446"))

        self.setAutoFillBackground(True); 
        self.setPalette(palette)

        datas.set_widget("central_view", self)

        self.build_central_view()

    def build_central_view(self):
        self.view_box = QVBoxLayout(self)

        self.title_label = QLabel("Aucune série sélectionnée")
        self.view_box.addWidget(self.title_label)

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
        children = []
        for i in range(self.central_grid.count()):
            child = self.central_grid.itemAt(i).widget()
            if child:
                children.append(child)
        for child in children:
            child.deleteLater()
        
        self.thumbnail_buttons = {}

        if datas.get_current_serie() == "":
            self.title_label.setText("Aucune série sélectionnée")
            return

        self.title_label.setText(datas.get_current_serie_path() + " (" + str(len(datas.get_photos())) + " photos)")

        placeholder_pixmap = self.load_placeholder()
        
        i = 0
        for id, path in datas.get_photos().items():
            button = CentralButton(id, path, placeholder_pixmap)
            button.clicked.connect(partial(self.open_photo, id))

            self.central_grid.addWidget(button, i//5,i%5)
            self.thumbnail_buttons[id] = button
            i += 1
        
        # TODO : load thumbnails in a different thread
    
    def load_placeholder(self) -> QPixmap:
        photo_pixmap = QPixmap("icons/placeholder-square.jpg")

        #On rend d'abord la photo en temps que carré 1024x1024px (ici, on ne fait que la réduire en taille pour que son plus petit coté fasse 1024px)
        photo_pixmap_overscaled = photo_pixmap.scaled(1024, 1024, aspectRatioMode=Qt.KeepAspectRatioByExpanding)

        #On centre le carré sur l'image, car c'est souvent au centre de la photo ce qui est intéressant
        aleft = (photo_pixmap_overscaled.width() - 1024) // 2
        atop = (photo_pixmap_overscaled.height() - 1024) // 2
        photo_pixmap_overscaled_cropped = photo_pixmap_overscaled.copy(QRect(aleft, atop, 1024, 1024))

        #Ensuite on la réduit de taille d'un facteur 4 avec un smooth, qui permet d'avoir un joli rendu
        return photo_pixmap_overscaled_cropped.scaled(256, 256, transformMode=Qt.SmoothTransformation)

    def open_photo(self, id: str):
        print("Opening photo ", id)
        datas.set_current_photo(id)
    
    def set_thumbnail_photo(self, pixmap: QPixmap, id: str, id_serie: str):
        button = self.thumbnail_buttons.get(id)

        if button and datas.get_current_serie() == id_serie:
            button.set_thumbnail(pixmap)
    
