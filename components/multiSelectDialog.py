from PySide6.QtWidgets import QDialog, QVBoxLayout, QListWidget, QDialogButtonBox

class MultiSelectDialog(QDialog):
    def __init__(self, options):
        super().__init__()
        self.setWindowTitle("Select Way points")

        self.layout = QVBoxLayout()
        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QListWidget.MultiSelection)

        for option in options:
            self.list_widget.addItem(option)

        self.layout.addWidget(self.list_widget)

        # Buttons for dialog
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)

    def get_selected_items(self):
        """Returns a list of selected items."""
        selected_items = self.list_widget.selectedItems()
        return [item.text() for item in selected_items]