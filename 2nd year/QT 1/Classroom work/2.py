import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 60)
        self.first_value = QLineEdit(self)
        self.first_value.resize(160, 20)
        self.first_value.move(10, 30)

        self.first_label = QLabel("Выражение:", self)
        self.first_label.move(10, 10)

        self.trick_button = QPushButton("->", self)
        self.trick_button.resize(40, 30)
        self.trick_button.move(180, 25)
        self.trick_button.clicked.connect(self.calculate)

        self.second_label = QLabel("Результат:", self)
        self.second_label.move(230, 10)

        self.second_value = QLineEdit(self)
        self.second_value.resize(160, 20)
        self.second_value.move(230, 30)

    def calculate(self):
        self.second_value.setText(str(eval(self.first_value.text())))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wt = Evaluator()
    wt.show()
    sys.exit(app.exec())