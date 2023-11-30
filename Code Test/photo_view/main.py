

import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from datas import *
from datas_loader_saver import *

from window import OizoWindow


if __name__ == "__main__":
    print(" - - - - - Start of Oizooo App - - - - - ")
    app = QApplication(sys.argv)

    print("First got widgets : ", widgets_)
    print()

    win = OizoWindow()
    win.show()

    qss_path = "style.qss"
    with open(qss_path, "r") as file:
        app.setStyleSheet(file.read())


    #app.setStyle("Fusion")

    # Custom brown palette.
    # palette = QPalette()
    # palette.setColor(QPalette.Window, QColor(188,170,164))
    # palette.setColor(QPalette.WindowText, QColor(121,85,72))
    # palette.setColor(QPalette.ButtonText, QColor(121,85,72))
    # palette.setColor(QPalette.Text, QColor(121,85,72))
    # palette.setColor(QPalette.Base, QColor(188,170,164))
    # palette.setColor(QPalette.AlternateBase, QColor(188,170,164))
    # app.setPalette(palette)
    
    app_load_datas()

    print()
    print("Finally got widgets : ", widgets_)

    error = app.exec_()
    print(" - - - - - End of Oizooo App - - - - - ")
    sys.exit(error)