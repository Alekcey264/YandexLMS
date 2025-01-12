import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
from random import choice


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>445</width>
    <height>43</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTextEdit" name="text_field">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>10</y>
      <width>311</width>
      <height>21</height>
     </rect>
    </property>
    <property name="sizePolicy">
     <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
      <horstretch>0</horstretch>
      <verstretch>0</verstretch>
     </sizepolicy>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Sunken</enum>
    </property>
    <property name="verticalScrollBarPolicy">
     <enum>Qt::ScrollBarAlwaysOff</enum>
    </property>
    <property name="horizontalScrollBarPolicy">
     <enum>Qt::ScrollBarAlwaysOff</enum>
    </property>
    <property name="lineWrapMode">
     <enum>QTextEdit::WidgetWidth</enum>
    </property>
   </widget>
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>91</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Получить</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.lines = None
        self.checked = False
        self.button.clicked.connect(self.random_text)

    def random_text(self):
        if not self.checked:
            with open('lines.txt', 'r', encoding='utf-8') as f:
                self.checked = True
                self.lines = f.readlines()
        if self.lines:   
            self.text_field.setText(choice(self.lines).strip())        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    rs = RandomString()
    rs.show()
    sys.exit(app.exec())