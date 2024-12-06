import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>290</width>
    <height>246</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>121</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Загрузить строки</string>
    </property>
   </widget>
   <widget class="QTextBrowser" name="text_field">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>271</width>
      <height>192</height>
     </rect>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Suffle(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.button.clicked.connect(self.set_strings)

    def set_strings(self):
        with open('Homework/lines.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        text = ''.join([lines[i] for i in range(1, len(lines), 2)])
        text += ''.join([lines[i] for i in range(0, len(lines), 2)])
        self.text_field.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    suffle = Suffle()
    suffle.show()
    sys.exit(app.exec())