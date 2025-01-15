from flask import Flask

app = Flask(__name__)


@app.route("/choice/<planet_name>")
def planet_choice(planet_name):
    planets = {
        "Меркурий": ["Информация о Меркурие 1", "Информация о Меркурие 2", "Информация о Меркурие 3", "Информация о Меркурие 4", "Информация о Меркурие 5"],
        "Венера": ["Информация о Венере 1", "Информация о Венере 2", "Информация о Венере 3", "Информация о Венере 4", "Информация о Венере 5"],
        "Марс": ["Информация о Марсе 1", "Информация о Марсе 2", "Информация о Марсе 3", "Информация о Марсе 4", "Информация о Марсе 5"],
        "Земля": ["Информация о Земле 1", "Информация о Земле 2", "Информация о Земле 3", "Информация о Земле 4", "Информация о Земле 5"],
        "Юпитер": ["Информация о Юпитере 1", "Информация о Юпитере 2", "Информация о Юпитере 3", "Информация о Юпитере 4", "Информация о Юпитере 5"],
        "Сатурн": ["Информация о Сатурне 1", "Информация о Сатурне 2", "Информация о Сатурне 3", "Информация о Сатурне 4", "Информация о Сатурне 5"],
        "Уран": ["Информация об Уране 1", "Информация об Уране 2", "Информация об Уране 3", "Информация об Уране 4", "Информация об Уране 5"],
        "Нептун": ["Информация о Нептуне 1", "Информация о Нептуне 2", "Информация о Нептуне 3", "Информация о Нептуне 4", "Информация о Нептуне 5"]
    }
    description = planets.get(planet_name)
    headers = ["text-center text-primary", "text-center text-info", "text-center mt-4", "text-center mt-3", "text-center mt-2"]
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
                            <h1>Мое предложение: {planet}</h1>
                            <div class="container mt-5">
                                {answer}
                            </div>
                        </body> 
                    </html>"""
            ).format(
                planet=planet_name,
                answer=(
                    '<br>'.join(
                        [
                            f'<h{i + 1} class="{headers[i]}">{description[i]}</h{i + 1}>'
                            for i in range(len(description))
                        ]
                    ) 
                    if description 
                    else 'Такой планеты еще не открыли!'
                )
            )


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")