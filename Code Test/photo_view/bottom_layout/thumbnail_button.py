


from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QToolButton, QSizePolicy
from PyQt5.QtCore import Qt, QSize, QEvent, QObject

import datas


class ThumbnailButton(QToolButton):

    def __init__(self, id, path, photo_pixmap_scaled):
        super().__init__(None)
        
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        #print("Adding button with icon ", app_get_current_serie_path() + path)

        icon = QIcon(photo_pixmap_scaled)

        self.setIcon(icon)
        self.setIconSize(QSize(256, 256))

        self.setToolTip(path)

        self.installEventFilter(self)


    def eventFilter(self, object: QObject, event: QEvent) -> bool:
        if object == self and event.type() == QEvent.Resize:
            width = self.height()
            self.setFixedWidth(width)
            self.setIconSize(QSize(width, width))

        return False

    def set_thumbnail(self, pixmap: QPixmap):
         icon = QIcon(pixmap)
         self.setIcon(icon)