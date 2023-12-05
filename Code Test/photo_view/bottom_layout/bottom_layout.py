
from functools import partial
import typing

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QToolButton, QSizePolicy, QWidget
from PyQt5.QtCore import QEvent, QObject, QRect, Qt

import datas

from bottom_layout.scroll_area_bottom import ScrollAreaBottom
from bottom_layout.thumbnail_button import ThumbnailButton


class BottomLayout(QHBoxLayout):

    previous_photo_button: QPushButton
    thumbnail_button_list: QHBoxLayout
    next_photo_button: QPushButton

    thumbnail_buttons: dict

    last_serie: int

    def __init__(self, parent = None):
        super().__init__(parent)
        datas.set_widget("bottom_layout", self)

        self.thumbnail_buttons = {}
        self.last_serie = ""

        self.build_bottom_layout()

    def build_bottom_layout(self):
        self.previous_button = QToolButton()
        self.previous_button.setObjectName("navigation_button")
        self.previous_button.setArrowType(Qt.LeftArrow)
        self.previous_button.setAutoRaise(True)
        self.previous_button.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.previous_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.previous_button.setMinimumHeight(80)
        self.previous_button.clicked.connect(self.go_to_previous_photo)
        self.addWidget(self.previous_button)

        scroll = ScrollAreaBottom()
        scroll_widget = scroll.widget
        self.addWidget(scroll)

        intermediate_hbox = QHBoxLayout(scroll_widget)

        self.thumbnails_box = QHBoxLayout(scroll_widget)
        self.thumbnails_box.setContentsMargins(0, 0, 0, 0)
        intermediate_hbox.addLayout(self.thumbnails_box)

        intermediate_hbox.addWidget(QWidget())
        
        self.next_button = QToolButton()
        self.next_button.setObjectName("navigation_button")
        self.next_button.setArrowType(Qt.RightArrow)
        self.next_button.setAutoRaise(True)
        self.next_button.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.next_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.next_button.clicked.connect(self.go_to_next_photo)
        self.addWidget(self.next_button)
    
    def update_selected_serie(self):
        # Clear buttons
        children = []
        for i in range(self.thumbnails_box.count()):
            child = self.thumbnails_box.itemAt(i).widget()
            if child:
                children.append(child)
        for child in children:
            child.deleteLater()
        
        # Reset link to buttons
        self.thumbnail_buttons = {}

        # No serie, diable
        if datas.get_current_serie() == "":
            self.previous_button.setDisabled(True)
            self.next_button.setDisabled(True)
            return

        # Bottom buttons
        photo = datas.get_current_photo()
        photos_ids = list(datas.get_photos().keys())

        if photo == "" or len(datas.get_photos()) == 0:
            self.previous_button.setDisabled(False)
            self.next_button.setDisabled(False)
        else:
            self.previous_button.setDisabled(photos_ids.index(photo) == 0)
            self.next_button.setDisabled(photos_ids.index(photo) == len(photos_ids)-1)

        # The buttons
        placeholder_pixmap = self.load_placeholder()

        for id, path in datas.get_photos().items():
            button = ThumbnailButton(id, path, placeholder_pixmap)
            button.clicked.connect(partial(self.open_photo, id))

            self.thumbnails_box.addWidget(button)
            self.thumbnail_buttons[id] = button

    def update_selected_photo(self, last_selected: str, new_selected: str):
        # Bottom buttons
        if datas.get_current_serie() == "":
            self.previous_button.setDisabled(True)
            self.next_button.setDisabled(True)
            return

        photo = datas.get_current_photo()
        photos_ids = list(datas.get_photos().keys())

        if photo == "" or len(datas.get_photos()) == 0:
            self.previous_button.setDisabled(False)
            self.next_button.setDisabled(False)
        else:
            self.previous_button.setDisabled(photos_ids.index(photo) == 0)
            self.next_button.setDisabled(photos_ids.index(photo) == len(photos_ids)-1)

        # Selected button
        if last_selected != "":
            self.thumbnail_buttons[last_selected].setDisabled(False)
        if new_selected != "":  
            self.thumbnail_buttons[new_selected].setDisabled(True)
    
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

        # TODO : Scroll so that the thumbnail is in the center of the scrollbar

    def go_to_next_photo(self):
        if datas.get_current_serie() == "":
            return

        photo = datas.get_current_photo()
        photos_ids: list = list(datas.get_photos().keys())

        if photo == "" and len(photos_ids) > 0:
            print(datas.get_photos(), photos_ids[0])
            datas.set_current_photo(photos_ids[0])
            return

        new_photo = photos_ids[photos_ids.index(photo) + 1]
        datas.set_current_photo(new_photo)

    def go_to_previous_photo(self):
        if datas.get_current_serie() == "":
            return
        
        photo = datas.get_current_photo()
        photos_ids: list = list(datas.get_photos().keys())

        if photo == "" and len(photos_ids) > 0:
            print(datas.get_photos(), photos_ids[0])
            datas.set_current_photo(photos_ids[0])
            return

        new_photo = photos_ids[photos_ids.index(photo) - 1]
        datas.set_current_photo(new_photo)

    def set_thumbnail_photo(self, pixmap: QPixmap, id: str, id_serie: str):
        button = self.thumbnail_buttons.get(id)

        if button and datas.get_current_serie() == id_serie:
            button.set_thumbnail(pixmap)



