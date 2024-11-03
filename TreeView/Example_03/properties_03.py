import json
from PySide6.QtWidgets import (
    QApplication, QTreeWidget, QTreeWidgetItem, QLineEdit, QVBoxLayout, QWidget, QCheckBox, QPushButton
)

class PropertyEditorWidget(QWidget):
    def __init__(self, json_file):
        super().__init__()
        self.json_file = json_file
        self.properties = self.load_properties()

        # Erstelle ein TreeWidget für die Eigenschaften
        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(2)
        self.tree_widget.setHeaderLabels(["Eigenschaft", "Wert"])

        # Fülle das TreeWidget mit Eigenschaften
        self.populate_tree_widget()

        # Speichern-Button
        self.save_button = QPushButton("Speichern")
        self.save_button.clicked.connect(self.save_properties)

        # Layout setzen
        layout = QVBoxLayout(self)
        layout.addWidget(self.tree_widget)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

    def load_properties(self):
        """Lädt Eigenschaften aus einer JSON-Datei."""
        with open(self.json_file, "r") as f:
            return json.load(f)

    def populate_tree_widget(self):
        """Füllt das TreeWidget mit Eigenschaften aus self.properties."""
        for group_name, group_properties in self.properties.items():
            # Erstelle ein Gruppenelement für jede Gruppe
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

    def save_properties(self):
        """Speichert die aktuellen Eigenschaften zurück in die JSON-Datei."""
        for i in range(self.tree_widget.topLevelItemCount()):
            group_item = self.tree_widget.topLevelItem(i)
            group_name = group_item.text(0)

            # Gehe jede Eigenschaft in der Gruppe durch
            for j in range(group_item.childCount()):
                prop_item = group_item.child(j)
                prop_name = prop_item.text(0)
                prop_editor = self.tree_widget.itemWidget(prop_item, 1)

                # Finde die entsprechende Eigenschaft in self.properties und aktualisiere den Wert
                for prop in self.properties[group_name]:
                    if prop["name"] == prop_name:
                        if prop["type"] == "text":
                            prop["value"] = prop_editor.text()
                        elif prop["type"] == "checkbox":
                            prop["value"] = prop_editor.isChecked()

        # Schreibe die aktualisierten Eigenschaften in die JSON-Datei zurück
        with open(self.json_file, "w") as f:
            json.dump(self.properties, f, indent=4)

# Anwendung starten und Eigenschaften aus JSON-Datei laden
app = QApplication([])
window = PropertyEditorWidget("properties_03.json")
window.show()
app.exec()
