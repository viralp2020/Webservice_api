# Movie Renting Web App API

This is a simple Flask-based API for managing movie data. It supports operations such as retrieving a list of movies, adding a new movie, updating an existing movie, retrieving a specific movie by ID, and deleting a movie. The data is persisted in a JSON file (`movies.json`).

## Features

- **GET /movies**: Retrieve a list of all movies.
- **GET /movies/{movie_id}**: Retrieve details of a specific movie by its ID.
- **POST /movies**: Add a new movie to the database.
- **PUT /movies/{movie_id}**: Update details of a specific movie by its ID.
- **DELETE /movies/{movie_id}**: Delete a specific movie by its ID.

## Installation

1. Clone the repository:
    git clone https://github.com/viralp2020/Webservice_api.git
    cd movie-renting-web-app

2. Install the required dependencies:
    pip install -r requirements.txt
    

3. Run the application:
    python app.py
   

    The application will be running at [http://localhost:5000].

## Usage

### API Endpoints

- **GET /movies**: Retrieve a list of all movies.

curl http://localhost:5000/movies
  

- **GET /movies/{movie_id}**: Retrieve details of a specific movie by its ID.

    
    curl http://localhost:5000/movies/1
    

- **POST /movies**: Add a new movie to the database.

    
    curl -X POST -H "Content-Type: application/json" -d '{"id": 11, "name": "New Movie", "year": 2023, "genre": "Comedy", "rating": 8.0}' http://localhost:5000/movies
    

- **PUT /movies/{movie_id}**: Update details of a specific movie by its ID.

    
    curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Movie", "year": 2022, "genre": "Action", "rating": 9.0}' http://localhost:5000/movies/11
    

- **DELETE /movies/{movie_id}**: Delete a specific movie by its ID.

    
    curl -X DELETE http://localhost:5000/movies/11
    

### HTML Interface

You can also interact with the API using the HTML interface. Open your browser and navigate to [http://localhost:5000/movies](http://localhost:5000/movies).

## Data Persistence

Changes made through API endpoints are persistently stored in the `movies.json` file.

## Contributing

Contributions are welcome! If you find a bug, have a feature request, or would like to suggest improvements, please open an issue or submit a pull request.

