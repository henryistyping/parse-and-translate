from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFileDialog, QMainWindow, QTableWidgetItem
from main_screen_ui import Ui_MainWindow


class MainScreen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Super Localizer")
        self.actionOpen.triggered.connect(
            self.browseFiles
        )  #://FIXME ask to save the current file bofore opening dialog window.

    def do_something(self):
        print("Hello, World!")

    def browseFiles(self):
        fileName = QFileDialog.getOpenFileName(
            self, "Open File", "", "All Files (*);;Text Files (*.txt)"
        )

        while self.mainTableWidget.rowCount() > 0:
            self.mainTableWidget.removeRow(0)

        if fileName[0]:
            f = open(fileName[0], "r")

            with f:
                data = f.readlines()
                self.populateTable(data)

    def populateTable(self, data):
        n = self.mainTableWidget.rowCount()
        self.mainTableWidget.setRowCount(n + len(data))  # hardcoded for now
        for i in data:
            item = item2 = QTableWidgetItem()
            self.mainTableWidget.setItem(n, 0, item)  # set source text
            item.setText(i)
            n = n + 1
