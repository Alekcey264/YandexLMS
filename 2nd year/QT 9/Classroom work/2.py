import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QSize


class Car(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.lbl = QLabel(self)
        self.cur_car = "car1.png"
        self.pixmap = QPixmap(self.cur_car)
        self.lbl.setPixmap(self.pixmap)
        self.lbl.resize(49, 41)
        self.setMouseTracking(True)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            if self.cur_car == "car1.png":
                self.cur_car = "car2.png"
            elif self.cur_car == "car2.png":
                self.cur_car = "car3.png"
            else:
                self.cur_car = "car1.png"
        self.pixmap = QPixmap(self.cur_car)
        self.lbl.setPixmap(self.pixmap)
    
    def mouseMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        if x in range(0, 251) and y in range(0, 251):
            self.lbl.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    car = Car()
    car.show()
    sys.exit(app.exec())