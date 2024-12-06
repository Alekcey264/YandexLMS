import sys
import io

from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6 import uic


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>543</width>
    <height>373</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="PlotWidget" name="graphicsView">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>521</width>
     <height>311</height>
    </rect>
   </property>
  </widget>
  <widget class="QLineEdit" name="function_line">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>330</y>
     <width>251</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>270</x>
     <y>330</y>
     <width>60</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>От</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="x_first">
   <property name="geometry">
    <rect>
     <x>290</x>
     <y>330</y>
     <width>31</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QLineEdit" name="lineEdit_3">
   <property name="geometry">
    <rect>
     <x>350</x>
     <y>330</y>
     <width>31</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="x_last">
   <property name="geometry">
    <rect>
     <x>330</x>
     <y>330</y>
     <width>60</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>до</string>
   </property>
  </widget>
  <widget class="QPushButton" name="make_plot">
   <property name="geometry">
    <rect>
     <x>420</x>
     <y>330</y>
     <width>113</width>
     <height>32</height>
    </rect>
   </property>
   <property name="text">
    <string>Построить</string>
   </property>
  </widget>
 </widget>
 <customwidgets>
  <customwidget>
   <class>PlotWidget</class>
   <extends>QGraphicsView</extends>
   <header>pyqtgraph</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
"""


class MakePlots(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.make_plot.clicked.connect(self.calculate_values)

    def calculate_values(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mp = MakePlots()
    mp.show()
    sys.exit(app.exec())
