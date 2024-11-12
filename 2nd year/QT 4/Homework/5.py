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
    <width>498</width>
    <height>260</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPlainTextEdit" name="text_edit">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>10</y>
      <width>331</width>
      <height>241</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="filename_edit">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>141</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="new_button">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>141</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Создать новый</string>
    </property>
   </widget>
   <widget class="QPushButton" name="save_button">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>70</y>
      <width>141</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Сохранить новый</string>
    </property>
   </widget>
   <widget class="QPushButton" name="open_button">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>100</y>
      <width>141</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Открыть файл</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Notebook(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.new_button.clicked.connect(self.new)
        self.save_button.clicked.connect(self.save)
        self.open_button.clicked.connect(self.open)
    
    def new(self):
        self.filename_edit.clear()
        self.text_edit.clear()

    def save(self):
        if self.filename_edit.text():
            with open(self.filename_edit.text(), 'w', encoding='utf-8') as f:
                f.write(self.text_edit.toPlainText())

    def open(self):
        try:
            with open(self.filename_edit.text(), 'r', encoding='utf-8') as f:
                self.text_edit.setPlainText(f.read())
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    nb = Notebook()
    nb.show()
    sys.exit(app.exec())