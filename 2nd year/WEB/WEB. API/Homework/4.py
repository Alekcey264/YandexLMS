import requests
import sys
import os
import io

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
from conf import MAP_API_KEY

WINDOW_SIZE = [600, 450]
template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>621</width>
    <height>400</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLabel" name="link">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>370</y>
     <width>631</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>TextLabel</string>
   </property>
   <property name="openExternalLinks">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QLabel" name="image">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>641</width>
     <height>351</height>
    </rect>
   </property>
   <property name="text">
    <string>TextLabel</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class SlideShow(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.getImage()
        self.setImage()

    def getImage(self):
        self.cur_index = 1
        self.images = {1: ["37.617698,55.755864"], 2: ["30.314997,59.938784"], 3: ["-74.002863,40.714627"]}
        for key, value in self.images.items():
            url = f"https://static-maps.yandex.ru/v1?ll={value[0]}&z=11&l=map&apikey={MAP_API_KEY}"
            response = requests.get(url)
            if not response:
                print(response.status_code, response.reason)
                sys.exit(1)
            map_image = f"map{key}.png"
            with open(map_image, "wb") as file:
                file.write(response.content)
            self.images[key].extend([map_image, url])

    def setImage(self):
        self.pixmap = QPixmap(self.images[self.cur_index][1])
        self.image.setPixmap(self.pixmap)
        self.link.setText(f"<a href={self.images[self.cur_index][2]}>Информация<a>")

    def keyPressEvent(self, event):
        if self.cur_index == len(self.images):
            self.cur_index = 1
        else:
            self.cur_index += 1
        self.setImage()
        

    def closeEvent(self, event):
        for value in self.images.values():
            os.remove(value[1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ss = SlideShow()
    ss.show()
    sys.exit(app.exec())
