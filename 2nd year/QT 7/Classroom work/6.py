import sqlite3
import sys
import io

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6 import uic


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>584</width>
    <height>424</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QComboBox" name="parameterSelection">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>181</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="queryButton">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>60</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Пуск</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>20</y>
      <width>361</width>
      <height>391</height>
     </rect>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.load