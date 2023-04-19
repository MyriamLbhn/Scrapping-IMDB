# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient
from dotenv import load_dotenv
import os

class ScrapPipeline(object):
    
    def __init__(self) -> None:
        load_dotenv(dotenv_path='/home/apprenant/Documents/DevIA/Projet_DevIA/Scrapping-IMDB/.env')
        ATLAS_KEY = os.getenv('ATLAS_KEY')
        self.client = MongoClient(ATLAS_KEY)
        self.db = self.client['imbd-scrap']
        self.movies_collection = self.db['movies']
        self.series_collection = self.db['series']

    def process_item(self, item, spider):
        if spider.name == 'top_rated_movies':
            self.movies_collection.insert_one(dict(item))
        elif spider.name == 'top_rated_series':
            self.series_collection.insert_one(dict(item))
        return item
    
    
        

