import streamlit as st
import pandas as pd
from utils_mongodb import *

st.set_page_config(page_title="Recherche de films et de séries sur IMDb", page_icon=":clapper:", layout="wide")

# Onglets
tabs = ['Films', 'Séries']
selected_tab = st.sidebar.radio('Sélectionnez une catégorie', tabs)

# Interface utilisateur
st.title('Recherche de films et de séries sur IMDb')

# Recherche par nom
st.header('Recherche par nom')
name = st.text_input('Nom du film ou de la série')
if name:
    if selected_tab == 'Films':
        results = search_movies_by_name(name)
    else:
        results = search_series_by_name(name)
    if results:
        df = pd.DataFrame(results)
        st.write(df)
    else:
        st.write('Aucun résultat')


# Recherche par acteur(s)
st.header('Recherche par acteur(s)')
actors = st.text_input('Acteur(s)')
if actors:
    if selected_tab == 'Films':
        results = search_movies_by_actors(actors)
    else:
        results = search_series_by_actors(actors)
    if results:
        df = pd.DataFrame(results)
        st.write(df)
    else:
        st.write('Aucun résultat')


# Recherche par genre
st.header('Recherche par genre')
genres = movies_collection.distinct('genre')
genre = st.selectbox('Genre', genres)
if genre:
    if selected_tab == 'Films':
        results = search_movies_by_genre(genre)
    else:
        results = search_series_by_genre(genre)
    if results:
        df = pd.DataFrame(results)
        st.write(df)
    else:
        st.write('Aucun résultat')


# Recherche par durée
st.header('Recherche par durée')
duration = st.slider('Durée maximale', 0, 300, 120)
if duration:
    if selected_tab == 'Films':
        results = search_movies_by_duration(duration)
    else:
        results =search_series_by_duration(duration)
    if results:
        df = pd.DataFrame(results)
        st.write(df)
    else:
        st.write('Aucun résultat')


# Recherche par note minimale
st.header('Recherche par note minimale')
score = st.slider('Note minimale', 8.0, 10.0, 8.0, 0.1)
if score:
    if selected_tab == 'Films':
        results = search_movies_by_score(score)
    else :
        results = search_series_by_score(score)
    if results:
        df = pd.DataFrame(results)
        st.write(df)
    else:
        st.write('Aucun résultat')
