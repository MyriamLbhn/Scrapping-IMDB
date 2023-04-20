# Scrapping-IMDB

Projet de Web Scraping et de manipulation de données avec Python, MongoDB et Scrapy.

Dans ce projet, nous allons récupérer les informations de l'IMDb à partir de différentes sections et les stocker dans une base de données MongoDB hébergée sur Atlas. Nous utiliserons Scrapy pour extraire les données de l'IMDb et pymongo pour interagir avec notre base de données MongoDB.

## Partie 1 :
Dans la première partie du projet, nous allons extraire des informations sur le top 250 des meilleurs films et séries sur IMBD.
Nous allons sauvegarder ces informations dans un fichier CSV en utilisant des Spiders différents pour les films et les séries.

## Partie 2 : 
Dans la deuxième partie du projet, nous allons stocker les informations récupérées dans notre base de données MongoDB hébergée sur Atlas. Nous allons utiliser pymongo pour interagir avec notre base de données. Nous allons également répondre à plusieurs questions en effectuant des requêtes pymongo (dans le notebook *requests.ipynb*). Pour scraper les données directement sur Atlas, il faut effectuer la commande `scrapy crawl top_rated_movies` ou `scrapy crawl top_rated_series`

## Partie 3 : 
Application streamlit pour présenter le projet. L'application dispose de 3 onglets. 
L'onglet "Films" qui affiche les informations des 250 meilleurs films. L'onglet "Séries" qui affiche les informations des 250 meilleures séries.
L'onglet "Quelques stats sur les films" qui reprends les réponses du notebook.

## Fichiers :
Projet scrapy : scrap  
    scrap > scrap > spiders > *scrap_film.py* : fichier spider pour extraire les informations sur les films  
                              *scrap_serie.py* : fichier spider pour extraire les informations sur les series  
                    *fonctions.py* : contient la fonction pour convertir la durée du film en minute  
                    *items.py* : contient le modèle pour nos items scrapés  
                    *pipelines.py* : contient la pipeline pour envoyer les données scrapées directement sur Atlas  
                    *top_rated_movies.csv* : fichier csv contenant les informations des films, générés avec la commande `scrapy crawl top_rated_movies -O top_rated_movies.csv`  
                    *top_rated_series.csv* : fichier csv contenant les informations des films, générés avec la commande `scrapy crawl top_rated_series -O top_rated_series.csv`  
  


Notebook : *requests.ipynb* -> contient des reqêtes pymongo pour répondre à des des questions (type Top 3 des films par genre)
  


Streamlit : pour lancer l'application, utiliser la commande "streamlit run fichier_script.py"  
    - *script_csv.py* : script qui utilise les données du fichier csv  
    - *utils_csv.py* : fonctions nescessaires à l'application script_csv  
    - *script_mongodb.py* : script qui utilise les données stockées sur le cloud MongoDB Atlas  
    - *utils_search_mongodb.py* : fonctions de recherche des films et séries par nom, genre, acteurs...  
    - *utils_stats_mongodb.py* : fonctions pour répondre à quelques questions statistiques sur les films.  
                   
## Requirement.txt :
Pour installer les modules python nécessaires, effectuer la commande `pip install -r requirements.txt`

## Confidentialité
Il faut créer un fichier *.env* qui contient votre clé Atlas :  
`ATLAS_KEY=mongodb+srv://<username>:<password>@<cluster_name>.tpkbwnd.mongodb.net/test`
