import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>668</width>
    <height>468</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>641</width>
      <height>431</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="widgetArt" rowminimumheight="0" columnminimumwidth="0"/>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class WidgetArt(QMainWindow):
    def __init__(self, matrix):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.matrix = matrix
        self.initUI()

    def initUI(self):
        symb = {1: '*', 0: ''}
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.widgetArt.addWidget(QPushButton(symb[self.matrix[i][j]], self), i, j)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    matrix = [
        [1, 0],
        [0, 1]
    ]
    wa = WidgetArt(matrix)
    wa.show()
    sys.exit(app.exec())