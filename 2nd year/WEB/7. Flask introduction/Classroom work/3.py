from flask import Flask, url_for

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


@app.route("/image_mars")
def image_mars():
    return f"""<!doctype html>
                <html lang="en>
                    <head>
                        <meta chatset="utf-8">
                        <title>Привет, Марс!</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src={url_for('static', filename='img/mars.jpg')} alt="Mars picture">
                        <p>Вот она какая, красная планета.</p>
                    </body> 
                </html>"""


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
