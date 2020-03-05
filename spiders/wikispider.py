from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class WikiSpider(CrawlSpider):
    name = "WikiSpider"
    allowed_domains = ['en.wikipedia.com']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia']
    base_url = 'https://en.wikipedia.org/wiki/Wikipedia'
    rules = [
            Rule(
                LinkExtractor(allow='wiki/'),
                follow=True
                )
            ]

    def parse(self, response):
        print(f'Reached {response.url}.')
        yield {
                'Title': response.css('h1.firstHeading::text').get()
              }
