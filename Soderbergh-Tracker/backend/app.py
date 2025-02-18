from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# The __name__ part is just telling Flask "this is my app right here in this file."
app = Flask(__name__)

# Base URL for all TMDb API requests
TMDB_BASE_URL = "https://api.themoviedb.org/3"

# I'll create the first "route". A route is like a door - when someone knocks on that door (visits that URL), it'll tell Flask what to do.
# The '/' means this is my home page (like the front door of a house).
@app.route('/')
def home():
    return "Hello! Welcome to the Soderbergh Movie Tracker!"

@app.route('/movies')
def get_soderbergh_movies():
    # Steven Soderbergh's TMDb ID is 1884
    url = f"{TMDB_BASE_URL}/person/1884/movie_credits"
    
    # Create parameters for the API request
    params = {
        'api_key': os.getenv('TMDB_API_KEY'),
        'language': 'en-US'
    }

    try:
        # Make the API request
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Filter for movies where Soderbergh was the director
            director_credits = [movie for movie in data['crew']
                                if movie['job'] == 'Director']
            # Sort the movies by release date
            director_credits.sort(key=lambda x: x['release_date'] if x['release_date'] else'9999')
            # Return the results
            return jsonify (director_credits)
        else:
            return jsonify({'error': 'Failed to fetch data from TMDb'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Here I tell Flask how to run the app. This is like saying "okay, now let's start playing"
if __name__ == '__main__':
    app.run(debug=True)