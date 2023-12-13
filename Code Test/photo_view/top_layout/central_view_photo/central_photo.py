



from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import QObject, QEvent, Qt

import datas

from top_layout.central_view_photo.cadre import Cadre


class CentralPhoto(QWidget):

    qlabel: QLabel

    cadres: list

    def __init__(self, parent = None):
        super().__init__(parent)
        datas.set_widget("central_photo", self)

        self.cadres = []

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumHeight(100)

        self.qlabel = QLabel(self)
        self.qlabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.qlabel.setScaledContents(True)
        
        self.installEventFilter(self)
    
    # Quand la fenêtre est resize
    def eventFilter(self, object: QObject, event: QEvent) -> bool:
        if object == self and event.type() == QEvent.Resize and not self.qlabel.pixmap() == None:
            self.resize()

        return False

    # On centre l'image sur le QWidget
    def resize(self):
        widget_ratio = self.width() / self.height()
        qlabel_ratio = self.qlabel.pixmap().width() / self.qlabel.pixmap().height()

        if widget_ratio >= qlabel_ratio:
            # Widget trop large
            qlabel_x = int(self.width() / 2 - self.height() * qlabel_ratio / 2)
            qlabel_y = 0
            qlabel_width = int(self.height() * qlabel_ratio)
            qlabel_height = int(self.height())

            self.qlabel.setGeometry(qlabel_x, qlabel_y, qlabel_width, qlabel_height)
        
        else:
            # Widget trop haut
            qlabel_x = 0
            qlabel_y = int(self.height() / 2 - self.width() / qlabel_ratio / 2)
            qlabel_width = int(self.width())
            qlabel_height = int(self.width() / qlabel_ratio)

            self.qlabel.setGeometry(qlabel_x, qlabel_y, qlabel_width, qlabel_height)

    
    def set_pixmap(self, photo_pixmap):
        #self.initial_pixmap = photo_pixmap
        self.qlabel.setPixmap(photo_pixmap)
        self.resize()
        self.remove_cadres()
    
    def remove_cadres(self):
        for cadre in self.cadres:
            cadre.deleteLater()
        
        self.cadres = []
    
    def update_boxes(self):
        print("Updating central photo boxes, to ", datas.get_boxes_current_photo())
        self.remove_cadres()

        for id, data in datas.get_boxes_current_photo().items():
            specie, x, y, w, h = data["specie"], data["x"], data["y"], data["w"], data["h"]

            print("Showing box ", specie, x, y, w, h)

            cadre = Cadre(specie, x, y, w, h, self.qlabel, self.qlabel.pixmap())
            cadre.show()
            self.cadres.append(cadre)


    # def set_boxes(self, boxes_classes, boxes_shapes):
    #     # On enlève tous les cadres de la photo
    #     self.remove_cadres()
        
    #     for i in range(len(boxes_shapes)):
    #         cadre = Cadre(boxes_classes[i], boxes_shapes[i], self.qlabel, self.qlabel.pixmap())
    #         cadre.show()
    #         self.cadres.append(cadre)

