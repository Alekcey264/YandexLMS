import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from decimal import Decimal


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("1.ui", self)
        self.initUI()
        
    def initUI(self):
        self.text = ''
        self.temp_text = ''
        self.buttonGroup_digits.buttonClicked.connect(self.add_digit)
        self.buttonGroup_binary.buttonClicked.connect(self.add_binary)
        self.btn_eq.clicked.connect(self.calculate)
        self.btn_clear.clicked.connect(self.clr)
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_dot.clicked.connect(self.dot)
        self.btn_fact.clicked.connect(self.fact)

    def add_digit(self, object):
        self.text += object.text()
        self.temp_text += object.text()
        self.table.display(self.temp_text)

    def add_binary(self, object):
        self.operators = ['+', '-', '*', '/', '^', '**']
        if any(op in self.text for op in self.operators) and self.text[-1] not in self.operators:
            self.calculate()
        if self.text:
            if self.text[-1] in self.operators:
                self.text.replace(self.text[-1], object.text())
        if object.text() == '^':
            self.text += '**'
        else:
            self.text += object.text()
        self.temp_text = ''

    def calculate(self):
        if self.text:
            if self.text[0] in self.operators:
                self.text = '0' + self.text
            if '/' in self.text and int(self.text[self.text.rfind('/') + 1:]) == 0:
                self.table.display('Error')
                self.text = ''
                self.temp_text = ''
            else:
                self.text = str(eval(self.text))
                if int(float(self.text)) == float(self.text):
                    self.text = str(int(float(self.text)))
                if len(self.text) > 5 and int(self.text) < 10000:
                    self.text = self.text[:5]
                elif int(self.text) > 10000:
                    self.text = f"{Decimal(self.text):.0E}"
                self.table.display(self.text)
                self.temp_text = self.text

    def clr(self):
        self.table.display(0)
        self.text = ''
        self.temp_text = ''

    def sqrt(self):
        if self.text and eval(self.text) > 0:
            self.text += '**0.5'
            self.temp_text = ''
            self.calculate()
        else:
            self.table.display('Error')
            self.text = ''
            self.temp_text = ''

    def dot(self):
        if self.text:
            if self.text[-1] != '.':
                self.text += '.'
                self.temp_text += '.'
                self.table.display(self.temp_text)
    
    def fact(self):
        if self.text:
            temp_val = 1
            check = eval(self.text)
            if int(check) == float(check) and check > 0:
                for i in range(int(check), 1, -1):
                    temp_val *= i
            else:
                self.table.display('Error')
                self.text = ''
            self.temp_text = ''
            self.text = str(temp_val)
            self.calculate()
                

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
