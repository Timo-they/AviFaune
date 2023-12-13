


import typing
from PyQt5 import QtGui
from PyQt5.QtCore import QEvent, QObject, Qt
from PyQt5.QtWidgets import QWidget, QLabel

import datas


class Cadre(QLabel):

    def __init__(self, specie, x, y, w, h, qlabel, pixmap):
        super().__init__(qlabel)

        self.specie = str(int(specie))
        self.x, self.y, self.w, self.h = x, y, w, h
        self.x, self.y, self.w, self.h = int(self.x), int(self.y), int(self.w), int(self.h)

        self.qlabel = qlabel
        self.pixmap = pixmap

        # TODO : Set cadre color depending on specie
        print("TODO : Set cadre color depending on specie")
        
        self.setObjectName("cadre")
        self.setToolTip(datas.get_specie_name(self.specie))
        self.resize()
    
    def resize(self):
        x, y, w, h = self.x, self.y, self.w, self.h
        x, y, w, h = int(x), int(y), int(w), int(h)

        print("Box : ", x, y, w, h)

        qlabel_x = self.qlabel.x()
        qlabel_y = self.qlabel.y()
        qlabel_width = self.qlabel.width()
        qlabel_height = self.qlabel.height()
        print("QLabel : ", qlabel_x, qlabel_y ,qlabel_width, qlabel_height)

        pixmap_width = self.pixmap.width()
        pixmap_height = self.pixmap.height()
        print("QPixmap : ", pixmap_width, pixmap_height)

        cadre_x = int((x - w/2) * qlabel_width / pixmap_width)
        cadre_y = int((y - h/2) * qlabel_height / pixmap_height)
        cadre_width = int(w * qlabel_width / pixmap_width)
        cadre_height = int(h * qlabel_height / pixmap_height)
        
        self.setGeometry(cadre_x, cadre_y, cadre_width, cadre_height)
        print("Added cadre at ", cadre_x, cadre_y, cadre_width, cadre_height)

    def eventFilter(self, object: QObject, event: QEvent) -> bool:
        if object == self and event.type() == QEvent.Resize:
            self.resize()

        return False
