


from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QToolButton, QSizePolicy, QLabel, QWidget
from PyQt5.QtCore import QSize, QObject, QEvent, Qt

import datas


class CentralButton(QToolButton):

    path: str

    def __init__(self, id, path, photo_pixmap_scaled):
        super().__init__(None)
        
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        icon = QIcon(photo_pixmap_scaled)

        self.setIcon(icon)
        self.setIconSize(QSize(512, 512))

        self.setText(path)
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
            height = self.width() + 23
            self.setFixedHeight(height)
            self.setIconSize(QSize(height-17, height-17))

            if not self.label == None:
                self.label.move(12, 14)

        return False
    
    def check_has_box(self):
        # Il n'y a pas de cadre encore pour cette photo
        if not self.path in datas.get_stats_serie().keys():
            self.label.setVisible(False)

        # Il y a des cadres dans cette photo
        else:
            # On affiche le nombre de cadres qu'il y a dessus
            stats = datas.get_stats_serie()[self.path]
            count = len(stats)
            self.label.setText(" " + str(count) + " ")
            #self.label.setText("100000")
