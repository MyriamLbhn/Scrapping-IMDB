import streamlit as st
import pandas as pd

# Chargement des données
movies_df = pd.read_csv('/home/apprenant/Documents/DevIA/Projet_DevIA/Scrapping-IMDB/scrap/scrap/top_rated_movies.csv')
series_df = pd.read_csv('/home/apprenant/Documents/DevIA/Projet_DevIA/Scrapping-IMDB/scrap/scrap/top_rated_series.csv')

def get_formatted_results(df):
    df = df.loc[:, ['title', 'original_title', 'score', 'genre', 'year', 'time', 'stars', 'country', 'storyline', 'public']]
    df['year'] = df['year'].astype(str).str.replace(',', '')
    return df

# Fonctions de recherche
def search_movies_by_name(name):
    results = movies_df[movies_df['title'].str.contains(name, case=False)]
    return results

def search_movies_by_actors(actors):
    results = movies_df[movies_df['stars'].str.contains(actors, case=False)]
    return results

def get_unique_genres(df):
    all_genres = []
    for genres in df['genre'].str.split(','):
        all_genres += genres
    unique_genres = sorted(set(all_genres))
    return unique_genres

def search_movies_by_genre(genre):
    results = movies_df[movies_df['genre'].str.contains(genre, case=False)]
    return results

def search_movies_by_duration(duration):
    results = movies_df[movies_df['time'] <= duration]
    return results

def search_movies_by_score(score):
    results = movies_df[movies_df['score'] >= score].sort_values(by='score', ascending=False)
    return results

def search_series_by_name(name):
    results = series_df[series_df['title'].str.contains(name, case=False)]
    return results

def search_series_by_actors(actors):
    results = series_df[series_df['stars'].str.contains(actors, case=False)]
    return results

def search_series_by_genre(genre):
    results = series_df[series_df['genre'].str.contains(genre, case=False)]
    return results

def search_series_by_duration(duration):
    results = series_df[series_df['time'] <= duration]
    return results

def search_series_by_score(score):
    results = series_df[series_df['score'] >= score].sort_values(by='score', ascending=False)
    return results