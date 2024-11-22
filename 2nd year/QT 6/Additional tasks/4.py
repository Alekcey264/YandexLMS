import csv
import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt6.QtGui import QBrush, QColor


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>719</width>
    <height>392</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>171</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Строка для поиска</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="searchEdit">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>10</y>
      <width>561</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QTableWidget" name="resultTable">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>701</width>
      <height>341</height>
     </rect>
    </property>
    <property name="columnCount">
     <number>7</number>
    </property>
    <column/>
    <column/>
    <column/>
    <column/>
    <column/>
    <column/>
    <column/>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class TitanicSearch(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        with open('titanik.csv', 'r', encoding='utf-8') as csv_file:
            self.reader = list(csv.reader(csv_file, delimiter=',', quotechar='"'))
        title = self.reader[0]
        self.reader = self.reader[1:]
        self.resultTable.setHorizontalHeaderLabels(title)
        self.resultTable.setRowCount(len(self.reader))
        self.searchEdit.textChanged.connect(self.search)
        for i, row in enumerate(self.reader):
            if self.reader[i][5] == '1':
                color = QBrush(QColor(0, 255, 0))
            else:
                color = QBrush(QColor(255, 0, 0))
            for j, value in enumerate(row):
                self.resultTable.setItem(i, j, QTableWidgetItem(value))
                self.resultTable.item(i, j).setBackground(color)
                
    def search(self):
        if len(self.searchEdit.text()) > 3:
            print('searching')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ts = TitanicSearch()
    ts.show()
    sys.exit(app.exec())