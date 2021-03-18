from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

MOVIE_API = "https://api.themoviedb.org/3/search/movie"
MOVIE_API_KEY = "bad4399b890419abc9554858d74be3ef"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# WTF Form for Editing the rating and review


class MovieEdit(FlaskForm):
    updated_review = StringField('Your Review', validators=[
        DataRequired()])
    submit = SubmitField('Submit')


class AddMovie(FlaskForm):
    add_movie = StringField(
        'Movie Title', validators=[DataRequired()])
    submit = SubmitField('Search Movie')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///all_movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Creates the SQLite Database


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String, unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String, unique=False, nullable=True)
    img_url = db.Column(db.String, unique=False, nullable=False)

    # This allows each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# Enters the following details in the created database

# if db.session.query(Movie).count() < 1:
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper     rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)


@ app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = MovieEdit()
    movie_id = request.args.get('id')
    if form.validate_on_submit():
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.review = form.updated_review.data
        db.session.commit()
        return redirect(url_for('home'))
    movie_selected = Movie.query.get(movie_id)
    return render_template('edit.html', form=form, movie=movie_selected)


@ app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


movie_data = []


@ app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_name = form.add_movie.data
        search_params = {
            "api_key": MOVIE_API_KEY,
            "query": movie_name,
        }
        movie_info = requests.get(
            MOVIE_API, params=search_params).json()["results"]
        for movie in movie_info:
            movie_data.append({
                "id": movie["id"],
                "movie_name": movie["title"],
                "movie_year": movie["release_date"].split("-")[0],
            })
        return render_template('select.html', all_movies=movie_data)
    return render_template('add.html', form=form)


@ app.route('/select')
def select():
    movie_id = request.args.get('id')
    if movie_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        response = requests.get(movie_api_url, params={
                                "api_key": MOVIE_API_KEY, "language": "en-US"})
        data = response.json()
        add_new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"],
            rating=data["vote_average"],
        )
        db.session.add(add_new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=add_new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
