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
    <width>722</width>
    <height>453</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QCalendarWidget" name="calendarWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>371</width>
      <height>341</height>
     </rect>
    </property>
   </widget>
   <widget class="QListWidget" name="eventList">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>10</y>
      <width>321</width>
      <height>421</height>
     </rect>
    </property>
   </widget>
   <widget class="QTimeEdit" name="timeEdit">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>371</width>
      <height>22</height>
     </rect>
    </property>
    <property name="dateTime">
     <datetime>
      <hour>0</hour>
      <minute>0</minute>
      <second>0</second>
      <year>2000</year>
      <month>1</month>
      <day>1</day>
     </datetime>
    </property>
    <property name="currentSection">
     <enum>QDateTimeEdit::HourSection</enum>
    </property>
    <property name="calendarPopup">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>390</y>
      <width>371</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="addEventBtn">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>410</y>
      <width>371</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить событие</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.temp = list()
        self.addEventBtn.clicked.connect(self.update)

    def update(self):
        if self.lineEdit.text():
            date = self.calendarWidget.selectedDate().toPyDate().isoformat()
            time = self.timeEdit.time().toPyTime().isoformat()
            text = self.lineEdit.text()
            self.temp.append((date, time, text))
            self.temp.sort(key=lambda x: x[0])
            self.eventList.clear()
            for item in self.temp:
                self.eventList.addItem(f"{item[0]} {item[1]} - {item[2]}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sp = SimplePlanner()
    sp.show()
    sys.exit(app.exec())

