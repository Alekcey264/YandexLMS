import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class UfoControl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(250, 250, 300, 300)
        self.ufo = QLabel(self)
        self.ufo.setPixmap(QPixmap('ufo.png'))
        self.ufo.setGeometry(0, 0, 50, 50)

    def keyPressEvent(self, event):
        x = self.ufo.pos().x()
        y = self.ufo.pos().y()
        if event.key() == Qt.Key.Key_Right:
            x += 10
            if x > 250:
                x = 0
        elif event.key() == Qt.Key.Key_Left:
            x -= 10
            if x < 0:
                x = 250
        elif event.key() == Qt.Key.Key_Up:
            y -= 10
            if y < 0:
                y = 250
        elif event.key() == Qt.Key.Key_Down:
            y += 10
            if y > 250:
                y = 0
        self.ufo.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    uc = UfoControl()
    uc.show()
    sys.exit(app.exec())