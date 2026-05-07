from flask import Flask
# Add 'render_template' to your listed imports from Flask
from flask import Flask, render_template 
# instantiate a Flask app object
app = Flask(__name__)


#Exercise
@app.route('/books_dic', methods = ['GET'])
def books():
    dis = [{
    "title": "The Gruffalo",
    "author": "Julia Donaldson"
    },
    {
    "title": "Ada Twist, Scientist",
    "author": "Andrea Beaty"
    },
    {
    "title": "The Girl Who Drank the Moon",
    "author": "Kelly Barnhill"
    },
    {
    "title": "Dragons in a Bag",
    "author": "Zetta Elliott"
    }
    ]
    return dis



# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

# NEW PART START

# duplicate route
@app.route('/hello1', methods=['GET'])
def hello_again():
    return "Hello, hello and hello again!"


#Challenge
print("test")
@app.route('/authors', methods=['GET'])
def authors():
    dic = [
    {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
    },
    {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
    },
    {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
    },
    {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
    }
    ]
    return dic


@app.route("/books_html", methods = ["GET"])
def books_html():
    return render_template("books_ht.html")

#Flask just run files inside (templates folder)
@app.route("/css_practice", methods = ["GET"])
def index_html_css():
    return render_template("css_practice/index.html")

@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)


from lib.DatabaseConnection import *
from lib.BookRepository import *
@app.route("/books", methods = ["GET"])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BooksRepository(connection)
    books = book_repository.all()
    # print(books)
    return render_template("books.html", books = books )

# NEW PART END

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
#**************************************************************
#All calling methods must be before this condition.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
#**************************************************************