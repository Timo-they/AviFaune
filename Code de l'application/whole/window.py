


import typing
from PyQt5 import QtGui
from PyQt5.QtCore import QEvent, QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import datas

from bottom_layout.bottom_layout import BottomLayout
from top_layout.top_layout import TopLayout
from whole.menu_bar import MenuBarHandler


class OizoWindow(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        datas.set_widget("oizo_window", self)

        self.build_window()
    
    def build_window(self):
        print("Start of building app window...")
        self.setWindowTitle("Avifaune Scan")
        # TODO : A la fin faudrait l'exporter pour qu'elle se mette joliment en maximised je pense
        self.resize(1024, 720)

        #Le menu du haut
        MenuBarHandler()

        window_widget = QWidget()
        window_layout = QVBoxLayout(window_widget)

        # Ce qu'il y a sur la partie supérieure de la fenêtre
        top_layout = TopLayout()
        # Ce qu'il y a sur la partie inférieure de la fenêtre
        bottom_layout = BottomLayout()

        window_layout.addLayout(top_layout, 6)
        window_layout.addLayout(bottom_layout, 1)

        self.setCentralWidget(window_widget)

        self.setFocusPolicy(Qt.ClickFocus)
        self.setFocusProxy(self)
        self.installEventFilter(self)

    ## Ca marche pas...
    
    # def eventFilter(self, a0: QObject | None, event: QEvent) -> bool:
    #     if event.type() == QEvent.KeyPress:
    #         if event.key() == Qt.Key_Right:
    #             print("RIGHT KEY !")
    #             datas.get_widget("bottom_layout").go_to_next_photo()

    #         elif event.key() == Qt.Key_Left:
    #             datas.get_widget("bottom_layout").go_to_previous_photo()

    #     return super().eventFilter(a0, event)
