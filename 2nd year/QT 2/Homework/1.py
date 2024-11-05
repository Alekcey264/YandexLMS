import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>456</width>
    <height>378</height>
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
      <y>20</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Имя</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>51</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Телефон</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="contactName">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>20</y>
      <width>251</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="contactNumber">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>50</y>
      <width>251</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="addContactBtn">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>30</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QListWidget" name="contactList">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>431</width>
      <height>271</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.addContactBtn.clicked.connect(self.add_value)

    def add_value(self):
        if self.contactName.text() and self.contactNumber.text():
            self.contactList.addItem(self.contactName.text() + ' ' + self.contactNumber.text())
            self.contactName.setText('')
            self.contactNumber.setText('')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mn = MyNotes()
    mn.show()
    sys.exit(app.exec())