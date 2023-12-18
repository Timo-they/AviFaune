

from PyQt5.QtGui import QShowEvent, QHideEvent
from PyQt5.QtWidgets import QScrollArea, QWidget, QFrame, QSizePolicy
from PyQt5.QtCore import Qt, QObject, QEvent

import datas


class ScrollAreaBottom(QScrollArea):

    widget: QWidget

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.verticalScrollBar().setEnabled(False)
        self.setFrameStyle(QFrame.NoFrame)

        self.horizontalScrollBar().installEventFilter(self)
        
        self.widget = QWidget()
        self.widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setWidget(self.widget)
        self.widget.installEventFilter(self)
        self.installEventFilter(self)
        self.widget.setObjectName("panel-color")
    
    def eventFilter(self, object: QObject, event: QEvent) -> bool:
        # if object == self.horizontalScrollBar() and (event.type() == QEvent.Show or event.type() == QEvent.Hide):
        #     print("YOOOOOOOOOO", event)
        #     self.resize()

        if object == self and event.type() == QEvent.Resize:
            self.resize()
        
        return False

    def resize(self):
        if self.horizontalScrollBar().isVisible():
            self.widget.setMaximumHeight(self.height() - 8)
        else:
            self.widget.setMaximumHeight(self.height())
        