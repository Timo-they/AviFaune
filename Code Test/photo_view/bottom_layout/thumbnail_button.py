


from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QToolButton, QSizePolicy, QLabel
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
        self.path = path
        
        self.label = QLabel(self)
        self.label.setObjectName("little_cadre")
        self.label.move(12, 14)
        #self.label.setGeometry(12, 14, 15, 15)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Il n'y a pas de cadre encore pour cette photo
        if not path in datas.get_stats_serie().keys():
            self.label.setVisible(False)

        # Il y a des cadres dans cette photo
        else:
            # On affiche le nombre de cadres qu'il y a dessus
            stats = datas.get_stats_serie()[path]
            count = len(stats)
            self.label.setText(" " + str(count) + " ")
            #self.label.setText("100000")

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
    
    def check_has_box(self):
        # Il n'y a pas de cadre encore pour cette photo
        if not self.path in datas.get_stats_serie().keys():
            self.label.setVisible(False)

        # Il y a des cadres dans cette photo
        else:
            # On affiche le nombre de cadres qu'il y a dessus
            self.label.setVisible(True)
            stats = datas.get_stats_serie()[self.path]
            count = len(stats)
            self.label.setText(" " + str(count) + " ")
            #self.label.setText("100000")