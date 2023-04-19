from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TopSerieItem
from ..fonctions import convert_to_minutes
import scrapy


class IMDbTop250Serie(CrawlSpider):
    name = 'top_rated_tv_shows'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/toptv/']

    rules = (
        Rule(LinkExtractor(restrict_css=".titleColumn a"), callback="parse_serie"),
    )

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250', headers={
            'User-Agent': self.user_agent
        })



    def parse_serie(self, response):
        title = response.css("h1[data-testid='hero__pageTitle'] span::text").get().strip()
        original_title = response.css('li.ipc-metadata-list__item:contains("Original title") span.ipc-metadata-list-item__list-content-item::text').getall()
        score = response.css("span.iTLWoV::text").get()
        genre = response.css('a.ipc-chip--on-baseAlt span.ipc-chip__text::text').getall()
        year = response.css('ul.sc-htoDjs.kOCCPw li.ipc-inline-list__item a.ipc-link--inherit-color::text').get()
        time_dflt = response.css('ul.sc-htoDjs.kOCCPw li.ipc-inline-list__item::text').get()
        time = convert_to_minutes(time_dflt)
        storyline = response.css('span.Td8wCn::text').get()
        stars = list(set(response.css('li.ipc-metadata-list__item:contains("Stars") li.ipc-inline-list__item a.ipc-metadata-list-item__list-content-item--link::text').getall()))
        public = response.css('ul.sc-htoDjs.kOCCPw li.ipc-inline-list__item a.ipc-link--inherit-color::text').getall()[-1]
        country = response.css('li.ipc-metadata-list__item[data-testid="title-details-origin"] a.ipc-metadata-list-item__list-content-item--link::text').getall()

        top_series_items = TopSerieItem()

        top_series_items['title'] = title
        top_series_items['original_title'] = original_title
        top_series_items['score'] = score
        top_series_items['genre'] = genre
        top_series_items['year'] = year
        top_series_items['time'] = time
        top_series_items['storyline'] = storyline
        top_series_items['stars'] = stars
        top_series_items['public'] = public
        top_series_items['country'] = country

        yield top_series_items
