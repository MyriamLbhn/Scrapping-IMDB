import streamlit as st
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

# Fonctions de recherche pour les films
def search_movies_by_name(name):
    cursor = movies_collection.find({'title': {'$regex': f'.*{name}.*', '$options': 'i'}}, {'_id': 0})
    return list(cursor)

def search_movies_by_actors(actor):
    cursor = movies_collection.find({'stars': {'$regex': f'.*{actor}.*', '$options': 'i'}}, {'_id': 0})
    return list(cursor)

def search_movies_by_genre(genre):
    cursor = movies_collection.find({'genre': genre}, {'_id': 0})
    return list(cursor)

def search_movies_by_duration(duration):
    cursor = movies_collection.find({'time': {'$lt': duration}}, {'_id': 0})
    return list(cursor)

def search_movies_by_score(score):
    cursor = movies_collection.aggregate([
        {'$addFields': {'score_num': {'$toDouble': '$score'}}},
        {'$match': {'score_num': {'$gte': score}}},
        {'$sort': {'score_num': -1}},
        {'$project': {'score_num': 0}},
        {'$project': {'_id': 0}}])
    return list(cursor)


# Fonctions de recherche pour les séries
def search_series_by_name(name):
    cursor = series_collection.find({'title': {'$regex': f'.*{name}.*', '$options': 'i'}}, {'_id': 0})
    return list(cursor)

def search_series_by_actors(actor):
    cursor = series_collection.find({'stars': {'$regex': f'.*{actor}.*', '$options': 'i'}}, {'_id': 0})
    return list(cursor)

def search_series_by_genre(genre):
    cursor = series_collection.find({'genre': genre}, {'_id': 0})
    return list(cursor)

def search_series_by_duration(duration):
    cursor = series_collection.find({'time': {'$lt': duration}}, {'_id': 0})
    return list(cursor)

def search_series_by_score(score):
    cursor = series_collection.aggregate([
        {'$addFields': {'score_num': {'$toDouble': '$score'}}},
        {'$match': {'score_num': {'$gte': score}}},
        {'$sort': {'score_num': -1}},
        {'$project': {'score_num': 0}},
        {'$project': {'_id': 0}}])
    return list(cursor)