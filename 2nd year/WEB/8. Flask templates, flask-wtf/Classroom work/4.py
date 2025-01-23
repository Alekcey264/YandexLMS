from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    values = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "среднее",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Бум бац бэцлес",
        "ready": "False"
    }
    return render_template('4.html', **values)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)