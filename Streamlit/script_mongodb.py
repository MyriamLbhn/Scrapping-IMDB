import streamlit as st
import pandas as pd
from utils_search_mongodb import *
from utils_stats_mongodb import *

st.set_page_config(page_title="Recherche de films et de séries sur IMDb", page_icon=":clapper:", layout="wide")

# Onglets
tabs = ['Films', 'Séries', 'Quelques stats sur les films' ]
selected_tab = st.sidebar.radio('Sélectionnez une catégorie', tabs)


if selected_tab in ['Films', 'Séries'] : 
    # Interface utilisateur
    st.title('Recherche de films et de séries sur IMDb')

    # Recherche par nom
    st.header('Recherche par nom')
    name = st.text_input('Nom du film ou de la série')
    if name:
        if selected_tab == 'Films':
            results = search_media_by_name(name, 'movies')
        else:
            results = search_media_by_name(name, 'series')
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
            results = search_media_by_actors(actors, 'movies')
        else:
            results = search_media_by_actors(actors, 'series')
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
            results = search_media_by_genre(genre, 'movies')
        else:
            results = search_media_by_genre(genre, 'series')
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
            results = search_media_by_duration(duration, 'movies')
        else:
            results =search_media_by_duration(duration, 'series')
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
            results = search_media_by_score(score, 'movies')
        else :
            results = search_media_by_score(score, 'series')
        if results:
            df = pd.DataFrame(results)
            st.write(df)
        else:
            st.write('Aucun résultat')


# Page Quelques stats sur les films
if selected_tab == 'Quelques stats sur les films':
    
    # Affichage du top 5 des films
    st.header('Top des films avec les 5 meilleures notes')
    top_movies_df = get_top_movies(5)
    st.write(top_movies_df)

    # Affichage du nombre de films selon l'acteur
    st.header('Nombre de films par acteur')
    actor = st.text_input("Nom de l'acteur")
    if actor:
        result = count_movies_by_actor(actor)
        st.write(result)


     # Afficher les titres des films et leur score
    st.header(f"Top des films avec les 3 meilleures notes par genre :")
    st.write('Recherche par genre')
    genres = movies_collection.distinct('genre')
    genre = st.selectbox('Genre', genres)
    top_movies = get_top_movies_by_genre(genre, 3)
    df = pd.DataFrame(top_movies)
    st.dataframe(df)
    
    # Afficher le % de films d'un pays dans le top 100
    st.header(f"Pourcentage de films dans le top 100 selon le pays :")
    st.write('Recherche par pays')
    st.header('Recherche par pays')
    countries = movies_collection.distinct('country')
    country = st.selectbox('Pays', countries)
    result = get_top_movies_by_country(country)
    st.write(result)
    
    # Affichage des résultats
    st.header("Durée moyenne par genre :")
    df = get_avg_duration_by_genre()
    st.dataframe(df)
