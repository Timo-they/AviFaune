

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

        self.setMinimumWidth(120)
        self.setMaximumWidth(250)

        self.build_serie_view()

    def build_serie_view(self):
        # La vue entière
        view_box = QVBoxLayout(self)
        view_box.setContentsMargins(0, 0, 0, 0)
        
        # Le titre de la vue
        label = QLabel("Séries")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        view_box.addWidget(label)

        # La barre séparatrice
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        view_box.addWidget(separator)

        # La liste scrollable de séries
        scroll = ScrollAreaSerie()
        scroll_widget = scroll.widget
        view_box.addWidget(scroll)

        self.series_list_box = QVBoxLayout(scroll_widget)
        self.series_list_box.setContentsMargins(0, 2, 0, 2)
        self.series_list_box.setSpacing(0)

    # Quand la série change ou que la liste des séries change
    def update(self):
        # On supprime tous les boutons de série
        children = []
        for i in range(self.series_list_box.count()):
            child = self.series_list_box.itemAt(i).widget()
            if child:
                children.append(child)
        for child in children:
            child.deleteLater()
        
        # On réajoute tous les boutons de série
        for id, path in datas.get_series().items():
            button = QPushButton(os.path.basename(os.path.dirname(path)))
            button.setToolTip(path)
            button.setObjectName("serie-button")
            button.clicked.connect(partial(self.open_serie, id))

            if id == datas.get_current_serie():
                button.setDisabled(True)

            self.series_list_box.addWidget(button)

        # Euh, ça c'est juste pour éviter certains trucs bizarre
        fill_widget = QWidget()
        self.series_list_box.addWidget(fill_widget)
    
    # On ouvre une série
    def open_serie(self, id: str):
        print("Opening serie ", id)
        datas.set_current_serie(id)
