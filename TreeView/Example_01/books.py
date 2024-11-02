import sys

from PySide6 import QtWidgets
from xml.etree import ElementTree


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.tree = QtWidgets.QTreeWidget(self)
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Struktur', 'Daten'])
        self.tree.itemClicked.connect(self.on_item_clicked)
        self.layout.addWidget(self.tree)
        self.setLayout(self.layout)

        books = open("books.xml", "r").read()
        self.show_books(books)

    def show_books(self, books: str):
        tree = ElementTree.fromstring(books)
        catalog = QtWidgets.QTreeWidgetItem([tree.tag])
        self.tree.addTopLevelItem(catalog)

        def show_elements(node, elements):
            for element in elements:
                branch = QtWidgets.QTreeWidgetItem()
                branch.setText(0, element.tag)
                if element.tag == 'book':
                    branch.setText(1, element.attrib['id'])
                else:
                    branch.setText(1, element.text)
                node.addChild(branch)
                show_elements(branch, element)

        show_elements(catalog, tree.findall(".//book"))

    def on_item_clicked(self, item):
        path = self.get_parent_path(item)
        print(f'Click on item {item.text(0)} with data: {item.text(1)}, path: {path}')

    def get_parent_path(self, item):
        def get_parent(item, full_path):
            if item.parent() is None:
                return full_path
            full_path = item.parent().text(0) + '/' + full_path
            return get_parent(item.parent(), full_path)

        return get_parent(item, item.text(0))


app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
