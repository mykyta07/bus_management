from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget
from PySide6.QtGui import QAction
from ui_index import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Bus Management")