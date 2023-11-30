


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from datas import *


class StatView(QWidget):

    box: QVBoxLayout

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName("panel-color")

        self.build_stat_view()

    def build_stat_view(self):
        # title_label = QLabel("Séries")
        # title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.addWidget(title_label)

        self.box = QVBoxLayout(self)

        # id = QFontDatabase.addApplicationFont("roboto/Roboto-BoldItalic.ttf")
        # if id < 0: print(" /!\ Error, cannot read : roboto/Roboto-BoldItalic.ttf /!\ ")

        # families = QFontDatabase.applicationFontFamilies(id)
        # print(families[0])

        label = QLabel("Pas de statistiques pour l'instant...")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setWordWrap(True)
        self.box.addWidget(label)

        # label.setFont(QFont(families[0], 80))
