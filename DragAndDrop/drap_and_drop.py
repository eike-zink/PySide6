import sys

from PySide6 import QtWidgets, QtCore, QtGui


class DragButton(QtWidgets.QPushButton):
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            drag = QtGui.QDrag(self)
            mine = QtCore.QMimeData()
            drag.setMimeData(mine)

            drag.exec(QtCore.Qt.MoveAction)


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

        self.layout = QtWidgets.QHBoxLayout()
        for label in ['A', 'B', 'C', 'D', 'E', 'F']:
            btn = DragButton(label)
            self.layout.addWidget(btn)

        self.setLayout(self.layout)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        pos = event.pos()
        widget = event.source()

        for n in range(self.layout.count()):
            # Get the widget at each index in turn
            w = self.layout.itemAt(n).widget()
            if pos.x() < w.x() + w.size().width() // 2:
                self.layout.insertWidget(n-1, widget)
                break

        event.accept()


app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
