from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TopMovieItem
import scrapy


class IMDbTop250Movie(CrawlSpider):
    name = 'top_rated_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']
    movie_count = 0

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    rules = (
        Rule(LinkExtractor(restrict_css=".titleColumn a"), callback="parse_movie"),
    )

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers={
            'User-Agent': self.user_agent
        })

    def parse_movie(self, response):
        title = response.css("h1[data-testid='hero__pageTitle'] span::text").get().strip()
        original_title = response.css('li.ipc-metadata-list__item:contains("Also known as") span.ipc-metadata-list-item__list-content-item::text').getall()
        score = response.css("span.iZlgcd::text").get()
        genre = response.css('a.ipc-chip--on-baseAlt span.ipc-chip__text::text').getall()
        year = response.css('ul.sc-afe43def-4 li.ipc-inline-list__item a.ipc-link--inherit-color::text').get()
        time = response.css('ul.sc-afe43def-4 li.ipc-inline-list__item::text').get()
        description = response.css('span.sc-5f699a2-0::text').get()
        actor = list(set(response.css('li.ipc-metadata-list__item:contains("Stars") li.ipc-inline-list__item a.ipc-metadata-list-item__list-content-item--link::text').getall()))
        public = response.css('ul.sc-afe43def-4 li.ipc-inline-list__item a.ipc-link--inherit-color::text').getall()[-1]
        country = response.css('li.ipc-metadata-list__item[data-testid="title-details-origin"] a.ipc-metadata-list-item__list-content-item--link::text').getall()
      
        top_movies_items = TopMovieItem()
        
        top_movies_items['title'] = title
        top_movies_items['original_title'] = original_title
        top_movies_items['score'] = score
        top_movies_items['genre'] = genre
        top_movies_items['year'] = year
        top_movies_items['time'] = time
        top_movies_items['description'] = description
        top_movies_items['actor'] = actor
        top_movies_items['public'] = public
        top_movies_items['country'] = country        
            
        yield top_movies_items