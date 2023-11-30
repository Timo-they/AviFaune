

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from datas import *

from bottom_layout.scroll_area_bottom import *


class BottomLayout(QHBoxLayout):

    previous_photo_button: QPushButton
    thumbnail_button_list: QHBoxLayout
    next_photo_button: QPushButton

    def __init__(self, parent = None):
        super().__init__(parent)
        app_set_widget("bottom_layout", self)

        self.build_bottom_layout()

    def build_bottom_layout(self):
        self.previous_button = QToolButton()
        self.previous_button.setArrowType(Qt.LeftArrow)
        self.previous_button.setAutoRaise(True)
        self.previous_button.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.previous_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.addWidget(self.previous_button)

        scroll = ScrollAreaBottom()
        scroll_widget = scroll.widget
        self.addWidget(scroll)

        self.thumbnails_box = QHBoxLayout(scroll_widget)
        self.thumbnails_box.setContentsMargins(4, 4, 4, 4)
        #self.thumbnails_box.addWidget(QWidget())
        
        self.next_button = QToolButton()
        self.next_button.setArrowType(Qt.RightArrow)
        self.next_button.setAutoRaise(True)
        self.next_button.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.next_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.addWidget(self.next_button)
    
    # def update(self):
    #     if app_get_current_serie() == "":
    #         self.title_label.setText("Aucune série sélectionnée")
    #         return

    #     self.title_label.setText(app_get_current_serie_path())
        
    #     children = []
    #     for i in range(self.central_grid.count()):
    #         child = self.central_grid.itemAt(i).widget()
    #         if child:
    #             children.append(child)
    #     for child in children:
    #         child.deleteLater()

    #     photo_pixmap = QPixmap("placeholder-square.jpg")

    #     #On rend d'abord la photo en temps que carré 1024x1024px (ici, on ne fait que la réduire en taille pour que son plus petit coté fasse 1024px)
    #     photo_pixmap_overscaled = photo_pixmap.scaled(1024, 1024, aspectRatioMode=Qt.KeepAspectRatioByExpanding)

    #     #On centre le carré sur l'image, car c'est souvent au centre de la photo ce qui est intéressant
    #     aleft = (photo_pixmap_overscaled.width() - 1024) // 2
    #     atop = (photo_pixmap_overscaled.height() - 1024) // 2
    #     photo_pixmap_overscaled_cropped = photo_pixmap_overscaled.copy(QRect(aleft, atop, 1024, 1024));

    #     #Ensuite on la réduit de taille d'un facteur 4 avec un smooth, qui permet d'avoir un joli rendu
    #     placeholder_pixmap_scaled = photo_pixmap_overscaled_cropped.scaled(256, 256, transformMode=Qt.SmoothTransformation)

    #     i = 0
    #     for id, path in app_get_photos().items():
    #         button = CentralButton(id, path, photo_pixmap_scaled)
    #         #self.thumbnails_to_load.append((app_get_current_serie_path() + path, button))

    #         self.central_grid.addWidget(button, i//5,i%5)
    #         i += 1
        
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

