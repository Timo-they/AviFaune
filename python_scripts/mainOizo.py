from PyQt5.QtWidgets import * # PyQt module for graphic components (controls, etc...)
from PyQt5.QtCore import * # PyQt core-module (threads, I/O, events,..)
from PyQt5.QtGui import * # PyQt module for graphics OpenGL-based, fonts, etc...

from IHM import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self) -> None: # create default constructor
       super(MainWindow, self).__init__()
       self.setupUi(self)


def main():
    import sys # Only needed for access to command line arguments

    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.

    C_INIT_FULL_SCREEN = 0 # full-screen GUI (0 : OFF, 1 : 0N) 

    h_application = QApplication(sys.argv) # create an application instance from the QApplication() class
    # only one instance of application is allowed per main program

    h_window = MainWindow() # create a main window instance from the MainWindow subclass

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
    