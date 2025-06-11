from PyQt6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Suno - Audio Enhancer")

        # UI elements
        self.label = QLabel("No file selected")
        self.select_button = QPushButton("Choose Audio File")
        self.enhance_button = QPushButton("Enhance (not working yet)")

        # Connect file chooser to function
        self.select_button.clicked.connect(self.choose_file)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_button)
        layout.addWidget(self.enhance_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def choose_file(self):
        file_dialog = QFileDialog()
        filename, _ = file_dialog.getOpenFileName(
            self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)"
        )
        if filename:
            self.label.setText(os.path.basename(filename))

