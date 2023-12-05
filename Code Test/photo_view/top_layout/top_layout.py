


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

        self.mode = "series"

        self.build_top_layout()
    
    def build_top_layout(self):
        self.serie_view = SerieView()
        self.stat_view = StatView()
        self.central_view = CentralView()
        self.central_view_photo = CentralViewPhoto()

        self.addWidget(self.serie_view, 1)
        self.addWidget(self.central_view, 4)
        self.addWidget(self.stat_view, 1)

    def update(self):
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


