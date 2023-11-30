


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from datas import *

from bottom_layout.bottom_layout import *
from top_layout.top_layout import *
from menu_bar import *


class OizoWindow(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        app_set_widget("oizo_window", self)

        self.build_window()
    
    def build_window(self):
        print("Building App window")
        self.setWindowTitle("Oizoos")
        self.resize(1024, 720)

        MenuBarHandler()

        window_widget = QWidget()
        window_layout = QVBoxLayout(window_widget)

        top_layout = TopLayout()
        bottom_layout = BottomLayout()

        window_layout.addLayout(top_layout, 6)
        window_layout.addLayout(bottom_layout, 1)

        self.setCentralWidget(window_widget)