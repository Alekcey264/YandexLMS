from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QRadioButton, QLabel
import sys


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 190, 300)
        self.x_radio = QRadioButton("X", self)
        self.x_radio.move(60, 20)
        self.x_radio.setChecked(True)
        self.x_radio.clicked.connect(self.change)
        self.o_radio = QRadioButton("O", self)
        self.o_radio.move(110, 20)
        self.o_radio.clicked.connect(self.change)
        self.button_grid = [
            QPushButton('', self), QPushButton('', self), QPushButton('', self),
            QPushButton('', self), QPushButton('', self), QPushButton('', self),
            QPushButton('', self), QPushButton('', self), QPushButton('', self),
        ]
        [item.resize(50, 50) for item in self.button_grid]
        [item.clicked.connect(self.fill) for item in self.button_grid]
        self.def_x = 10
        self.def_y = 50
        for i in range(3):
            self.button_grid[(i * 3)].move(10, self.def_y)
            self.button_grid[(i * 3) + 1].move(70, self.def_y)
            self.button_grid[(i * 3) + 2].move(130, self.def_y)
            self.def_y += 60
        self.result = QLabel('', self)
        self.result.move(85, 240)
        self.new_game_button = QPushButton('Новая игра', self)
        self.new_game_button.move(60, 260)
        self.new_game_button.clicked.connect(self.reset)
        self.text = 'X'
        
    def change(self):
        if self.sender().text() == 'X':
            self.text = 'X'
        else:
            self.text = 'O'
        self.reset()

    def reset(self):
        [item.setText('') for item in self.button_grid]
        self.result.setText('')

    def fill(self):
        if self.sender().text() == '':
            self.sender().setText(self.text)
            if self.text == "X":
                self.text = "O"
            else:
                self.text = "X"



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ttt = TicTacToe()
    ttt.show()
    sys.exit(app.exec())