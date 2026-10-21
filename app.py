import os
import secrets

from flask import Flask, request, redirect, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash

from lib.login_required import *
from lib.User import *
from lib.UserRepository import *
from lib.film_repository import *
from lib.DatabaseConnection import *
from lib.BookRepository import *

app = Flask(__name__)
# The session key comes from the environment. Without it, a random key is
# made at start, so a restart logs everyone out but nothing is guessable.
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)


#BOOKS ----------------------------------------------------------

@app.route("/books", methods = ["GET"])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BooksRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books = books )

#Log in before you're able to create books.
@app.route('/books', methods=['POST'])
@login_required
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BooksRepository(connection)
    book_details = request.form
    book = Books(title=book_details["title"], author=book_details["author"])
    book_repository.create_book(book)
    return redirect ("/books")

#FILMS ----------------------------------------------------------

@app.route('/films', methods=['GET'])
def get_all_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    return render_template("films.html", films=films)

#Log in before you're able to create films.
@app.route('/films', methods=['POST'])
@login_required
def make_new_film():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    film_details = request.form
    film = Film(title=film_details["title"], genre=film_details["genre"], release_year=film_details["release_year"])
    film_repository.create_film(film)
    return redirect("/films")

#USER --------------------------------------------------------------

@app.route('/users/new', methods=['GET'])
def get_signup_form():
    return render_template("signup_form.html")

@app.route('/sessions/new', methods=['GET'])
def get_login_form():
    return render_template("login_form.html")

# Sign up: the password is stored only as a salted hash, never as plain text.
@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    user = User(
        username=user_details["username"],
        password=generate_password_hash(user_details["password"]),
    )
    user_repository.create(user)
    return redirect("/books")

# Log in: compare the typed password with the stored hash.
@app.route('/sessions', methods=['POST'])
def create_session():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)

    username = request.form["username"]
    password = request.form["password"]

    user = user_repository.find_by_username(username)

    if user is not None and check_password_hash(user.password, password):
        session["user_id"] = user.id
        session["username"] = user.username
        return redirect("/books")
    else:
        return redirect("/sessions/new")


# Debug mode only when FLASK_DEBUG=1 (local development). Never in production:
# the debugger would let anyone who reaches the port run code on the server.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=os.environ.get("FLASK_DEBUG") == "1")
