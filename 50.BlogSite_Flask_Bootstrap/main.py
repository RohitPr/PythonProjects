from flask import Flask, render_template, request
import requests
import smtplib


# Custom API Created using npoint and saved it in JSON format
API_URL = "https://api.npoint.io/2722c84e8ff4b2ddbd15"

# EMAIL CREDENTIALS
MY_EMAIL = "EMAIL"
MY_PASSWORD = "PASSWORD"

posts = requests.get(API_URL).json()

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', posts=posts)

# Send Email when user fills the contact form


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "message": request.form["message"],
            "phone": request.form["phone"]
        }
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:You have a new Message!\n\nNAME : {data['name']}\n EMAIL : {data['email']} \n PHONE : {data['phone']} \n MESSAGE : {data['message']} "
            )
        return render_template('updated.html')
    else:
        return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')

# Routes to different posts as per User's choice


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in posts:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
