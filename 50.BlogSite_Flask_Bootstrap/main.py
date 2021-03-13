from flask import Flask, render_template
import requests

# Custom API Created using npoint and saved it in JSON format
API_URL = "https://api.npoint.io/2722c84e8ff4b2ddbd15"

posts = requests.get(API_URL).json()

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', posts=posts)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
