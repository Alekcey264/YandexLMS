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
        self.resultButton.clicked.connect(self.show_results)
        self.classes.currentTextChanged.connect(self.class_changed)
        self.school.currentTextChanged.connect(self.school_changed)
        self.parse_csv()
        self.schools.addItems(self.schools_list)
        self.classes.addItems(self.classes_list)

    def show_results(self):
        self.ch_s = self.schools.currentText()
        self.ch_c = self.classes.currentText()
        if self.ch_s == "Все":
            self.ch_s = ""
        if self.ch_c == "Все":
            self.ch_c = ""
        print(list(filter(lambda x: self.ch_s in x[1], filter(lambda y: self.ch_c in y[2], self.reader))))
        
    def parse_csv(self):
        with open('rez.csv', 'r', encoding='utf-8') as f:
            self.reader = list(csv.reader(f, delimiter=',', quotechar='"'))[1:]
        self.reader = [[i[1].split()[-2], i[2].split('-')[2], i[2].split('-')[3], i[-1]] for i in self.reader]
        self.schools_list = sorted(list(set(item[1] for item in self.reader)), key=lambda x: int(x))
        self.classes_list = sorted(list(set(item[2] for item in self.reader)), key=lambda x: int(x))

    def class_changed(self):
        self.schools.clear()
        self.schools.addItems([item[1] for item in filter(lambda x: self.classes.currentText() in x[2], self.reader)])
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    olr = OlympResult()
    olr.show()
    sys.exit(app.exec())