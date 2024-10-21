from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QRadioButton
import sys


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.x_radio = QRadioButton("X", self)
        self.x_radio.move(200, 20)
        self.x_radio.setChecked(True)
        self.y_radio = QRadioButton("Y", self)
        self.y_radio.move(250, 20)
        self.button_grid = [
            QPushButton('', self), QPushButton('', self), QPushButton('', self),
            QPushButton('', self), QPushButton('', self), QPushButton('', self),
            QPushButton('', self), QPushButton('', self), QPushButton('', self),
        ]
        self.def_x = 10
        self.def_y = 50
        for i in range(3):
            for j in range(len(self.button_grid)):
                self.button_grid[i].move(self.def_x, self.def_y + 60 * j)
                self.button_grid[i].resize(50, 50)
                self.def_x += 60
            self.def_x = 10



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ttt = TicTacToe()
    ttt.show()
    sys.exit(app.exec())