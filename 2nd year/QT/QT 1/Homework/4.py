import sys
from PyQt6.QtWidgets import QWidget, QPlainTextEdit, QCheckBox, QApplication, QPushButton


class MacOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300, 300, 180, 300)
        self.menu_checkboxes = [QCheckBox('Чизбургер', self), QCheckBox('Гамбургер', self), 
                                QCheckBox('Кока-кола', self), QCheckBox('Наггетсы', self)]
        [item.setChecked(False) for item in self.menu_checkboxes]
        self.x_def = 10
        self.y_def = 10
        for item in self.menu_checkboxes:
            item.move(self.x_def, self.y_def)
            self.y_def += 40
        self.order_btn = QPushButton('Заказать', self)
        self.order_btn.move(self.x_def, self.y_def)
        self.order_btn.clicked.connect(self.change_check)
        self.y_def += 40
        self.result = QPlainTextEdit('Ваш заказ:\n\n', self)
        self.result.move(self.x_def, self.y_def)
        self.result.resize(160, 100)

    def change_check(self):
        self.temp_text = '\n'.join([item.text() for item in self.menu_checkboxes if item.isChecked()])
        self.temp_text = 'Ваш заказ:\n\n' + self.temp_text
        self.result.setPlainText(self.temp_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mo = MacOrder()
    mo.show()
    sys.exit(app.exec())
