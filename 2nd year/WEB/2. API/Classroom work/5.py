import os
import sys
import requests

from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QPixmap
from conf import MAP_API_KEY

WINDOW_SIZE = [600, 450]

class Australia(QWidget):
    def __init__(self):
        super().__init__()
        self.getImage()
        self.initUI()

    def initUI(self):
        self.setGeometry(350, 350, *WINDOW_SIZE)
        self.pixmap = QPixmap(self.map_image)
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, *WINDOW_SIZE)
        self.image.setPixmap(self.pixmap)

    def getImage(self):
        map_request = f"https://static-maps.yandex.ru/v1?ll=137.727707,-29.394543&z=4&l=map&apikey={MAP_API_KEY}"
        response = requests.get(map_request)
        if not response:
            print(response.status_code, response.reason)
            sys.exit()
        self.map_image = "map.png"
        with open(self.map_image, "wb") as file:
            file.write(response.content)

    def closeEvent(self, event):
        os.remove(self.map_image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    au = Australia()
    au.show()
    sys.exit(app.exec())
