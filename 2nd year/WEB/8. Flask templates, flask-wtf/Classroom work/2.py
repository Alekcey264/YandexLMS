from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/training/<prof>')
def training(prof):
    return render_template("2.html", title=prof.capitalize(), prof=prof, image="img/1.jpg")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)