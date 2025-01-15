from flask import Flask

app = Flask(__name__)


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def result(nickname, level, rating):
    return (
            """<!doctype html>
            <html lang="en>
                <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                </head>
                <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участи в миссии {name}:</h2>
                    <h3 class="alert alert-success">Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
                    <h3 class="alert alert-primary">составляет {rating}</h3>
                    <h3 class="alert alert-warning">Желаем удачи!</h3>
                </body> 
            </html>"""
    ).format(
        name=nickname,
        level=level,
        rating=rating
    )


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")