from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/table/<sex>/<age>')
def table(sex, age):
    return render_template('2.html', sex=sex, age=int(age))


if __name__ == "__main__":
    app.run(host='localhost', port=8080)