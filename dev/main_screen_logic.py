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
                lines = f.readlines()
            self.populateTable(lines)

    def populateTable(self, lines):

        # Ensure the table has enough rows for the data
        self.mainTableWidget.setRowCount(len(lines))

        for row, line in enumerate(lines):
            text = line.strip()  # strip of any leading or trailing whitespaces

            # Set the first column (non-editable)
            item_original = QTableWidgetItem(text)
            item_original.setFlags(item_original.flags() & ~Qt.ItemIsEditable)
            self.mainTableWidget.setItem(row, 0, item_original)

            # Set the second column (editable)
            item_editable = QTableWidgetItem(text)
            item_editable.setFlags(item_editable.flags() | Qt.ItemIsEditable)
            self.mainTableWidget.setItem(row, 1, item_editable)
