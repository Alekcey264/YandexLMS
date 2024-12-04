import sys

from PyQt6.QtWidgets import QPushButton, QWidget, QApplication
from random import randint


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(250, 250, 300, 300)
        self.button = QPushButton('Нажми меня', self)
        self.button.setGeometry(randint(100, 200), randint(50, 250), 100, 50)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        x, y = event.pos().x(), event.pos().y()
        b_x, b_y = self.button.pos().x(), self.button.pos().y()
        if x in range(b_x - 10, b_x + 110) and y in range(b_y - 10, b_y + 65):
            b_x = randint(0, 200)
            b_y = randint(0, 250)
        self.button.move(b_x, b_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MyWidget()
    mw.show()
    sys.exit(app.exec())