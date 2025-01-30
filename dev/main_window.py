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

# modules
from ui.main_screen_ui import Ui_MainWindow
from marker_dialog import FilterDialog


class MainScreen(QMainWindow, Ui_MainWindow):
    # Steps when initlizing
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Super Localizer")

        # Action menu items
        self.actionOpen.triggered.connect(self.browseFiles)
        self.actionSave.triggered.connect(self.saveProjectFile)
        self.actionExport.triggered.connect(self.exportFile)

        # Action Resize table
        self.setupTable()

        # Init storage for lines
        self.project_data = None
        self.current_project_path = None
        self.original_file_path = None

        # Marker filter dialog
        self.marker = None

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
    def browseFiles(self):
        fileName, _ = (
            QFileDialog.getOpenFileName(  # Returns file path and filter string, but we're only interested in the file path
                self, "Open File", "", "All Files (*);;Text Files (*.txt)"
            )
        )

        # if user doesn't select a file
        if not fileName:
            return

        self.original_file_path = fileName

        if fileName[0]:
            # clear the table
            while self.mainTableWidget.rowCount() > 0:
                self.mainTableWidget.removeRow(0)

            # read the content of the file
            f = open(fileName[0], "r")

            # STRETCH: allow options for multiple markers

            # opens the dialog window
            with f:
                lines = f.readlines()  # turns lines into arrays

            # Open the dialog window to filter the lines
            dialog = self.FilterDialog(self)
            if dialog.exec():
                regex_pattern = dialog.getRegexPattern()
                lines = self._filter_lines(lines, regex_pattern)

            self._populateTable(lines)

            # Init project data
            self.project_data = [{"original": line, "translated": ""} for line in lines]
            self.current_project_path = None  # Reset the project path

    def _filter_lines(self, lines, regex_pattern):
        # Filters the lines based on the regex pattern
        import re

        return [line for line in lines if re.search(regex_pattern, line)]

    def _populateTable(self, lines):

        # Ensure the table has enough rows for the data
        self.mainTableWidget.setRowCount(len(lines))

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

    def saveProjectFile(self):
        # Save current project dat (original and translated text) in JSON file

        # Check if there is any data // normally Save option should be disabled if there is no data
        if not self.project_data:
            QMessageBox.warning(self, "Warning", "No data to save")
            return

        # Opens up a Explorer Dialog to save the file
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Translated File", "", "Text Files (*.txt)"
        )
        if not file_name:
            return

        # Collect traslated text from table
        for row in range(self.mainTableWidget.rowCount()):
            self.project_data[row]["translated"] = self.mainTableWidget.item(
                row, 1
            ).text()

        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(self.project_data, f, indent=4, ensure_ascii=False)

        self.current_project_path = file_name
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
