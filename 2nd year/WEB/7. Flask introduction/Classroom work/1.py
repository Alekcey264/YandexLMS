from flask import Flask, url_for


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "Hello, Yandex!"

@app.route("/countdown")
def countdown():
    ls = [str(x) for x in range(10, 0, -1)]
    ls.append("Go!")
    return "</br>".join(ls)

@app.route("/image_sample")
def image():
    return f'''<img src="{url_for('static', filename='img/riana.jpeg')}"
            alt="No picture">'''

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")