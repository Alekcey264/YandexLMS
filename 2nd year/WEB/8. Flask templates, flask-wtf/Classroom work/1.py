from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def login():
    return render_template('base.html', title='Заготовка')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)