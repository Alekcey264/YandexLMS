import sys
import io
import sqlite3

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>667</width>
    <height>293</height>
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
      <y>10</y>
      <width>191</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="queryLine">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>10</y>
      <width>321</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="queryButton">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>10</y>
      <width>121</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Поиск</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>60</y>
      <width>121</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>ID:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>100</y>
      <width>121</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Название:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>121</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Год выпуска:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>180</y>
      <width>121</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Жанр:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>220</y>
      <width>121</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Продолжительность:</string>
    </property>
   </widget>
   <widget class="QLabel" name="errorLabel">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>250</y>
      <width>111</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLineEdit" name="idEdit">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>60</y>
      <width>451</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="titleEdit">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>100</y>
      <width>451</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="yearEdit">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>140</y>
      <width>451</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="genreEdit">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>180</y>
      <width>451</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="durationEdit">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>220</y>
      <width>451</width>
      <height>20</height>
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
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.value_to_find = 'year'
        self.parameterSelection.addItems(['Год выпуска', 'Название', 'Продолжительность'])
        self.parameterSelection.currentTextChanged.connect(self.change_value_to_find)
        self.queryButton.clicked.connect(self.set_values)

    def change_value_to_find(self):
        current_text = self.parameterSelection.currentText()
        if current_text == 'Год выпуска':
            self.value_to_find = 'year'
        elif current_text == 'Название':
            self.value_to_find = 'title'
        else:
            self.value_to_find = 'duration'

    def set_values(self):
        self.errorLabel.setText('')
        result = self.make_request()
        if result == 'error':
            self.errorLabel.setText('Неправильный запрос')
            result = ('', '', '', '', '')
        elif result[0] == '':
            self.errorLabel.setText('Ничего не найдено')
        self.idEdit.setText(str(result[0]))
        self.titleEdit.setText(str(result[1]))
        self.yearEdit.setText(str(result[2]))
        self.genreEdit.setText(str(result[3]))
        self.durationEdit.setText(str(result[4]))

    def make_request(self):
        try:
            con = sqlite3.connect('films_db.sqlite')
            cur = con.cursor()
            result = cur.execute(f'''SELECT id, title, year, genre, duration FROM films WHERE 
                                 {self.value_to_find} = ? ORDER BY id''', (self.queryLine.text(),)).fetchone()
            if not self.queryLine.text():
                raise Exception
        except Exception:
            return 'error'
        finally:
            con.close()
        if not result:
            result = ('', '', '', '', '')
        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MyWidget()
    mw.show()
    sys.exit(app.exec())