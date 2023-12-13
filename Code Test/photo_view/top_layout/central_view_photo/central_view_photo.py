



from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QLabel, QFrame, QHBoxLayout, QToolButton
from PyQt5.QtCore import Qt

import datas

from top_layout.central_view_photo.central_photo import CentralPhoto


class CentralViewPhoto(QWidget):

    view_box: QVBoxLayout
    title_label: QLabel

    def __init__(self, parent = None):
        super().__init__(parent)

        # Ca c'est pour la couleur de fond
        palette = QPalette()

        palette.setColor(QPalette.Window, QColor("#303446"))

        self.setAutoFillBackground(True); 
        self.setPalette(palette)

        datas.set_widget("central_view_photo", self)

        self.build_central_view()

    def build_central_view(self):
        self.view_box = QVBoxLayout(self)

        self.hbox = QHBoxLayout()
        self.view_box.addLayout(self.hbox)

        # Le bouton pour revenir à la vue de série
        self.return_button = QToolButton()
        self.return_button.setArrowType(Qt.UpArrow)
        self.return_button.setAutoRaise(True)
        self.return_button.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.return_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.return_button.clicked.connect(self.go_back_to_series)
        self.hbox.addWidget(self.return_button)

        # Titre de la photo
        self.title_label = QLabel("Aucune série sélectionnée")
        self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hbox.addWidget(self.title_label)

        # Séparateur
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        self.view_box.addWidget(separator)

        # Affichage central de la photo
        self.center_image = CentralPhoto()
        self.view_box.addWidget(self.center_image)

    
    # Quand la photo change
    def update(self):
        if datas.get_current_photo() == "":
            print("Removing photo from middle")
            self.title_label.setText("Aucune photo")
            return

        print("Opening photo for middle ", datas.get_current_photo_full_path()) 
        self.title_label.setText(datas.get_current_photo_name())

        photo_pixmap: QPixmap = QPixmap(datas.get_current_photo_full_path())
        self.center_image.set_pixmap(photo_pixmap)
    
    # Retourne à la vue de série
    def go_back_to_series(self):
        datas.set_current_photo("")