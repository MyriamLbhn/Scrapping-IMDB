import streamlit as st
import pandas as pd

# Chargement des données
movies_df = pd.read_csv('/home/apprenant/Documents/DevIA/Projet_DevIA/Scrapping-IMDB/scrap/scrap/top_rated_movies.csv')
series_df = pd.read_csv('/home/apprenant/Documents/DevIA/Projet_DevIA/Scrapping-IMDB/scrap/scrap/top_rated_series.csv')

def get_formatted_results(df: pd.DataFrame) -> pd.DataFrame:
    '''    
    Renvoie les colonnes 'title', 'original_title', 'score', 'genre', 'year', 'time', 'stars', 'country', 'storyline'
    et 'public' du dataframe df, avec une colonne 'year' convertie en string et les autres colonnes non modifiées.
    
    Args:
        df (pd.DataFrame): Le dataframe à formatter.
    
    Returns:
        pd.DataFrame: Le dataframe formaté.
    '''
    df = df.loc[:, ['title', 'original_title', 'score', 'genre', 'year', 'time', 'stars', 'country', 'storyline', 'public']]
    df['year'] = df['year'].astype(str).str.replace(',', '')
    return df

# Fonctions de recherche
def search_movies_by_name(name: str) -> pd.DataFrame:
    '''
        Recherche les films par titre.
    
    Args:
        name (str): Le nom à chercher dans les titres de films.
    
    Returns:
        pd.DataFrame: Le dataframe contenant les résultats de recherche.
    '''
    results = movies_df[movies_df['title'].str.contains(name, case=False)]
    return results

def search_movies_by_actors(actors: str) -> pd.DataFrame:
    '''
        Recherche les films par acteurs.
    
    Args:
        actors (str): Les noms à chercher dans les castings de films.
    
    Returns:
        pd.DataFrame: Le dataframe contenant les résultats de recherche.
    '''
    results = movies_df[movies_df['stars'].str.contains(actors, case=False)]
    return results

def get_unique_genres(df: pd.DataFrame) -> list[str]:
    '''
        Renvoie la liste des genres de films ou de séries uniques présents dans le dataframe df.
    
    Args:
        df (pd.DataFrame): Le dataframe contenant les genres à lister.
    
    Returns:
        List[str]: La liste des genres uniques.
    '''
    all_genres = []
    for genres in df['genre'].str.split(','):
        all_genres += genres
    unique_genres = sorted(set(all_genres))
    return unique_genres

def search_movies_by_genre(genre: str) -> pd.DataFrame:
    '''
        Recherche les films selon leur genre.
    
    Args:
        genre (str): Le genre à chercher dans les films.
    
    Returns:
        pd.DataFrame: Le dataframe contenant les résultats de recherche.
    '''
    results = movies_df[movies_df['genre'].str.contains(genre, case=False)]
    return results

def search_movies_by_duration(duration: int) -> pd.DataFrame:
    '''
        Recherche les films ayant une durée inférieure ou égale à une certaines durée en minutes.
    
    Args:
        duration (int): La durée maximale en minutes.
    
    Returns:
        pd.DataFrame: Le dataframe contenant les résultats de recherche.
    '''
    results = movies_df[movies_df['time'] <= duration]
    return results

def search_movies_by_score(score: str) -> pd.DataFrame:
    '''
        Recherche les films ayant une note supérieure ou égale à une score donné.
    
    Args:
        score (string): La note minimale.
    
    Returns:
        pd.DataFrame: Le dataframe contenant les résultats de recherche, triés par note décroissante.
    '''
    results = movies_df[movies_df['score'] >= score].sort_values(by='score', ascending=False)
    return results

def search_series_by_name(name: str) -> pd.DataFrame:
    '''
        Recherche les séries par titre.
    
    Args:
        name (str): Le nom à chercher dans les titres de séries.
    
    Returns:
        pd.DataFrame: Le dataframe contenant les résultats de recherche.
    '''
    results = series_df[series_df['title'].str.contains(name, case=False)]
    return results

def search_series_by_actors(actors: str) -> pd.DataFrame:
    '''
        Recherche les séries par acteurs.
    
    Args:
        actors (str): Les noms à chercher dans les castings de séries.
    
    Returns:
        pd.DataFrame: Le dataframe contenant les résultats de recherche.
    '''
    results = series_df[series_df['stars'].str.contains(actors, case=False)]
    return results

def search_series_by_genre(genre: str) -> pd.DataFrame:
    '''
        Recherche les séries selon leur genre.
    
    Args:
        genre (str): Le genre à chercher dans les séries.
    
    Returns:
        pd.DataFrame: Le dataframe contenant les résultats de recherche.
    '''
    results = series_df[series_df['genre'].str.contains(genre, case=False)]
    return results

def search_series_by_duration(duration: int) -> pd.DataFrame:
    '''
        Recherche les séries ayant des épisodes d'une durée inférieure ou égale à une certaines durée en minutes.
    
    Args:
        duration (int): La durée maximale en minutes.
    
    Returns:
        pd.DataFrame: Le dataframe contenant les résultats de recherche.
    '''
    results = series_df[series_df['time'] <= duration]
    return results

def search_series_by_score(score: str) -> pd.DataFrame:
    '''
        Recherche les séries ayant une note supérieure ou égale à une score donné.
    
    Args:
        score (float): La note minimale.
    
    Returns:
        pd.DataFrame: Le dataframe contenant les résultats de recherche, triés par note décroissante.
    '''
    results = series_df[series_df['score'] >= score].sort_values(by='score', ascending=False)
    return results