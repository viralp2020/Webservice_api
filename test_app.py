import json
import pytest
from flask import Flask
from flask.testing import FlaskClient
from flask_restx import Api, Resource, fields
from flask_httpauth import HTTPBasicAuth
from app import app, movies  # Import 'app' from app.py
# from app import movies  # Import your local database

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'localhost:5000'  # Adjust the port and host as needed
    with app.test_client() as client:
        yield client

def test_get_movies(client):
    response = client.get('/movies')
    assert response.status_code == 200
    assert json.loads(response.data) == movies

def test_get_movie(client):
    movie_id = 1
    response = client.get(f'/movies/{movie_id}')
    assert response.status_code == 200
    assert json.loads(response.data) == next((m for m in movies if m['id'] == movie_id), None)

def test_get_nonexistent_movie(client):
    movie_id = 999
    response = client.get(f'/movies/{movie_id}')
    assert response.status_code == 404
    assert "not found" in response.get_data(as_text=True).lower()

# Add more tests as needed

if __name__ == '__main__':
    pytest.main()
