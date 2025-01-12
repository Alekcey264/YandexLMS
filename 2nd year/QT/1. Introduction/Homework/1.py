import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel


class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 100)
        self.first_value = QLineEdit("0", self)
        self.first_value.move(10, 10)
        self.first_value.resize(40, 20)

        self.add_button = QPushButton("+", self)
        self.add_button.move(60, 5)
        self.add_button.resize(30, 30)
        self.add_button.clicked.connect(self.sum)

        self.substract_button = QPushButton("-", self)
        self.substract_button.move(90, 5)
        self.substract_button.resize(30, 30)
        self.substract_button.clicked.connect(self.sub)

        self.multiply_button = QPushButton("*", self)
        self.multiply_button.move(120, 5)
        self.multiply_button.resize(30, 30)
        self.multiply_button.clicked.connect(self.mul)

        self.second_value = QLineEdit("0", self)
        self.second_value.move(160, 10)
        self.second_value.resize(40, 20)
        
        self.label = QLabel("=", self)
        self.label.move(205, 10)

        self.result = QLineEdit(self)
        self.result.setReadOnly(True)
        self.result.move(215, 10)
        self.result.resize(40, 20)

        self.sum()

    def sum(self):
        self.result.setText(f"{int(self.first_value.text()) + int(self.second_value.text())}")

    def sub(self):
        self.result.setText(f"{int(self.first_value.text()) - int(self.second_value.text())}")

    def mul(self):
        self.result.setText(f"{int(self.first_value.text()) * int(self.second_value.text())}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wt = Arifmometr()
    wt.show()
    sys.exit(app.exec())