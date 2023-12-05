

from PyQt5.QtWidgets import QScrollArea, QWidget, QFrame, QSizePolicy
from PyQt5.QtCore import QObject, Qt, QEvent

import datas


class ScrollAreaCentral(QScrollArea):

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
    
    def eventFilter(self, object: QObject, event: QEvent) -> bool:
        # if object == self.widget and event.type() == QEvent.Resize:
        #     print("Setting the size to ", self.width())
        #     if self.verticalScrollBar().isVisible():
        #         self.widget.setFixedWidth(self.width() - 8)
        #     else:
        #         self.widget.setFixedWidth(self.width())
        if object == self and event.type() == QEvent.Resize:
            #print("Setting the size to ", self.width())
            if self.verticalScrollBar().isVisible():
                self.widget.setFixedWidth(self.width() - 8)
            else:
                self.widget.setFixedWidth(self.width())

        return False
        