from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def swapper_function():
        return "<b>" + function() + "</b>"

    return swapper_function


def make_italic(function):
    def swapper_function():
        return "<em>" + function() + "</em>"

    return swapper_function


@app.route('/')
@make_italic
@make_bold
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=True)
