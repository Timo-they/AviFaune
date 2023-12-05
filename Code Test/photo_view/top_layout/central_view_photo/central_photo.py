



from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import QObject, QEvent, Qt

import datas


class CentralPhoto(QWidget):

    qlabel: QLabel

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumHeight(100)

        self.qlabel = QLabel(self)
        self.qlabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.qlabel.setScaledContents(True)
        
        self.installEventFilter(self)
    
    def eventFilter(self, object: QObject, event: QEvent) -> bool:
        if object == self and event.type() == QEvent.Resize and not self.qlabel.pixmap() == None:
            self.resize()

        return False

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
