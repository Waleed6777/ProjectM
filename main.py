from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)         # This starts the Qt app engine
    window = MainWindow()                # This creates your main window
    window.show()                        # This shows the window
    sys.exit(app.exec())                 # This keeps the app running until you close it

