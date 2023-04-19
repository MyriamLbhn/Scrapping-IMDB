import streamlit as st
import pymongo
import pandas as pd

# Connexion à la base de données
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['imdb']
collection = db['movies']

# Fonctions de recherche
def search_by_name(name):
    cursor = collection.find({'title': {'$regex': f'.*{name}.*', '$options': 'i'}})
    return list(cursor)

def search_by_actors(actors):
    cursor = collection.find({'stars': {'$in': actors}})
    return list(cursor)

def search_by_genre(genre):
    cursor = collection.find({'genre': genre})
    return list(cursor)

def search_by_duration(duration):
    cursor = collection.find({'time': {'$lt': duration}})
    return list(cursor)

def search_by_score(score):
    cursor = collection.aggregate([
        {'$match': {'score': {'$gte': score}}},
        {'$sort': {'score': -1}}
    ])
    return list(cursor)

# Interface utilisateur
st.title('Recherche de films sur IMDb')

# Recherche par nom
st.header('Recherche par nom')
name = st.text_input('Nom du film')
if name:
    results = search_by_name(name)
    if results:
        df = pd.DataFrame(results)
        st.write(df)
    else:
        st.write('Aucun résultat')

# Recherche par acteur(s)
st.header('Recherche par acteur(s)')
actors = st.text_input('Acteur(s)')
if actors:
    actors = actors.split(',')
    results = search_by_actors(actors)
    if results:
        df = pd.DataFrame(results)
        st.write(df)
    else:
        st.write('Aucun résultat')

# Recherche par genre
st.header('Recherche par genre')
genres = collection.distinct('genre')
genre = st.selectbox('Genre', genres)
if genre:
    results = search_by_genre(genre)
    if results:
        df = pd.DataFrame(results)
        st.write(df)
    else:
        st.write('Aucun résultat')

# Recherche par durée
st.header('Recherche par durée')
duration = st.slider('Durée maximale', 0, 300, 120)
results = search_by_duration(duration)
if results:
    df = pd.DataFrame(results)
    st.write(df)
else:
    st.write('Aucun résultat')

# Recherche par note minimale
st.header('Recherche par note minimale')
score = st.slider('Note minimale', 0, 10, 7)
results = search_by_score(score)
if results:
    df = pd.DataFrame(results)
    st.write(df)
else:
    st.write('Aucun résultat')
