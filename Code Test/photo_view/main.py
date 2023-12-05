

import sys

from PyQt5.QtWidgets import QApplication

import datas
import whole.datas_loader_saver as datas_loader_saver

from whole.window import OizoWindow


if __name__ == "__main__":
    print()
    print(datas.COLOR_GREEN, " - - - - - Start of Oizooo App - - - - - ", datas.COLOR_RESET)
    print()

    app = QApplication(sys.argv)

    print(datas.COLOR_BRIGHT_BLUE, "First got widgets : ", datas.widgets_, datas.COLOR_RESET)
    print()

    win = OizoWindow()
    win.show()

    qss_path = "style.qss"
    with open(qss_path, "r") as file:
        app.setStyleSheet(file.read())
    
    datas_loader_saver.load_datas()

    print()
    print(datas.COLOR_BRIGHT_BLUE, "Finally got widgets : ", datas.widgets_, datas.COLOR_RESET)

    error = app.exec_()
    print()
    print(datas.COLOR_GREEN, " - - - - - End of Oizooo App - - - - - ", datas.COLOR_RESET)
    print()
    sys.exit(error)