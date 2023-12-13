

from functools import partial

from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QFrame, QGridLayout
from PyQt5.QtCore import QThread, QRect, Qt, QThreadPool

import datas

from top_layout.central_view.scroll_area_central import ScrollAreaCentral
from top_layout.central_view.central_button import CentralButton
from top_layout.central_view.thumbnail_loader import ThumbnailLoader, Worker

class CentralView(QWidget):

    view_box: QVBoxLayout
    title_label: QLabel

    # C'est la liste de tous les boutons associés à chaque photo de la série
    thumbnail_buttons: dict
    # {
    #   "0": Button,
    #   "1": Button
    # }

    thumnbnail_loader: ThumbnailLoader

    def __init__(self, parent = None):
        super().__init__(parent)

        self.thumbnail_buttons = {}
        self.threadpool = QThreadPool()

        # Ca c'est pour la couleur de fond
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#303446"))

        self.setAutoFillBackground(True); 
        self.setPalette(palette)

        datas.set_widget("central_view", self)

        self.build_central_view()

    def build_central_view(self):
        self.view_box = QVBoxLayout(self)

        # Le titre de la vue
        self.title_label = QLabel("Aucune série sélectionnée")
        self.view_box.addWidget(self.title_label)

        # La barre séparatrice
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        self.view_box.addWidget(separator)

        # La liste scrollable des photos
        scroll = ScrollAreaCentral()
        scroll_widget = scroll.widget
        self.view_box.addWidget(scroll)

        intermediate_vbox = QVBoxLayout(scroll_widget)
        self.central_grid = QGridLayout()
        self.central_grid.columnCount
        self.central_grid.setContentsMargins(4, 4, 4, 4)
        intermediate_vbox.addLayout(self.central_grid)

        intermediate_vbox.addWidget(QWidget())
    
    # Quand la série courante et changée
    def update(self):
        # On enlève tous les boutons des photos
        children = []
        for i in range(self.central_grid.count()):
            child = self.central_grid.itemAt(i).widget()
            if child:
                children.append(child)
        for child in children:
            child.deleteLater()
        
        self.thumbnail_buttons = {}

        # S'il y a pas de photos affichée, on change que le titre
        if datas.get_current_serie() == "":
            self.title_label.setText("Aucune série sélectionnée")
            return

        self.title_label.setText(datas.get_current_serie_path() + " (" + str(len(datas.get_photos())) + " photos)")

        # On charge l'image par défaut
        placeholder_pixmap = self.load_placeholder()
        
        # On ajoute tous les boutons un à un avec la miniature par défaut
        i = 0
        for id, path in datas.get_photos().items():
            button = CentralButton(id, path, placeholder_pixmap)
            button.clicked.connect(partial(self.open_photo, id))

            self.central_grid.addWidget(button, i//5,i%5)
            self.thumbnail_buttons[id] = button
            i += 1
        
        # On charge les miniatures
        # TODO : le faire dans un autre thread
        print("Multithreading with maximum %d threads" %  QThreadPool.globalInstance().maxThreadCount())
        if QThreadPool.globalInstance().activeThreadCount() > 0:
            print(datas.COLOR_BRIGHT_RED, "Le thread de miniatures est encore en cours... On attend qu'ca finisse")
            QThreadPool.globalInstance().waitForDone()


        self.thumbnail_loader = ThumbnailLoader(placeholder_pixmap)
        QThreadPool.globalInstance().start(self.thumbnail_loader)
        
        # print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        # # Pass the function to execute
        # worker = Worker(self.a) # Any other args, kwargs are passed to the run function

        # # Execute
        # self.threadpool.start(worker)

        # if self.thumnbnail_loader_thread.isRunning():
        #     print(datas.COLOR_BRIGHT_RED, "The thred has not finished yet, waiting for it", datas.COLOR_RESET)
        #     self.thumnbnail_loader_thread.wait()
        
        # self.thumnbnail_loader = ThumbnailLoader(placeholder_pixmap)

        # self.thumnbnail_loader_thread = QThread()
        # self.thumnbnail_loader.moveToThread(self.thumnbnail_loader_thread)
        # self.thumnbnail_loader_thread.started.connect(self.thumnbnail_loader.load_thumbnails)
        # self.thumnbnail_loader.finished.connect(self.thumnbnail_loader_thread.quit)
        # self.thumnbnail_loader.finished.connect(self.thumnbnail_loader.deleteLater)
        # self.thumnbnail_loader_thread.finished.connect(self.thumnbnail_loader_thread.deleteLater)

        # self.thumnbnail_loader_thread.start()
        # print(datas.COLOR_BRIGHT_YELLOW, "end", datas.COLOR_RESET)

    def a(self):
        for x in range(50):
            self.load_placeholder()
            print(x, ". Done", sep="")
    
    # Charge la miniature par défaut
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

    # Ouvre une photo cliquée
    def open_photo(self, id: str):
        datas.set_current_photo(id)
    
    # Fonction pour changer la miniature d'une photo
    def set_thumbnail_photo(self, icon: QIcon, id: str, id_serie: str):
        button = self.thumbnail_buttons.get(id)

        if button and datas.get_current_serie() == id_serie:
            button.setIcon(icon)#_thumbnail(pixmap)