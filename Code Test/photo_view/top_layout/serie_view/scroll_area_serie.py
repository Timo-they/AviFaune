

from PyQt5.QtWidgets import QScrollArea, QWidget, QFrame, QSizePolicy
from PyQt5.QtCore import QEvent, QObject, Qt

import datas


class ScrollAreaSerie(QScrollArea):

    widget: QWidget

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.horizontalScrollBar().setEnabled(False)
        self.setFrameStyle(QFrame.NoFrame)
        
        self.widget = QWidget()
        self.widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setWidget(self.widget)
        self.widget.installEventFilter(self)
        self.installEventFilter(self)
        
        self.widget.setObjectName("panel-color")
    
    # C'est pour que ce qu'il y a dans la scrollarea soit bien resized
    def eventFilter(self, object: QObject, event: QEvent) -> bool:
        if object == self and event.type() == QEvent.Resize:
            if self.verticalScrollBar().isVisible():
                self.widget.setFixedWidth(self.width() - 8)
            else:
                self.widget.setFixedWidth(self.width())

        return False
        