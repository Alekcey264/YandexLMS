import os
import sys
import requests

from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QPixmap
from conf import MAP_API_KEY

WINDOW_SIZE = [600, 450]

class Gulf(QWidget):
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
        points = [
            "29.906755,59.881217",
            "29.916154,59.894672",
            "29.967004,59.887317",
            "30.031896,59.866567",
            "30.137515,59.866796",
            "30.168377,59.888287",
            "30.216386,59.905630",
            "30.230331,59.916652",
            "30.262794,59.917455",
            "30.269878,59.925489",
            "30.277651,59.932029",
            "30.311760,59.941528"
        ]
        map_request = f"https://static-maps.yandex.ru/v1?apikey={MAP_API_KEY}&ll=30.078307,59.927407&z=10&pl=c:000000ff,w:2,{",".join(points)}"
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
    gulf = Gulf()
    gulf.show()
    sys.exit(app.exec())
