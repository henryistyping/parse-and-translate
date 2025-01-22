from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QHeaderView
from main_screen_ui import Ui_MainWindow

class MainScreen(QMainWindow, Ui_MainWindow):
    # Steps when initlizing
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Super Localizer")
        
        # Action Resize table
        self.setupTable()
        
        # Action open file
        self.actionOpen.triggered.connect(self.browseFiles)
        #://TODO ask to save the current file bofore opening dialog window.
        

    def do_something(self):
        print("Hello, World!")

    def setupTable(self):
        # stretch the headers out
        header = self.mainTableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

    def browseFiles(self):
        fileName = QFileDialog.getOpenFileName(
            self, "Open File", "", "All Files (*);;Text Files (*.txt)"
        )

        if fileName[0]:
            # clear the table
            while self.mainTableWidget.rowCount() > 0:
                self.mainTableWidget.removeRow(0)

            # read the content of the file
            f = open(fileName[0], "r")

            # TODO: ask if user wants to filter for any markers in the strings
            # STRETCH: allow options for multiple markers
            # STRETCH: hold the markers in memory, so that they're not lost even if you choose radio choice: no
            
            # open the dialog window
            self.open_dialog_marker()

            with f:
                lines = f.readlines()
            self._populateTable(lines)

    def open_dialog_marker(self):
        # opens the dialog window for filtering marker
        pass
        
        

    def _populateTable(self, lines):

        # Ensure the table has enough rows for the data
        self.mainTableWidget.setRowCount(len(lines))

        for row, line in enumerate(lines):
            text = line.strip()  # strip of any leading or trailing whitespaces

            # Set both columns up
            self._setTableItem(row, 0, text, editable=False)
            self._setTableItem(row, 1, text, editable=True)

    def _setTableItem(self, row, column, text, editable=False):
        # Set a specific item in the table
        item = QTableWidgetItem(text)
        flags = item.flags()

        if not editable:
            item.setFlags(flags & ~Qt.ItemIsEditable)
        else:
            item.setFlags(flags | Qt.ItemIsEditable)

        self.mainTableWidget.setItem(row, column, item)
        
        # Make the words wrap around in the cell
        self.mainTableWidget.setWordWrap(True)
        self.mainTableWidget.resizeRowsToContents()
