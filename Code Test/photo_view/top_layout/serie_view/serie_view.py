

import os
from functools import partial

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from datas import *
from serie_scanner import *

from top_layout.serie_view.scroll_area_serie import *


class SerieView(QWidget):

    series_list_box: QVBoxLayout

    def __init__(self, parent = None):
        super().__init__(parent)
        app_set_widget("serie_view", self)

        self.build_serie_view()

    def build_serie_view(self):
        view_box = QVBoxLayout(self)
        view_box.setContentsMargins(0, 0, 0, 0)

        # id = QFontDatabase.addApplicationFont("roboto/Roboto-BoldItalic.ttf")
        # if id < 0: print(" /!\ Error, cannot read : roboto/Roboto-BoldItalic.ttf /!\ ")

        # families = QFontDatabase.applicationFontFamilies(id)
        # print(families[0])
        
        label = QLabel("Séries")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        view_box.addWidget(label)

        # label.setFont(QFont(families[0], 80))

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        view_box.addWidget(separator)

        scroll = ScrollAreaSerie()
        scroll_widget = scroll.widget
        view_box.addWidget(scroll)

        self.series_list_box = QVBoxLayout(scroll_widget)
        self.series_list_box.setContentsMargins(0, 2, 0, 2)
        self.series_list_box.setSpacing(0)

    def update(self):
        children = []
        for i in range(self.series_list_box.count()):
            child = self.series_list_box.itemAt(i).widget()
            if child:
                children.append(child)
        for child in children:
            child.deleteLater()
        
        for id, path in app_get_series().items():
            button = QPushButton(os.path.basename(os.path.dirname(path)))
            button.setToolTip(path)
            button.setObjectName("serie-button")
            button.clicked.connect(partial(self.open_serie, id))

            if id == app_get_current_serie():
                button.setDisabled(True)

            self.series_list_box.addWidget(button)

        fill_widget = QWidget()
        self.series_list_box.addWidget(fill_widget)
    
    def open_serie(self, id: str):
        print("Opening serie ", id)
        app_set_current_serie(id)
        app_scan_serie()
        print("Opened serie ", app_get_current_serie_name())
