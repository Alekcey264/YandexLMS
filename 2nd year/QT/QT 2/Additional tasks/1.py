import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>777</width>
    <height>583</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>141</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Порог срабатывания (%)</string>
    </property>
   </widget>
   <widget class="QDoubleSpinBox" name="alert_value">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>10</y>
      <width>591</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>751</width>
      <height>491</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="0" column="0">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Текст 1</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Текст 2</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QPlainTextEdit" name="text1"/>
     </item>
     <item row="1" column="1">
      <widget class="QPlainTextEdit" name="text2"/>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="checkBtn">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>540</y>
      <width>751</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Сравнить</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.checkBtn.clicked.connect(self.check_plagiarism)

    def check_plagiarism(self):
        check_value = self.alert_value.value()
        text1 = self.text1.toPlainText().split('\n')
        text2 = self.text2.toPlainText().split('\n')
        if text1[-1] == '' and len(text1) > 1:
            text1.pop()
        text1 = set(text1)
        if text2[-1] == '' and len(text2) > 1:
            text2.pop()
        text2 = set(text2)
        diff = str(round(len(text1 & text2) / len(text1 | text2) * 100, 2))
        if diff[-1] == '0':
            diff = diff + '0'
        if float(diff) >= check_value:
            self.statusBar().showMessage(f'Тексты похожи на {diff}%, плагиат')
        else:
            self.statusBar().showMessage(f'Тексты похожи на {diff}%, не плагиат')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ap = AntiPlagiarism()
    ap.show()
    sys.exit(app.exec())