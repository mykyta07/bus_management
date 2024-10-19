from PySide6.QtWidgets import QApplication
from frontPage import MainWindow
import sys

app = QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec()

# don't forget to change encoding of ui_index.py to utf-8