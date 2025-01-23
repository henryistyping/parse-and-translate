from PySide6.QtWidgets import QDialog
import re  # regex

from ui.marker_dialog_ui import Ui_Marker_filter


class MarkerFilterDialog(QDialog, Ui_Marker_filter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Filtering for text markers")
        # return self.okay_buttonBox.accepted.connect(self.filter)

    # Receive lines from the MainWindow
    def setLines(self, lines):
        self.lines = lines
        

    def handleUpdatedLines(self):

        if self.yes_radioButton.isChecked():
            start_char = re.escape(self.startsWith_lineEdit.text())
            end_char = re.escape(self.endsWith_lineEdit.text())
            pattern = rf"^{start_char}.*{end_char}$"

            return re.finall(pattern)
        # TODO: add options for multiple markers
        # TODO: pass all matching strings to the main window
