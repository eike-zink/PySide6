from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QLineEdit, QVBoxLayout, QWidget, QCheckBox

class PropertyEditorWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Erstelle ein TreeWidget für die Eigenschaften
        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(2)
        self.tree_widget.setHeaderLabels(["Eigenschaft", "Wert"])

        # Beispiel: Gruppe von Eigenschaften hinzufügen
        group_item = QTreeWidgetItem(self.tree_widget, ["Gruppe 1"])
        group_item.setExpanded(True)  # Gruppe ist zunächst aufgeklappt

        # Beispiel-Eigenschaft mit Textfeld
        property1 = QTreeWidgetItem(group_item, ["Eigenschaft 1"])
        editor1 = QLineEdit("Wert 1")
        self.tree_widget.setItemWidget(property1, 1, editor1)

        # Beispiel-Eigenschaft mit Checkbox
        property2 = QTreeWidgetItem(group_item, ["Eigenschaft 2"])
        checkbox2 = QCheckBox()
        checkbox2.setChecked(False)  # Beispielwert: Checkbox standardmäßig aktiviert
        self.tree_widget.setItemWidget(property2, 1, checkbox2)

        # Weitere Gruppe mit einer Checkbox hinzufügen
        group_item2 = QTreeWidgetItem(self.tree_widget, ["Gruppe 2"])
        group_item2.setExpanded(True)

        property3 = QTreeWidgetItem(group_item2, ["Eigenschaft 3"])
        checkbox3 = QCheckBox("Aktiviert")
        checkbox3.setChecked(True)  # Beispielwert: Checkbox standardmäßig deaktiviert
        self.tree_widget.setItemWidget(property3, 1, checkbox3)

        # Layout setzen
        layout = QVBoxLayout(self)
        layout.addWidget(self.tree_widget)
        self.setLayout(layout)

# Anwendung starten
app = QApplication([])
window = PropertyEditorWidget()
window.show()
app.exec()
