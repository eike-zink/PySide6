from PySide6.QtWidgets import (
    QApplication, QTreeWidget, QTreeWidgetItem, QLineEdit, QVBoxLayout, QWidget, QCheckBox
)

class PropertyEditorWidget(QWidget):
    def __init__(self, properties):
        super().__init__()

        # Erstelle ein TreeWidget für die Eigenschaften
        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(2)
        self.tree_widget.setHeaderLabels(["Eigenschaft", "Wert"])

        # Iteriere über die Liste der Eigenschaften und füge sie dynamisch hinzu
        for group_name, group_properties in properties.items():
            # Erstelle ein Gruppenelement für jede Eigenschaftengruppe
            group_item = QTreeWidgetItem(self.tree_widget, [group_name])
            group_item.setExpanded(True)

            # Füge die Eigenschaften zur Gruppe hinzu
            for prop in group_properties:
                prop_item = QTreeWidgetItem(group_item, [prop["name"]])

                # Erstelle das passende Eingabefeld basierend auf dem Typ
                if prop["type"] == "text":
                    editor = QLineEdit(prop["value"])
                    self.tree_widget.setItemWidget(prop_item, 1, editor)
                elif prop["type"] == "checkbox":
                    editor = QCheckBox()
                    editor.setChecked(prop["value"])
                    self.tree_widget.setItemWidget(prop_item, 1, editor)

        # Layout setzen
        layout = QVBoxLayout(self)
        layout.addWidget(self.tree_widget)
        self.setLayout(layout)

# Beispiel-Datenstruktur für Eigenschaften
properties = {
    "Gruppe 1": [
        {"name": "Eigenschaft 1", "type": "text", "value": "Wert 1"},
        {"name": "Eigenschaft 2", "type": "checkbox", "value": True},
    ],
    "Gruppe 2": [
        {"name": "Eigenschaft 3", "type": "text", "value": "Wert 3"},
        {"name": "Eigenschaft 4", "type": "checkbox", "value": False},
    ]
}

# Anwendung starten
app = QApplication([])
window = PropertyEditorWidget(properties)
window.show()
app.exec()
