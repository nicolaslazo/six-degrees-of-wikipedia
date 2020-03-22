import re
import scrapy


class WikiSpider(scrapy.Spider):
    name = "WikiSpider"
    allowed_domains = ['en.wikipedia.org']

    custom_settings = {
        'DEPTH_LIMIT': 6,

        # Crawling order settings (BFO)
        'DEPTH_PRIORITY': 1,
        'SCHEDULER_DISK_QUEUE': 'scrapy.squeues.PickleFifoDiskQueue',
        'SCHEDULER_MEMORY_QUEUE': 'scrapy.squeues.FifoMemoryQueue',

        # Logging settings
        'LOG_LEVEL':'INFO'
    }

    def __init__(self, start_article_url='', **kwargs):
        self.start_urls = [start_article_url]
        super().__init__(**kwargs)


    def parse(self, response):
        if self.contains_blacklisted_keyword(response.url) or not self.is_valid_url(response.url):
            return

        yield {
            'Title': response.css('h1.firstHeading::text').get(),
            'URL': response.url
        }

        yield from response.follow_all(css='div.mw-content-ltr a::attr(href)')


    def is_valid_url(self, url):
        allowed_links_regex = '(https://en.wikipedia.org)?/wiki/.*'
        if re.match(allowed_links_regex, url):
            return True


    def contains_blacklisted_keyword(self, url):
        blacklisted_keywords = [
            'File:',
            'Wikipedia:',
            'Template:',
            'Talk:',
            'Portal:',
            'Help:',
            'Template_talk:',
            'Main_Page',
        ]

        return any(map(lambda keyword: keyword in url, blacklisted_keywords))
