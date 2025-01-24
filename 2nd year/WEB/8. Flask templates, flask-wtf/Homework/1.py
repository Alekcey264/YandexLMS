from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    passengers = [
        'Ridley',
        'Andy',
        'Mark',
        'Venkata',
        'Teddy',
        'Shaun'
    ]
    return render_template('1.html', title='Пассажиры', passengers=passengers)


if __name__ == "__main__":
    app.run(host='localhost', port=8080)