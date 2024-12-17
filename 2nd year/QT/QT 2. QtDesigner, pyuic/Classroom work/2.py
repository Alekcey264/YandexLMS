import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>807</width>
    <height>600</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="minimumSize">
   <size>
    <width>0</width>
    <height>0</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>9</x>
      <y>149</y>
      <width>781</width>
      <height>141</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="0" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Цвет №1</string>
       </property>
      </widget>
     </item>
     <item row="2" column="0">
      <widget class="QRadioButton" name="radioButton_2">
       <property name="text">
        <string>Красный</string>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QRadioButton" name="radioButton_7">
       <property name="text">
        <string>Синий</string>
       </property>
       <property name="checked">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item row="3" column="0">
      <widget class="QRadioButton" name="radioButton_3">
       <property name="text">
        <string>Зелёный</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QRadioButton" name="radioButton">
       <property name="text">
        <string>Синий</string>
       </property>
       <property name="checked">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item row="3" column="1">
      <widget class="QRadioButton" name="radioButton_9">
       <property name="text">
        <string>Зелёный</string>
       </property>
      </widget>
     </item>
     <item row="2" column="1">
      <widget class="QRadioButton" name="radioButton_8">
       <property name="text">
        <string>Красный</string>
       </property>
       <property name="checked">
        <bool>false</bool>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Цвет №2</string>
       </property>
      </widget>
     </item>
     <item row="0" column="2">
      <widget class="QLabel" name="label_4">
       <property name="text">
        <string>Цвет №3</string>
       </property>
      </widget>
     </item>
     <item row="1" column="2">
      <widget class="QRadioButton" name="radioButton_10">
       <property name="text">
        <string>Синий</string>
       </property>
       <property name="checked">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item row="2" column="2">
      <widget class="QRadioButton" name="radioButton_11">
       <property name="text">
        <string>Красный</string>
       </property>
      </widget>
     </item>
     <item row="3" column="2">
      <widget class="QRadioButton" name="radioButton_12">
       <property name="text">
        <string>Зелёный</string>
       </property>
       <property name="checkable">
        <bool>true</bool>
       </property>
       <property name="checked">
        <bool>false</bool>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="make_flag">
    <property name="geometry">
     <rect>
      <x>690</x>
      <y>330</y>
      <width>101</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Сделать флаг</string>
    </property>
   </widget>
   <widget class="QLabel" name="result">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>380</y>
      <width>311</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(807, 600)
        self.color_group_1 = QButtonGroup(self)
        self.color_group_1.addButton(self.radioButton, id=1)
        self.color_group_1.addButton(self.radioButton_2, id=2)
        self.color_group_1.addButton(self.radioButton_3, id=3)
        self.color_group_2 = QButtonGroup(self)
        self.color_group_2.addButton(self.radioButton_7, id=1)
        self.color_group_2.addButton(self.radioButton_8, id=2)
        self.color_group_2.addButton(self.radioButton_9, id=3)
        self.color_group_3 = QButtonGroup(self)
        self.color_group_3.addButton(self.radioButton_10, id=1)
        self.color_group_3.addButton(self.radioButton_11, id=2)
        self.color_group_3.addButton(self.radioButton_12, id=3)
        self.groups = [self.color_group_1, self.color_group_2, self.color_group_3]
        for group in self.groups:
            group.buttons()[0].setChecked(True)
        self.make_flag.clicked.connect(self.change_text)

    def change_text(self):
        corr = list()
        for group in self.groups:
            for item in group.buttons():
                if item.isChecked():
                    corr.append(item.text())
        self.result.setText(f'Цвета: {corr[0]}, {corr[1]} и {corr[2]}')
        self.result.resize(self.result.sizeHint())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fm = FlagMaker()
    fm.show()
    sys.exit(app.exec())