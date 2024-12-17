import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QLCDNumber


class MiniCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 120)
        self.first_label = QLabel("Первое число (целое):", self)
        self.number_1 = QLineEdit(self)
        self.second_label = QLabel("Второе число (целое):", self)
        self.number_2 = QLineEdit(self)
        self.calculate_button = QPushButton("->", self)
        self.sum_label = QLabel("Сумма:", self)
        self.sub_label = QLabel("Разность:", self)
        self.mul_label = QLabel("Произведение:", self)
        self.div_label = QLabel("Частное:", self)
        self.result_sum = QLCDNumber(self)
        self.result_sub = QLCDNumber(self)
        self.result_mul = QLCDNumber(self)
        self.result_div = QLCDNumber(self)

        self.first_label.move(10, 10)
        
        self.number_1.move(10, 30)
        self.number_1.resize(100, 20)

        self.second_label.move(10, 70)

        self.number_2.move(10, 90)
        self.number_2.resize(100, 20)

        self.calculate_button.move(120, 45)
        self.calculate_button.resize(40, 30)
        self.calculate_button.clicked.connect(self.calculate)

        self.sum_label.move(180, 15)
        
        self.sub_label.move(180, 40)

        self.mul_label.move(180, 65)
        
        self.div_label.move(180, 90)

        self.result_sum.move(290, 10)
        self.result_sum.resize(100, 25)

        self.result_sub.move(290, 35)
        self.result_sub.resize(100, 25)

        self.result_mul.move(290, 60)
        self.result_mul.resize(100, 25)

        self.result_div.move(290, 85)
        self.result_div.resize(100, 25)

    def calculate(self):
        num1 = int(self.number_1.text())
        num2 = int(self.number_2.text())
        self.result_sum.display(num1 + num2)
        self.result_sub.display(num1 - num2)
        self.result_mul.display(num1 * num2)
        if num2 == 0:
            self.result_div.display("Error")
        else:
            self.result_div.display(round(num1 / num2, 3))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wt = MiniCalculator()
    wt.show()
    sys.exit(app.exec())