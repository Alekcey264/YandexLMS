from flask import Flask

app = Flask(__name__)


@app.route("/")
def slash():
    return "<b>Миссия Колонизация Марса</b>"


@app.route("/index")
def index():
    return "<b>И на Марсе будут яблони цвести!</b>"


@app.route("/promotion")
def promotion():
    return '''<b>
            <div>Человечество вырастает из детства.</div>
            <div>Человечеству мала одна планета.</div>
            <div>Мы сделаем обитаемыми безжизненные пока планеты.</div>
            <div>И начнем с Марса!</div>
            <div>Присоединяйся!</div>
            </b>'''


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
