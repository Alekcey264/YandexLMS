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
                        <meta charset="utf-8">
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
                    <meta charset="utf-8">
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
                                    <form class="bid_form" method="post" enctype="multipart/form-data">
                                        <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname" required="true">
                                        <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name" required="true">
                                        <br>
                                        <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email" required="true">
                                        <br>
                                        <div class="form-group">
                                            <label for="edSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="edSelect" name="education" required="true">
                                                <option value="">-</option>
                                                <option value="base">Начальное</option>
                                                <option value="middle">Среднее</option>
                                                <option value="middle_prof">Среднее профиссиональное</option>
                                                <option value="high_unf">Высшее неоконченное</option>
                                                <option value="high_not_full">Высшее неполное</option>
                                                <option value="high">Высшее</option>
                                            </select>
                                        </div>
                                        <br>
                                        <label for="jobs">Какие у Вас есть профессии?</label>
                                        <div class="form-group form-check" id="jobs" name="jobs">
                                            <div>
                                                <input type="checkbox" class="form-check-input" id="ing-res" name="ing-res">
                                                <label class="form-check-label" for="ing-res">Инженер-исследователь</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" class="form-check-input" id="ing-bui" name="ing-bui">
                                                <label class="form-check-label" for="ing-bui">Инженер-строитель</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" class="form-check-input" id="pilot" name="pilot">
                                                <label class="form-check-label" for="pilot">Пилот</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" class="form-check-input" id="meteo" name="meteo">
                                                <label class="form-check-label" for="meteo">Метеоролог</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" class="form-check-input" id="healthcare" name="healthcare">
                                                <label class="form-check-label" for="healthcare">Инженер по жизнеобеспечению</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" class="form-check-input" id="radiation" name="radiation">
                                                <label class="form-check-label" for="radiation">Инженер по радиационной защите</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" class="form-check-input" id="doctor" name="doctor">
                                                <label class="form-check-label" for="doctor">Врач</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" class="form-check-input" id="exobio" name="exobio">
                                                <label class="form-check-label" for="exobio">Экзобиолог</label>
                                            </div>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="sex" id="male" value="male checked">
                                                <label class="form-check-label" for="male">Мужской</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="sex" id="female" value="female checked">
                                                <label class="form-check-label" for="female">Женский</label>
                                            </div>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="why">Почему вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows=3" name="why"></textarea>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="photo" required="true">
                                        </div>
                                        <br>
                                        <div class="form-group file-check">
                                            <input type="checkbox" class="form-check-input" id="agree" name="agree">
                                            <label class="form-check-label" for="agree">Готовы остаться на Марсе?</label>
                                        </div>
                                        <br>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                            </body>
                        </html>'''
    elif request.method == "POST":
        return "Заявка отправлена"

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
