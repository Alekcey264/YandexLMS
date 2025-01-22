from flask import Flask, render_template

app = Flask(__name__)


@app.route("/list_prof/<list>")
def list_prof(list):
    profs = ["инженер-исследователь",
        "пилот",
        "строитель",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите",
        "астрогеолог",
        "гляциолог",
        "инженер жизнеобеспечения",
        "метеоролог",
        "оператор марсохода",
        "киберинженер",
        "штурман",
        "пилот дронов"
        ]
    return render_template("3.html", list=list, profs=profs)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)