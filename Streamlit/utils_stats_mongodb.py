import pymongo
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Connection à la base de données Atlas MongoDB
load_dotenv(dotenv_path='/home/apprenant/Documents/DevIA/Projet_DevIA/Scrapping-IMDB/.env')
ATLAS_KEY = os.getenv('ATLAS_KEY')
client = MongoClient(ATLAS_KEY)
db = client['imbd-scrap']
movies_collection = db['movies']
series_collection = db['series']

def get_top_movies(n):
    top_movies = movies_collection.find({}, {'_id': 0, 'title': 1, 'score': 1}).sort('score', pymongo.DESCENDING).limit(n)
    nth_score = top_movies[n-1]['score']
    # Filtrer les films avec un score supérieur ou égal au n-ème score
    top_movies = [movie for movie in movies_collection.find({'score': {'$gte': nth_score}}, {'_id': 0, 'title': 1, 'score': 1}).sort('score', pymongo.DESCENDING)]
    df = pd.DataFrame(top_movies, columns=['title', 'score'])
    return df

def count_movies_by_actor(actor_name):
    count = movies_collection.count_documents({"stars": {"$regex": actor_name, "$options": "i"}})
    return f"{actor_name} a joué dans {count} films"


def get_top_movies_by_genre(genre, n):
    # Récupérer les n meilleurs films pour le genre donné
    top_movies = list(movies_collection.find({'genre': genre}, {'_id':0}).sort([('score', -1)]).limit(n))
    if len(top_movies) > 0:
        # Récupérer le score du n-ème film pour filtrer les films ex-aequo
        nth_score = top_movies[-1]['score']
        # Récupérer les films ex-aequo avec le n-ème film
        additional_movies = list(movies_collection.find({'genre': genre, 'score': nth_score}).sort([('score', -1)]).skip(n))
        top_movies.extend(additional_movies)
        return top_movies
    else:
        return None

def get_top_movies_by_country(country):
    top_100_movies = movies_collection.find().sort('score', pymongo.DESCENDING).limit(100)
    nb_movies = 0
    for movie in top_100_movies:
        if country in movie['country']:
            nb_movies += 1
    return f"Parmi les 100 films les mieux notés, {nb_movies} sont du pays {country}."


def get_avg_duration_by_genre():
    genres = movies_collection.distinct('genre')
    result = {}
    for genre in genres:
        count = movies_collection.count_documents({'genre': genre})
        total_duration = sum(movie['time'] for movie in movies_collection.find({'genre': genre}))
        avg_duration = total_duration / count
        result[genre] = round(avg_duration, 2)
    df = pd.DataFrame(list(result.items()), columns=['genre', 'durée moyenne (min)'])
    return df



