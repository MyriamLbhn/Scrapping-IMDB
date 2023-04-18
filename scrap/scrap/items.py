# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TopMovieItem(scrapy.Item):
    title = scrapy.Field()
    original_title = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    year = scrapy.Field()
    time = scrapy.Field()
    storyline = scrapy.Field()
    stars = scrapy.Field()
    public = scrapy.Field()
    country = scrapy.Field()
