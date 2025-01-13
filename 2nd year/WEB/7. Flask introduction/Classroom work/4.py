from flask import Flask, url_for, request

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


@app.route("/promotion_image")
def promotion_image():
    return f"""<!doctype html>
            <html lang="en>
                <head>
                    <meta chatset="utf-8">
                    <title>Привет, Марс!</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src={url_for('static', filename='img/mars.jpg')} alt="Mars picture">
                    <b>
                        <div class="alert alert-secondary" role="alert">Человечество вырастает из детства.</div>
                        <div class="alert alert-success"" role="alert">Человечеству мала одна планета.</div>
                        <div class="alert alert-light" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                        <div class="alert alert-warning" role="alert">И начнем с Марса!</div>
                        <div class="alert alert-danger" role="alert">Присоединяйся!</div>
                    </b>
                </body> 
            </html>"""


@app.route("/form_for_candidates", methods=["POST", "GET"])
def form_for_candidates():
    if request.method == "GET":
        return f'''<!doctype html>
                        <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                            </head>
                            <body>
                                <h1>Анкета претендента</h1>
                                <h2>на участие в миссии</h2>
                                <div>
                                hey 
                                    <form class="login_form" method="post>
                                        <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    </form>
                                </div>
                            </body>
                        </html>'''


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
