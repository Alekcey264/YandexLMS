import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLineEdit


class WidgetsHideNSeek(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 150)

        self.checkbox1 = QCheckBox("edit1", self)
        self.checkbox1.move(10, 10)
        self.checkbox2 = QCheckBox("edit2", self)
        self.checkbox2.move(10, 40)
        self.checkbox3 = QCheckBox("edit3", self)
        self.checkbox3.move(10, 70)
        self.checkbox4 = QCheckBox("edit4", self)
        self.checkbox4.move(10, 100)
        self.boxes = [self.checkbox1, self.checkbox2, self.checkbox3, self.checkbox4]
        [item.setChecked(True) for item in self.boxes]
        [item.clicked.connect(self.check) for item in self.boxes]

        self.edit1 = QLineEdit("Поле edit1", self)
        self.edit1.move(70, 10)
        self.edit2 = QLineEdit("Поле edit2", self)
        self.edit2.move(70, 40)
        self.edit3 = QLineEdit("Поле edit3", self)
        self.edit3.move(70, 70)
        self.edit4 = QLineEdit("Поле edit4", self)
        self.edit4.move(70, 100)
        self.lines = [self.edit1, self.edit2, self.edit3, self.edit4]

    def check(self):
        if not self.sender().isChecked():
            self.hide(self.boxes.index(self.sender()))
        else:
            self.show_box(self.boxes.index(self.sender()))

    def show_box(self, index):
        self.lines[index].show()

    def hide(self, index):
        self.lines[index].hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wt = WidgetsHideNSeek()
    wt.show()
    sys.exit(app.exec())