from flask import Flask
from flask.testing import FlaskClient
from flask_restx import Api, Resource, fields
from flask_httpauth import HTTPBasicAuth
import json

app = Flask(__name__)
auth = HTTPBasicAuth()

# Create an instance of the Api class
api = Api(app, version='1.0', title='Movie Renting API', description='API for managing movie data')

# Define the movie model for Swagger documentation
movie_model = api.model('Movie', {
    'id': fields.Integer(required=True, description='Movie ID'),
    'name': fields.String(required=True, description='Movie Name'),
    'year': fields.Integer(description='Release Year'),
    'genre': fields.String(description='Genre'),
    'rating': fields.Float(description='Rating'),
})

# Sample hardcoded username and password (replace with your actual credentials)
users = {
    'admin': 'admin'
}

# Load existing data from the JSON file or create an empty list
try:
    with open('movies.json', 'r') as file:
        movies = json.load(file)
except FileNotFoundError:
    movies = []

# HTTP basic authentication callback
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

# Routes
@api.route('/movies')
class MoviesResource(Resource):
    @api.marshal_list_with(movie_model)
    def get(self):
        return movies

    @api.expect(movie_model)
    @api.marshal_with(movie_model, code=201)
    def post(self):
        new_movie = request.get_json()
        new_movie_id = new_movie.get('id')

        # Check if the movie with the same ID already exists
        if any(movie['id'] == new_movie_id for movie in movies):
            return {'error': f'Movie with ID {new_movie_id} already exists'}, 400

        movies.append(new_movie)

        # Save the updated data to the JSON file
        with open('movies.json', 'w') as file:
            json.dump(movies, file, indent=2)

        return new_movie, 201

@api.route('/movies/<int:movie_id>')
class MovieResource(Resource):
    @api.marshal_with(movie_model)
    def get(self, movie_id):
        movie = next((m for m in movies if m['id'] == movie_id), None)
        if movie:
            return movie
        else:
            api.abort(404, f"Movie {movie_id} not found")

    @api.expect(movie_model)
    @api.marshal_with(movie_model)
    def put(self, movie_id):
        movie = next((m for m in movies if m['id'] == movie_id), None)
        if movie:
            updated_movie = request.get_json()
            movie.update(updated_movie)

            # Save the updated data to the JSON file
            with open('movies.json', 'w') as file:
                json.dump(movies, file, indent=2)

            return movie
        else:
            api.abort(404, f"Movie {movie_id} not found")

    @auth.login_required  # Requires authentication for this endpoint
    @api.response(204, 'Movie deleted')
    def delete(self, movie_id):
        global movies
        movies = [m for m in movies if m['id'] != movie_id]

        # Save the updated data to the JSON file
        with open('movies.json', 'w') as file:
            json.dump(movies, file, indent=2)

        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
