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

# Fonctions de recherche
def search_media_by_name(name: str, media_type: str) -> list:
    """
    Recherche des films ou des séries par nom.
    
    Args:
        name (str): Le nom à chercher.
        media_type (str): Le type de média ('movies' ou 'series').
    
    Returns:
        list: Une liste de dictionnaires contenant les résultats de la recherche.
    """
    if media_type == 'movies':
        cursor = movies_collection.find({'title': {'$regex': f'.*{name}.*', '$options': 'i'}}, {'_id': 0})
        return list(cursor)
    elif media_type == 'series':
        cursor = series_collection.find({'title': {'$regex': f'.*{name}.*', '$options': 'i'}}, {'_id': 0})
        return list(cursor)
    else:
        raise ValueError("Invalid media type. Choose from 'movies', or 'series'.")

def search_media_by_actors(actor, media_type):
    if media_type == 'movies':
        cursor = movies_collection.find({'stars': {'$regex': f'.*{actor}.*', '$options': 'i'}}, {'_id': 0})
        return list(cursor)
    elif media_type == 'series':
        cursor = series_collection.find({'stars': {'$regex': f'.*{actor}.*', '$options': 'i'}}, {'_id': 0})
        return list(cursor)
    else:
        raise ValueError("Invalid media type. Choose from 'movies', or 'series'.")
    
def search_media_by_genre(genre: str, media_type: str) -> list:
    """
    Recherche des films ou des séries par genre.
    
    Args:
        genre (str): Le genre à chercher.
        media_type (str): Le type de média ('movies' ou 'series').
    
    Returns:
        list: Une liste de dictionnaires contenant les résultats de la recherche.
    """
    if media_type == 'movies':
        cursor = movies_collection.find({'genre': genre}, {'_id': 0})
        return list(cursor)
    elif media_type == 'series':
        cursor = series_collection.find({'genre': genre}, {'_id': 0})
        return list(cursor)
    else:
        raise ValueError("Invalid media type. Choose from 'movies', or 'series'.")

def search_media_by_duration(duration: int, media_type: str) -> list:
    """
    Recherche des films ou des séries par durée.
    
    Args:
        duration (int): La durée maximale (en minutes) à chercher.
        media_type (str): Le type de média ('movies' ou 'series').
    
    Returns:
        list: Une liste de dictionnaires contenant les résultats de la recherche.
    """
    if media_type == 'movies':
        cursor = movies_collection.find({'time': {'$lt': duration}}, {'_id': 0})
        return list(cursor)
    elif media_type == 'series':
        cursor = series_collection.find({'time': {'$lt': duration}}, {'_id': 0})
        return list(cursor)
    else:
        raise ValueError("Invalid media type. Choose from 'movies', or 'series'.")
    
def search_media_by_score(score: str, media_type: str) -> list:
    """
    Recherche des films ou des séries par score.
    
    Args:
        score (str): Le score minimal à chercher.
        media_type (str): Le type de média ('movies' ou 'series').
    
    Returns:
        list: Une liste de dictionnaires contenant les résultats de la recherche.
    """
    if media_type == 'movies':
        cursor = movies_collection.aggregate([
            {'$addFields': {'score_num': {'$toDouble': '$score'}}},
            {'$match': {'score_num': {'$gte': score}}},
            {'$sort': {'score_num': -1}},
            {'$project': {'score_num': 0}},
            {'$project': {'_id': 0}}])
        return list(cursor)
    elif media_type == 'series':
        cursor = series_collection.aggregate([
            {'$addFields': {'score_num': {'$toDouble': '$score'}}},
            {'$match': {'score_num': {'$gte': score}}},
            {'$sort': {'score_num': -1}},
            {'$project': {'score_num': 0}},
            {'$project': {'_id': 0}}])
        return list(cursor)
    else:
        raise ValueError("Invalid media type. Choose from 'movies', or 'series'.")