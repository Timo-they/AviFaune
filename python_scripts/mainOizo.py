
from PyQt5.QtWidgets import * # PyQt module for graphic components (controls, etc...)
from PyQt5.QtCore import * # PyQt core-module (threads, I/O, events,..)
from PyQt5.QtGui import * # PyQt module for graphics OpenGL-based, fonts, etc...

from mainWindow import MainWindow

C_INIT_FULL_SCREEN = 0 # full-screen GUI (0 : OFF, 1 : 0N)

def main():
    h_application = QApplication([])
    h_window = MainWindow()

    if C_INIT_FULL_SCREEN:
        h_window.setGeometry(QScreen.availableGeometry(QApplication.primaryScreen())) # full screen
    else:
        h_window.move(QScreen.availableGeometry(QApplication.primaryScreen()).center()) # center

    h_window.show() # show the main window (as it's running in hidden mode by default)

    h_event_loop = h_application.exec_()  # Start the event loop.

    # Your application won't reach here until you exit and the event loop has stopped.
    sys.exit(h_event_loop)

if __name__ == '__main__':
    main()
