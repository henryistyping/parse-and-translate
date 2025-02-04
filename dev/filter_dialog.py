from PySide6.QtWidgets import QDialog
import re  # regex

from ui.ui_filter_dialog import Ui_Marker_filter


class FilterDialog(QDialog, Ui_Marker_filter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Filter for text markers")
        
        # buttons
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        

    # Returns regex pattern from user input
    def getRegexPattern(self):
        #grab regex pattern from input fields in the dialog
        marker_start = self.startsWith_lineEdit.text()
        marker_end = self.EndsWith_lineEdit.text()
        return (marker_start, marker_end)
    
