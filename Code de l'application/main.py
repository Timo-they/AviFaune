

import sys

from PyQt5.QtWidgets import QApplication

import datas
import whole.datas_loader_saver as datas_loader_saver

from whole.window import OizoWindow

if __name__ == "__main__":
    print()
    print(datas.COLOR_GREEN, " - - - - - Start of Oizooo App - - - - - ", datas.COLOR_RESET)
    print()

    # L'application globale, pas besoin de toucher à quoique ce soit
    app = QApplication(sys.argv)

    print(datas.COLOR_BRIGHT_BLUE, "First got widgets : ", datas.widgets_, datas.COLOR_RESET)
    print()

    # C'est là que toute la fenêtre est construite
    win = OizoWindow()
    win.show()

    # Chargement de la feuille de style (c'est très stylé)
    qss_path = "style.qss"
    with open(qss_path, "r") as file:
        app.setStyleSheet(file.read())

    # Une fois que tout est en place, on charge les données pour qu'elles soient affichées joliment
    datas_loader_saver.load_datas()

    # Ca c'est juste pour vérifier que tous les widgets sont bien instanciés. Utile en débug.
    print()
    print(datas.COLOR_BRIGHT_BLUE, "Finally got widgets : ", datas.widgets_, datas.COLOR_RESET)

    # Finalement l'application est lancée réellement
    error = app.exec_()
    print()
    print(datas.COLOR_GREEN, " - - - - - End of Oizooo App - - - - - ", datas.COLOR_RESET)
    print()
    sys.exit(error)