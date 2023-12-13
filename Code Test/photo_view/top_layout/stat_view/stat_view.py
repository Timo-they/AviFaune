

from functools import partial
import os

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QPushButton, QHBoxLayout, QSpinBox, QLayoutItem, QSizePolicy
from PyQt5.QtCore import Qt

import datas

from top_layout.stat_view.scroll_area_stat import ScrollAreaStat

class StatView(QWidget):

    box: QVBoxLayout
    stat_boxes: list

    def __init__(self, parent = None):
        super().__init__(parent)
        datas.set_widget("stat_view", self)

        self.stat_boxes = []

        self.setMinimumWidth(120)
        self.setMaximumWidth(300)

        self.build_stat_view()

    def build_stat_view(self):
        # La vue entière
        view_box = QVBoxLayout(self)
        view_box.setContentsMargins(0, 0, 0, 0)
        
        # Le titre de la vue
        label = QLabel("Stats")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        view_box.addWidget(label)

        # La barre séparatrice
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        view_box.addWidget(separator)

        # La liste scrollable de séries
        scroll = ScrollAreaStat()
        scroll_widget = scroll.widget
        view_box.addWidget(scroll)

        self.stats_list_box = QVBoxLayout(scroll_widget)
        self.stats_list_box.setContentsMargins(4, 4, 4, 4)
        self.stats_list_box.setSpacing(0)

    # Quand la série change ou que la liste des séries change
    def update(self):
        # On supprime tous les boutons de série
        # children = []
        # for i in range(self.stats_list_box.count()):
        #     child = self.stats_list_box.itemAt(i).layout()
        #     if child:
        #         children.append(child)
        #     else:
        #         child = self.stats_list_box.itemAt(i).widget()
        #         if child:
        #             children.append(child)
        
        # for child in children:
        #     child.deleteLater()
        
        # if datas.get_current_serie() == "":
        #     return

        # for layout in self.stat_boxes:
        #     while layout.count():
        #         item = layout.takeAt(0)
        #         widget = item.widget()

        #         if widget is not None:
        #             widget.setParent(None)
            
        #     while layout.count():
        #         item = layout.takeAt(0)
        #         if item is not None:
        #             while item.count():
        #                 subitem = item.takeAt(0)
        #                 widget = subitem.widget()
        #                 if widget is not None:
        #                     widget.setParent(None)
        #             layout.removeItem(item)
                
            # while 1:
            #     child = layout.takeAt(0)
            #     if not child:
            #         break
            #     child.widget().deleteLater()
            
            # delete layout
            
        # for child in self.stat_boxes:
        #     child.widget().deleteLater()
        
        self.stat_boxes = []
        
        #Show serie stats
        if datas.get_current_photo() == "":
            # On réajoute tous les boutons de série
            for id, name in datas.get_species().items():
                box = QHBoxLayout()

                label = QLabel(name + " : ")
                label.setToolTip(name)
                box.addWidget(label)

                spin = QSpinBox()

                if datas.get_current_photo() == "":
                    spin.setDisabled(True)

                specie_stats = datas.get_stats_serie().get("global")
                if specie_stats:
                    specie_stat = specie_stats.get(id)

                    if specie_stat:
                        spin.setValue(int(specie_stat))

                box.addWidget(spin)

                self.stats_list_box.addLayout(box)
                self.stat_boxes.append(box)

            # Euh, ça c'est juste pour éviter certains trucs bizarre
            fill_widget = QWidget()
            self.stats_list_box.addWidget(fill_widget)
