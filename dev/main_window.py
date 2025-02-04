from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QMainWindow,
    QTableWidgetItem,
    QHeaderView,
    QMessageBox,
)
import json
import os
import shutil
import re

# modules
from ui.ui_main_screen import Ui_MainWindow
from filter_dialog import FilterDialog


class MainScreen(QMainWindow, Ui_MainWindow):
    # Steps when initlizing
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Super Localizer")

        # Action menu items
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveProjectFile)
        self.actionExport.triggered.connect(self.exportFile)

        # Action Resize table
        self.setupTable()

        # Init storage for lines
        self.project_data = None
        self.current_project_path = None
        self.original_file_path = None

        # Marker filter dialog
        self.marker_start = None
        self.marker_end = None

    def setupTable(self):
        # stretch the headers out
        header = self.mainTableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        self.mainTableWidget.setWordWrap(True)
        self.mainTableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )

    # STRETCH: Turn the file browsing section into its own class
    """
        1. Open a file using a FileDialog (explorer window)
        2. Remember the source file path
        3. Read the content of the file
        4. Copy all of source texts as project_data
        5. Start filtering the lines by regex pattern
        6. Populate the table with the filtered lines 
    """

    # TODO: Maybe separate the function into opening project file and opening source files? PROBABLY
    def openFile(self):
        (
            fileName,
            _,
        ) = QFileDialog.getOpenFileName(  # Returns file path and filter string, but we're only interested in the file path
            self,
            "Open File",
            "",
            "All Files (*);;Text Files (*.txt);;Project Files (*.trpj)",
        )

        if fileName:
            # If user does select file, clear table
            while self.mainTableWidget.rowCount() > 0:
                self.mainTableWidget.removeRow(0)

            # if user opens the project file
            if fileName.endswith(".trpj"):
                lines = self.project_data = json.load(open(fileName, "r"))

            # if user opens a new text file
            else:
                # read the content of the file
                f = open(fileName, "r")

                # STRETCH 1: Filter for specific markers (beginning and end of string)
                # STRETCH 2: allow multiple lines
                # STRETCH 3: Remember the markers used
                with f:
                    lines = f.readlines()  # turns lines into arrays

                # TODO: refactor this into a function
                # FIXME: build a better if statement for this
                # Init and copy all source texts into project_data
                self.project_data = [{"original": line, "translated": ""} for line in lines]

                # TODO: refactor this into a function
                # TODO: Decision pending - Decide whether to show this dialog window after user has select file or after the source texts have been set to table.
                # Open dialog window to grab filter patterns
                filter_dialog = FilterDialog(self)
                if filter_dialog.exec():  # if user clicks ok
                    if not filter_dialog.getRegexPattern() == ("", ""):
                        # temp fix when use has no regex pattern set
                        regex_pattern = filter_dialog.getRegexPattern()

                        # sanity check
                        print(regex_pattern)

                        # start filtering the lines by regex pattern
                        lines = self._filter_lines(lines, regex_pattern)

            # save the source file path / ?: set project path
            self.original_file_path = fileName
            self.current_project_path = None  # Reset the project path

            # populate the table using the filtered lines
            self._populateTable(lines)
            print(lines)

    def _filter_lines(self, lines, regex_pattern):
        # Filters the lines based on the regex pattern
        return [line for line in lines if re.search(regex_pattern, line)]

    def _populateTable(self, lines):

        # Ensure the table has enough rows for the data
        self.mainTableWidget.setRowCount(len(lines))

        # If the project data was from previous project file
        if self.project_data[0]["translated"] != "":
            for index, item in enumerate(self.project_data):
                self._setTableItem(index, 0, item["original"], editable=False)
                self._setTableItem(index, 1, item["translated"], editable=True)
        # If not
        else:
            for row, line in enumerate(lines):
                # Set both columns up
                self._setTableItem(row, 0, line, editable=False)
                self._setTableItem(row, 1, line, editable=True)
            

    def _setTableItem(self, row, column, text, editable=False):
        # Set a specific item in the table
        item = QTableWidgetItem(text)
        flags = item.flags()

        if not editable:
            item.setFlags(flags & ~Qt.ItemIsEditable)
        else:
            item.setFlags(flags | Qt.ItemIsEditable)

        self.mainTableWidget.setItem(row, column, item)

        """
        Save current work as project file (original and translated text) as JSON file
        """

    # Save project file under same name as before if it's from a previously made project file
    def saveProjectFile(self):
        # Check if there is any data
        # TODO: Disable save button if there's no data; delete the line 146
        if not self.project_data:
            QMessageBox.warning(self, "Warning", "No data to save")
            return

        # Opens up a Explorer Dialog to save the file
        # We ignore the filter string as _
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Proeject File",
            "untitled.trpj",
            "Translation Project (*.trpj);;All Files (*)",
        )

        # if user doesn't select a file
        if not file_path:
            return

        # Add .trpj to the file path
        if not file_path.endswith(".trpj"):
            file_path += ".trpj"

        # Collect traslated text from table
        for row in range(self.mainTableWidget.rowCount()):
            self.project_data[row]["translated"] = self.mainTableWidget.item(
                row, 1
            ).text()

        # Save the file as JSON
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.project_data, f, ensure_ascii=False)

        self.current_project_path = file_path
        QMessageBox.information(self, "Success", "File saved successfully")
        # STRETCH: Give user two options:
        # 1. Save project file as new
        # 2. Overwrite project file that the data were called from

    def exportFile(self):
        # export translated text to a new file, matching original format
        if not self.project_data:
            QMessageBox.warning(self, "Warning", "No data to export")
            return

        # Opens up a Explorer Dialog to save the file
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Export Translated File", "", "Text Files (*.txt)"
        )
        if not file_name:
            return

        # Collect translated text from table
        translated_lines = [
            item["translated"] if item["translated"] else item["original"]
            for item in self.project_data
        ]

        with open(file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(translated_lines))

        QMessageBox.information(self, "Success", "File exported successfully!")
