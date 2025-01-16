from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFileDialog, QMainWindow
from main_screen_ui import Ui_MainWindow


class MainScreen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Super Localizer")
        self.actionOpen.triggered.connect(self.do_something)

    def do_something(self):
        print("Hello, World!")
