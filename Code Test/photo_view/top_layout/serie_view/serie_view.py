

import os
from functools import partial

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame, QPushButton
from PyQt5.QtCore import Qt

import datas

from top_layout.serie_view.scroll_area_serie import ScrollAreaSerie


class SerieView(QWidget):

    series_list_box: QVBoxLayout

    def __init__(self, parent = None):
        super().__init__(parent)
        datas.set_widget("serie_view", self)

        self.setMinimumWidth(100)

        self.build_serie_view()

    def build_serie_view(self):
        view_box = QVBoxLayout(self)
        view_box.setContentsMargins(0, 0, 0, 0)
        
        label = QLabel("Séries")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        view_box.addWidget(label)

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
        
        for id, path in datas.get_series().items():
            button = QPushButton(os.path.basename(os.path.dirname(path)))
            button.setToolTip(path)
            button.setObjectName("serie-button")
            button.clicked.connect(partial(self.open_serie, id))

            if id == datas.get_current_serie():
                button.setDisabled(True)

            self.series_list_box.addWidget(button)

        fill_widget = QWidget()
        self.series_list_box.addWidget(fill_widget)
    
    def open_serie(self, id: str):
        print("Opening serie ", id)
        datas.set_current_serie(id)
