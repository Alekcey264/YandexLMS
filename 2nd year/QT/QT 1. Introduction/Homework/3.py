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
        self.current_move = 'X'
        self.x_radio.clicked.connect(self.change)
        self.o_radio = QRadioButton("O", self)
        self.o_radio.move(110, 20)
        self.o_radio.clicked.connect(self.change)
        self.button_grid = [
            [QPushButton('', self), QPushButton('', self), QPushButton('', self)],
            [QPushButton('', self), QPushButton('', self), QPushButton('', self)],
            [QPushButton('', self), QPushButton('', self), QPushButton('', self)],
        ]
        [[item.resize(50, 50) for item in item1] for item1 in self.button_grid]
        [[item.clicked.connect(self.fill) for item in item1] for item1 in self.button_grid]
        self.def_x = 10
        self.def_y = 50
        for i in range(3):
            self.button_grid[i][0].move(10, self.def_y)
            self.button_grid[i][1].move(70, self.def_y)
            self.button_grid[i][2].move(130, self.def_y)
            self.def_y += 60
        self.result = QLabel('', self)
        self.result.resize(80, 20)
        self.result.move(60, 240)
        self.new_game_button = QPushButton('Новая игра', self)
        self.new_game_button.move(60, 260)
        self.new_game_button.clicked.connect(self.reset)
        self.text = 'X'
        
    def change(self):
        if self.sender().text() == 'X' and self.current_move != 'X':
            self.current_move = 'X'
            self.text = 'X'
            self.reset()
        elif self.sender().text() == 'O' and self.current_move != 'O':
            self.current_move = 'O'
            self.text = 'O'
            self.reset()

    def reset(self):
        [[item.setText('') for item in item1] for item1 in self.button_grid]
        [[item.setEnabled(True) for item in item1] for item1 in self.button_grid]
        self.result.setText('')

    def fill(self):
        if self.sender().text() == '':
            self.sender().setText(self.text)
            if self.text == "X":
                self.text = "O"
            else:
                self.text = "X"
        self.check_win()
    
    def check_win(self):
        winning_combinations = [
            ((0, 0), (0, 1), (0, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 0), (1, 1), (2, 2)),
            ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), ((0, 2), (1, 1), (2, 0)),
            ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2))
        ]
        
        for combo in winning_combinations:
            c_1st = combo[0][0]
            c_2nd = combo[0][1]
            c_3rd = combo[1][0]
            c_4th = combo[1][1]
            if self.button_grid[c_1st][c_2nd].text() == self.button_grid[c_3rd][c_4th].text():
                c_1st = combo[2][0]
                c_2nd = combo[2][1]
                if self.button_grid[c_3rd][c_4th].text() == self.button_grid[c_1st][c_2nd].text():
                    if self.button_grid[c_1st][c_2nd].text() in {'X', 'O'}:
                        [[item.setEnabled(False) for item in item1] for item1 in self.button_grid]
                        self.result.setText(f'Выиграл {self.button_grid[c_1st][c_2nd].text()}!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ttt = TicTacToe()
    ttt.show()
    sys.exit(app.exec())