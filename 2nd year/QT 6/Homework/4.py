import csv
import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QComboBox" name="schools">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>301</width>
      <height>22</height>
     </rect>
    </property>
    <item>
     <property name="text">
      <string>Все</string>
     </property>
    </item>
   </widget>
   <widget class="QComboBox" name="classes">
    <property name="geometry">
     <rect>
      <x>330</x>
      <y>10</y>
      <width>301</width>
      <height>22</height>
     </rect>
    </property>
    <item>
     <property name="text">
      <string>Все</string>
     </property>
    </item>
   </widget>
   <widget class="QPushButton" name="resultButton">
    <property name="geometry">
     <rect>
      <x>660</x>
      <y>10</y>
      <width>131</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Узнать результаты</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>781</width>
      <height>551</height>
     </rect>
    </property>
    <property name="columnCount">
     <number>2</number>
    </property>
    <column/>
    <column/>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class OlympResult(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        with open('rez.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
        # list(filter(lambda x: ..., filter(lambda y: ..., reader)))
        print(self.classes.currentText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    olr = OlympResult()
    olr.show()
    sys.exit(app.exec())