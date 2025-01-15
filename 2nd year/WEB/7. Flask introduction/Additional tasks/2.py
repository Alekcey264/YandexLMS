from flask import Flask, url_for

app = Flask(__name__)


@app.route("/carousel")
def carousel():
    return f"""<!doctype html>
            <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                    <title>Пейзажи Марса</title>
                </head>
                <body>
                    <h1 class="text-center">Пейзажи Марса</h1>
                    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                        <div class="carousel-indicators">
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                        </div>
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <img src="{url_for('static', filename='img/1.jpg')}" class="d-block w-100" alt="hey">
                            </div>
                            <div class="carousel-item">
                                <img src="{url_for('static', filename='img/2.jpg')}" class="d-block w-100" alt="hey">
                            </div>
                            <div class="carousel-item">
                                <img src="{url_for('static', filename='img/3.jpg')}" class="d-block w-100" alt="hey">
                            </div>
                        </div>
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" 
                    integrity="sha384-pzjw8f+ua7Kw1TIqkvQ8fXzIBsVGAHmxMRBA+jT3Glh94A1ANUUhAU8tWtEd7fG8" 
                    crossorigin="anonymous"></script>
                </body> 
            </html>"""



if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")