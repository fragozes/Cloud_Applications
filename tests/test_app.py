import sys
import os

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_films_returns():
    client = app.test_client()
    response = client.get("/films")
    assert 'Film1' in response.data.decode('utf-8')
    assert 'Grown Ups' in response.data.decode('utf-8') 