


from PyQt5.QtWidgets import QHBoxLayout

import datas

from top_layout.central_view.central_view import CentralView
from top_layout.central_view_photo.central_view_photo import CentralViewPhoto
from top_layout.serie_view.serie_view import SerieView
from top_layout.stat_view.stat_view import StatView


class TopLayout(QHBoxLayout):

    mode: str

    def __init__(self, parent = None):
        super().__init__(parent)
        datas.set_widget("top_layout", self)

        # Mode d'affichage
        # C'est une variable très locale
        self.mode = "series"
        # "series" -> En mode affichage de série
        # "photo" -> En mode affichage de photo

        self.build_top_layout()
    
    def build_top_layout(self):
        # La vue de série (gauche)
        self.serie_view = SerieView()

        # La vue de stats (droite)
        self.stat_view = StatView()

        # La vue affichée au milieu en mode série
        self.central_view = CentralView()

        # La vue affichée au milieu en mode photo
        self.central_view_photo = CentralViewPhoto()

        self.addWidget(self.serie_view, 1)
        self.addWidget(self.central_view, 4)
        self.addWidget(self.stat_view, 1)

    # Quand la photo change ou que la série change
    def update(self):
        # Passe soit en mode series soit photo
        if datas.get_current_photo() != "" and self.mode == "series":
            self.replaceWidget(self.central_view, self.central_view_photo)
            self.central_view.setVisible(False)
            self.central_view_photo.setVisible(True)
            self.mode = "photo"
        
        elif datas.get_current_photo() == "" and self.mode == "photo":
            self.replaceWidget(self.central_view_photo, self.central_view)
            self.central_view.setVisible(True)
            self.central_view_photo.setVisible(False)
            self.mode = "series"


