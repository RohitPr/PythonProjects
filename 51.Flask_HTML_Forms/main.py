from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["POST"])
def login():
    username = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    print(username, email, message)
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
