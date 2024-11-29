import io
import sys
import sqlite3

from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidgetItem
from PyQt6 import uic


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>790</width>
    <height>543</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>771</width>
      <height>31</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="layout_for_buttons"/>
   </widget>
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>771</width>
      <height>461</height>
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


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        russian_abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.buttons = [QPushButton(letter) for letter in russian_abc]
        [self.layout_for_buttons.addWidget(item) for item in self.buttons]
        [item.clicked.connect(self.show_values) for item in self.buttons]
        self.con = sqlite3.connect('films_db.sqlite')
        self.cur = self.con.cursor()
        self.tableWidget.setColumnCount(5)

    def show_values(self):
        self.tableWidget.clear()
        result = self.cur.execute(f'''SELECT films.id, films.title, films.year, genres.title, films.duration 
                                  FROM films INNER JOIN genres ON films.genre = genres.id 
                                  WHERE films.title LIKE "{self.sender().text()}%"''').fetchall()
        if result:
            self.statusBar().showMessage(f"Нашлось {len(result)} записей")
            self.tableWidget.setRowCount(len(result))
            for i in range(len(result)):
                for j in range(len(result[i])):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        else:
            self.statusBar().showMessage("К сожалению, ничего не нашлось")

    def closeEvent(self):
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MyWidget()
    mw.show()
    sys.exit(app.exec())