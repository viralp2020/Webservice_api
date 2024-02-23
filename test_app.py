import unittest
import json
import app

class TestMoviesAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.setup_test_data()

    def setup_test_data(self):
        # Add code to insert test data into the database
        pass

    def test_get_movies(self):
        response = self.app.get('/movies')
        self.assertEqual(response.status_code, 200)

    def test_get_movie_by_id(self):
        # Assuming there's a movie with ID 1 in your test data
        response = self.app.get('/movies/1')
        self.assertEqual(response.status_code, 200)
        movie = json.loads(response.data)
        self.assertEqual(movie['id'], 1)

    def test_create_movie(self):
        new_movie = {'id': 100, 'name': 'Test Movie', 'year': 2022, 'genre': 'Test Genre', 'rating': 5.0}
        response = self.app.post('/movies', json=new_movie)
        self.assertEqual(response.status_code, 201)

        # Check if the movie is added to the database
        response = self.app.get('/movies/100')
        self.assertEqual(response.status_code, 200)
        movie = json.loads(response.data)
        self.assertEqual(movie['name'], 'Test Movie')

    def test_update_movie(self):
        # Assuming there's a movie with ID 1 in your test data
        updated_movie = {'name': 'Updated Movie', 'year': 2023, 'genre': 'Updated Genre', 'rating': 4.5}
        response = self.app.put('/movies/1', json=updated_movie)
        self.assertEqual(response.status_code, 200)

        # Check if the movie is updated in the database
        response = self.app.get('/movies/1')
        self.assertEqual(response.status_code, 200)
        movie = json.loads(response.data)
        self.assertEqual(movie['name'], 'Updated Movie')

    def test_delete_movie(self):
        # Assuming there's a movie with ID 1 in your test data
        response = self.app.delete('/movies/1')
        self.assertEqual(response.status_code, 204)

        # Check if the movie is deleted from the database
        response = self.app.get('/movies/1')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
