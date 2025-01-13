from flask import Flask


app = Flask(__name__)


@app.route("/")
def slash():
    return "<b>Миссия Колонизация Марса</b>"

@app.route("/index")
def index():
    return "<b>И на Марсе будут яблони цвести!</b>"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")