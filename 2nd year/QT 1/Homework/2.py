from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit
import sys


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1570, 100)
        self.alphabet = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..'
        }
        self.alphabet_buttons = dict()
        for key in self.alphabet.keys():
            self.alphabet_buttons[key] = QPushButton(key, self)
        self.def_x = 10
        self.def_y = 10
        for value in self.alphabet_buttons.values():
            value.move(self.def_x, self.def_y)
            value.resize(50, 50)
            value.clicked.connect(self.morse)
            self.def_x += 60
        self.result = QLineEdit('', self)
        self.result.move(10, 70)
        self.result.resize(1550, 20)

    def morse(self):
        self.result.setText(self.result.text() + self.alphabet[self.sender().text()])
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MorseCode()
    mc.show()
    sys.exit(app.exec())