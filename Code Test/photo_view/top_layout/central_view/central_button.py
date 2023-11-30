


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from datas import *


class CentralButton(QToolButton):

    def __init__(self, id, path, photo_pixmap_scaled):
        super().__init__(None)
        
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        #print("Adding button with icon ", app_get_current_serie_path() + path)

        icon = QIcon(photo_pixmap_scaled)

        self.setIcon(icon)
        self.setIconSize(QSize(256, 256))

        self.setText(path)
        self.setToolTip(path)

        self.installEventFilter(self)


    def eventFilter(self, object: QObject, event: QEvent) -> bool:
            # if object == self.widget and event.type() == QEvent.Resize:
            #     print("Setting the size to ", self.width())
            #     if self.verticalScrollBar().isVisible():
            #         self.widget.setFixedWidth(self.width() - 8)
            #     else:
            #         self.widget.setFixedWidth(self.width())
            if object == self and event.type() == QEvent.Resize:
                #print("Setting the size to ", self.width())
                height = self.width() + 23
                self.setFixedHeight(height)
                self.setIconSize(QSize(height-17, height-17))

            return False