import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class WikiSpider(scrapy.Spider):
    name = "WikiSpider"
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia']

    def parse(self, response):
        print(f'/\/\/\/\/\/\/\[WIKISPIDER] Reached {response.url}.')

        allowed_links_regex = '(https://en.wikipedia.org)?/wiki/.*'
        if not re.match(allowed_links_regex, response.url):
            print(f'/\/\/\/\/\/\/\[WIKISPIDER] ABANDONED {response.url}')
            # return

        yield {
                'Title': response.css('h1.firstHeading::text').get()
              }

        yield from response.follow_all(css='div.mw-content-ltr a::attr(href)')
