import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = "quotes_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        title = response.css('title:text').extract()
        yield {'title text' : title }
       
#dans le terminal : scrapy shell "https://www.imdb.com/chart/top/?ref_=nv_mv_250" pour scraper les donner des titres des films du site imdb