from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'example_secret_key'


def main():
    app.run(host='localhost', port=8080)


if __name__ == '__main__':
    main()