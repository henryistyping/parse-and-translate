from PySide6.QtWidgets import QDialog
import re  # regex

from ui.marker_dialog_ui import Ui_Marker_filter


class FilterDialog(QDialog, Ui_Marker_filter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Filtering for text markers")
        # return self.okay_buttonBox.accepted.connect(self.filter)

    # Get regex pattern from user
    def getRegexPattern(self):
        return self.lineEditRegex.text()
