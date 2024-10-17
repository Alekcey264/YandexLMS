import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton


class WordTrick(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 40)
        self.first_value = QLineEdit(self)
        self.first_value.resize(160, 20)
        self.first_value.move(10, 10)

        self.trick_button = QPushButton("->", self)
        self.trick_button.resize(40, 30)
        self.trick_button.move(180, 5)
        self.trick_button.clicked.connect(self.move_word)

        self.second_value = QLineEdit(self)
        self.second_value.resize(160, 20)
        self.second_value.move(230, 10)

    def move_word(self):
        if self.trick_button.text() == "->":
            temp_text = self.first_value.text()
            self.first_value.setText("")
            self.second_value.setText(temp_text)
            self.trick_button.setText("<-")
        else:
            temp_text = self.second_value.text()
            self.second_value.setText("")
            self.first_value.setText(temp_text)
            self.trick_button.setText("->")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wt = WordTrick()
    wt.show()
    sys.exit(app.exec())