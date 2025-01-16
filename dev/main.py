import sys

sys.path.insert(1, "./main_screen_ui") # adds path for module in diff dir

from PySide6 import QtWidgets
from main_screen_logic import MainScreen

app = QtWidgets.QApplication(sys.argv)

window = MainScreen()
window.show()

sys.exit(app.exec())
