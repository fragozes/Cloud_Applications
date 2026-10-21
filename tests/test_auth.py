from app import app
from lib.DatabaseConnection import DatabaseConnection


def reset_users():
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    return connection


def sign_up(client, username, password):
    return client.post("/users", data={"username": username, "password": password})


def test_password_is_stored_as_a_hash_not_plain_text():
    connection = reset_users()
    sign_up(app.test_client(), "hashuser", "s3cret-pass")

    stored = connection.execute("SELECT password FROM users WHERE username = 'hashuser'")[0]["password"]

    assert stored != "s3cret-pass"
    assert "s3cret-pass" not in stored


def test_login_with_the_right_password_starts_a_session():
    reset_users()
    client = app.test_client()
    sign_up(client, "loginuser", "right-pass")

    response = client.post("/sessions", data={"username": "loginuser", "password": "right-pass"})

    assert response.status_code == 302
    assert response.headers["Location"] == "/books"
    with client.session_transaction() as session:
        assert session["username"] == "loginuser"


def test_login_with_a_wrong_password_goes_back_to_the_form():
    reset_users()
    client = app.test_client()
    sign_up(client, "wrongpass", "right-pass")

    response = client.post("/sessions", data={"username": "wrongpass", "password": "wrong-pass"})

    assert response.headers["Location"] == "/sessions/new"
    with client.session_transaction() as session:
        assert "user_id" not in session


def test_login_with_an_unknown_user_goes_back_to_the_form():
    reset_users()

    response = app.test_client().post("/sessions", data={"username": "nobody", "password": "x"})

    assert response.status_code == 302
    assert response.headers["Location"] == "/sessions/new"


def test_creating_a_book_needs_a_login():
    response = app.test_client().post("/books", data={"title": "T", "author": "A"})

    assert response.headers["Location"] == "/sessions/new"


def test_creating_a_film_needs_a_login():
    response = app.test_client().post("/films", data={"title": "T", "genre": "G", "release_year": "2000"})

    assert response.headers["Location"] == "/sessions/new"


def test_protected_routes_keep_their_own_names():
    # Without functools.wraps every protected route would be named
    # "decorated_function", and Flask refuses a second one.
    assert "create_book" in app.view_functions
    assert "make_new_film" in app.view_functions
