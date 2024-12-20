import csv
import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>472</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>781</width>
      <height>421</height>
     </rect>
    </property>
    <property name="sortingEnabled">
     <bool>true</bool>
    </property>
    <property name="columnCount">
     <number>3</number>
    </property>
    <attribute name="horizontalHeaderCascadingSectionResizes">
     <bool>false</bool>
    </attribute>
    <attribute name="horizontalHeaderDefaultSectionSize">
     <number>254</number>
    </attribute>
    <attribute name="horizontalHeaderStretchLastSection">
     <bool>false</bool>
    </attribute>
    <attribute name="verticalHeaderVisible">
     <bool>true</bool>
    </attribute>
    <attribute name="verticalHeaderCascadingSectionResizes">
     <bool>false</bool>
    </attribute>
    <attribute name="verticalHeaderShowSortIndicator" stdset="0">
     <bool>false</bool>
    </attribute>
    <attribute name="verticalHeaderStretchLastSection">
     <bool>false</bool>
    </attribute>
    <column/>
    <column/>
    <column/>
   </widget>
   <widget class="QLineEdit" name="total">
    <property name="geometry">
     <rect>
      <x>472</x>
      <y>440</y>
      <width>321</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>430</x>
      <y>440</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Итого:</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class InteractiveReceipt(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.tableWidget.setHorizontalHeaderLabels(['Название', 'Цена', 'Количество'])
        with open('price.csv', 'r', encoding='utf-8') as f:
            self.reader = list(csv.reader(f, delimiter=';'))[1:]
            self.tableWidget.setRowCount(len(self.reader))
            for i, row in enumerate(self.reader):
                for j, column in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(column))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(0)))
            self.tableWidget.cellChanged.connect(self.calculate)

    def calculate(self, row, column):
        money = 0
        for i in range(len(self.reader)):
            count = self.tableWidget.item(i, 2)
            if count:
                money += (int(self.tableWidget.item(i, 1).text()) * int(count.text()))
        self.total.setText(str(money))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ir = InteractiveReceipt()
    ir.show()
    sys.exit(app.exec())