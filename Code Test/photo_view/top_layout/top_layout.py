


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from datas import *

from top_layout.central_view.central_view import *
from top_layout.serie_view.serie_view import *
from top_layout.stat_list.stat_list import *


class TopLayout(QHBoxLayout):

    def __init__(self, parent = None):
        super().__init__(parent)
        app_set_widget("top_layout", self)

        self.build_top_layout()
    
    def build_top_layout(self):
        serie_view = SerieView()
        stat_view = StatView()
        central_view = CentralView()

        self.addWidget(serie_view, 1)
        self.addWidget(central_view, 5)
        self.addWidget(stat_view, 1)

