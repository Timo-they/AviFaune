

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from datas import *


class ScrollAreaBottom(QScrollArea):

    widget: QWidget

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.verticalScrollBar().setEnabled(False)
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
            if self.horizontalScrollBar().isVisible():
                self.widget.setFixedHeight(self.height() - 8)
            else:
                self.widget.setFixedHeight(self.height())

        return False
        