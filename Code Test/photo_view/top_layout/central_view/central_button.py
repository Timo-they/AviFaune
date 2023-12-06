


from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QToolButton, QSizePolicy
from PyQt5.QtCore import QSize, QObject, QEvent, Qt

import datas


class CentralButton(QToolButton):

    def __init__(self, id, path, photo_pixmap_scaled):
        super().__init__(None)
        
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        icon = QIcon(photo_pixmap_scaled)

        self.setIcon(icon)
        self.setIconSize(QSize(512, 512))

        self.setText(path)
        self.setToolTip(path)

        self.installEventFilter(self)


    def eventFilter(self, object: QObject, event: QEvent) -> bool:
        if object == self and event.type() == QEvent.Resize:
            height = self.width() + 23
            self.setFixedHeight(height)
            self.setIconSize(QSize(height-17, height-17))

        return False
