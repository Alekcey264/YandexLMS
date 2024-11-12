import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>340</width>
    <height>154</height>
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
      <width>61</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Имя файла</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="filenameEdit">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>10</y>
      <width>171</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>10</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Рассчитать</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>151</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Максимальное значение</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="minEdit">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>50</y>
      <width>161</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="maxEdit">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>80</y>
      <width>161</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>151</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Минимальное значение</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>151</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Среднее значение</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="avgEdit">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>110</y>
      <width>161</width>
      <height>20</height>
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


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.button.clicked.connect(self.get_info)

    def get_info(self):
        try:
            with open(self.filenameEdit.text(), 'r', encoding='utf-8') as f:
                self.lines = f.read()
                self.check_lines()
        except FileNotFoundError:
            self.file_error()
            self.statusBar().showMessage("Указанный файл не существует")
    
    def check_lines(self):
        if self.lines:
            self.lines = self.lines.replace('\\t', '').replace('  ', ' ').replace('\\n', '')
            self.lines = self.lines.strip().split()
            true_line = list()
            for item in self.lines:
                if item.replace('-', '', 1).isnumeric():
                    true_line.append(int(item))
                else:
                    self.statusBar().showMessage("Файл содержит некорректные данные")
                    self.file_error()
                    break
            else:
                self.lines = true_line
                self.calculate()
        else:
            self.statusBar().showMessage("Указанный файл пуст")
            self.file_error()

    def calculate(self):
        mi_v, ma_v = str(min(self.lines)), str(max(self.lines)) 
        av_v = '{:.2f}'.format(sum(self.lines) / len(self.lines))
        self.minEdit.setText(mi_v)
        self.maxEdit.setText(ma_v)
        self.avgEdit.setText(av_v)
        with open('out.txt', 'w', encoding='utf-8') as f:
            f.write(f'Максимальное значение = {mi_v}\nМинимальное значение = {ma_v}\nСреднее значение = {av_v}')

    def file_error(self):
        self.minEdit.setText('')
        self.maxEdit.setText('')
        self.avgEdit.setText('')


# Classroom work/hey.txt
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fs = FileStat()
    fs.show()
    sys.exit(app.exec())