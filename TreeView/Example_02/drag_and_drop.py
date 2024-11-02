import sys

from PySide6 import QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.model = QtGui.QStandardItemModel()

        for k in range(0, 40):
            parent_item = self.model.invisibleRootItem()
            for i in range(0, 4):
                item = QtGui.QStandardItem(str(f'Item {k}.{i}'))
                parent_item.appendRow(item)
                parent_item = item

        self.view = QtWidgets.QTreeView()
        self.view.setModel(self.model)
        self.view.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

        self.setCentralWidget(self.view)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()