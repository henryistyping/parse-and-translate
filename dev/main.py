import sys

sys.path.insert(1, "./ui") # adds path for module in diff dir

from PySide6 import QtWidgets
from dev.main_window import MainScreen
# from marker_filter_ui import Ui_Marker_filter

app = QtWidgets.QApplication(sys.argv)

window = MainScreen()
window.show()

sys.exit(app.exec())
