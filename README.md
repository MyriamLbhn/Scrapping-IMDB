# Scrapping-IMDB

Projet de Web Scraping et de manipulation de données avec Python, MongoDB et Scrapy.

Dans ce projet, nous allons récupérer les informations de l'IMDb à partir de différentes sections et les stocker dans une base de données MongoDB hébergée sur Atlas. Nous utiliserons Scrapy pour extraire les données de l'IMDb et pymongo pour interagir avec notre base de données MongoDB.

## Partie 1 :
Dans la première partie du projet, nous allons extraire des informations sur le top 250 des meilleurs films sur IMBD.
Nous allons sauvegarder ces informations dans un fichier CSV en utilisant des Spiders différents pour les films et les séries.

## Partie 2 : 
Dans la deuxième partie du projet, nous allons stocker les informations récupérées dans notre base de données MongoDB hébergée sur Atlas. Nous allons utiliser pymongo pour interagir avec notre base de données. Nous allons également répondre à plusieurs questions en effectuant des requêtes pymongo (dans le notebook request.ipynb)

## Fichiers :
Projet scrapy : scrap
    scrap > scrap > spiders > scrap_film.py : fichier spider pour extraire les informations sur les films
                    scrap_serie.py : fichier spider pour extraire les informations sur les series
                    fonctions.py : contient la fonction pour convertir la durée du film en minute
                    items.py : contient le modèle pour nos items scrapés
                    pipelines.py : contient la pipeline pour envoyer les données scrapées directement sur Atlas
                    top_rated_movies.csv : fichier csv contenant les informations des films, générés avec la commande "scrapy crawl top_rated_movies -O top_rated_movies.csv"
                    



## Confidentialité
Il faut créer un fichier .env; qui contient :
ATLAS_KEY=mongodb+srv://<username>:<password>@<cluster_name>.tpkbwnd.mongodb.net/test
