import streamlit as st
import pandas as pd
from utils_csv import *


st.set_page_config(page_title="Recherche de films et de séries sur IMDb", page_icon=":clapper:", layout="wide")


# Interface utilisateur
st.title('Recherche de films et de séries sur IMDb')

# Onglets
tabs = ['Films', 'Séries']
selected_tab = st.sidebar.selectbox('Sélectionnez une catégorie', tabs)

# Recherche par nom
st.header('Recherche par nom')
name = st.text_input('Nom du film ou de la série')
if name:
    if selected_tab == 'Films':
        results = search_movies_by_name(name)
    else:
        results = search_series_by_name(name)
    if not results.empty:
        formatted_results = get_formatted_results(results)
        st.write(formatted_results)
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
    if not results.empty:
        formatted_results = get_formatted_results(results)
        st.write(formatted_results)
    else:
        st.write('Aucun résultat')

# Recherche par genre
st.header('Recherche par genre')
genres = get_unique_genres(movies_df) if selected_tab == 'Films' else get_unique_genres(series_df)
genre = st.selectbox('Genre', genres)
if genre:
    if selected_tab == 'Films':
        results = search_movies_by_genre(genre)
    else:
        results = search_series_by_genre(genre)
    if not results.empty:
        formatted_results = get_formatted_results(results)
        st.write(formatted_results)
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
    if not results.empty:
        formatted_results = get_formatted_results(results)
        st.write(formatted_results)
    else:
        st.write('Aucun résultat')
    

# Recherche par note minimale
st.header('Recherche par note minimale')
score = st.slider('Note minimale', 0, 10, 7)
if score:
    if selected_tab == 'Films':
        results = search_movies_by_score(score)
    else :
        results = search_series_by_score(score)
    if not results.empty:
        formatted_results = get_formatted_results(results)
        st.write(formatted_results)
    else:
        st.write('Aucun résultat')
