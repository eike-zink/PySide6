import json
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QTreeView, QVBoxLayout, QWidget, QPushButton
)
from PySide6.QtGui import QStandardItemModel,QStandardItem
from PySide6.QtGui import QColor

class PropertyEditorWidget(QWidget):
    def __init__(self, json_file):
        super().__init__()
        self.json_file = json_file
        self.properties = self.load_properties()

        # Erstelle ein QStandardItemModel für die Eigenschaften
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Eigenschaft", "Wert"])

        # Fülle das Model mit Eigenschaften
        self.populate_model()

        # Erstelle einen TreeView, um das Modell anzuzeigen
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)
        self.tree_view.expandAll()
        self.tree_view.setAlternatingRowColors(False)

        # Speichern-Button
        self.save_button = QPushButton("Speichern")
        self.save_button.clicked.connect(self.save_properties)

        # Layout setzen
        layout = QVBoxLayout(self)
        layout.addWidget(self.tree_view)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

    def load_properties(self):
        """Lädt Eigenschaften aus einer JSON-Datei."""
        with open(self.json_file, "r") as f:
            return json.load(f)

    def populate_model(self):
        """Füllt das QStandardItemModel mit Eigenschaften aus self.properties."""
        for group_name, group_properties in self.properties.items():
            # Erstelle ein Gruppenelement für jede Gruppe
            group_item = QStandardItem(group_name)
            group_item.setEditable(False)

            # Setze die Hintergrundfarbe der Gruppe
            # group_item.setBackground(QColor("#D3D3D3"))  # Hellgrau

            # Erstelle eine leere Zelle für den Wert-Spalteneintrag in der Gruppenzeile
            empty_value_item = QStandardItem()
            # empty_value_item.setBackground(QColor("#D3D3D3"))

            # Füge die Gruppenzeile dem Modell hinzu
            self.model.appendRow([group_item, empty_value_item])

            # Füge die Eigenschaften zur Gruppe hinzu
            for prop in group_properties:
                # Name der Eigenschaft
                prop_name_item = QStandardItem(prop["name"])
                prop_name_item.setEditable(False)

                # Wert der Eigenschaft
                if prop["type"] == "text":
                    prop_value_item = QStandardItem(prop["value"])
                    prop_value_item.setEditable(True)
                elif prop["type"] == "checkbox":
                    prop_value_item = QStandardItem()
                    prop_value_item.setCheckable(True)
                    prop_value_item.setCheckState(Qt.Checked if prop["value"] else Qt.Unchecked)
                    prop_value_item.setEditable(False)

                # Füge das Paar (Name, Wert) zur Gruppe hinzu
                group_item.appendRow([prop_name_item, prop_value_item])

    def save_properties(self):
        """Speichert die aktuellen Eigenschaften zurück in die JSON-Datei."""
        updated_properties = {}

        for i in range(self.model.rowCount()):
            group_item = self.model.item(i)
            group_name = group_item.text()
            updated_properties[group_name] = []

            # Gehe jede Eigenschaft in der Gruppe durch
            for j in range(group_item.rowCount()):
                prop_name_item = group_item.child(j, 0)
                prop_value_item = group_item.child(j, 1)

                # Speichere den Namen und den aktuellen Wert der Eigenschaft
                prop = {"name": prop_name_item.text()}
                if prop_value_item.isCheckable():
                    prop["type"] = "checkbox"
                    prop["value"] = prop_value_item.checkState() == Qt.Checked
                else:
                    prop["type"] = "text"
                    prop["value"] = prop_value_item.text()

                updated_properties[group_name].append(prop)

        # Schreibe die aktualisierten Eigenschaften in die JSON-Datei zurück
        with open(self.json_file, "w") as f:
            json.dump(updated_properties, f, indent=4)

# Anwendung starten und Eigenschaften aus JSON-Datei laden
app = QApplication([])
window = PropertyEditorWidget("properties_04.json")
window.show()
app.exec()
