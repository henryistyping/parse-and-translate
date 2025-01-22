from PySide6.QtWidgets import QDialog

from ui.marker_dialog_ui import Ui_Marker_filter

class MarkerFilterDialog(QDialog, Ui_Marker_filter):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setupUi(self)
    self.setWindowTitle("Filtering for text markers")