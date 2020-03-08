import scrapy
import re


class WikiSpider(scrapy.Spider):
    name = "WikiSpider"
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Aschegul']  # Arbitrary article placed for debugging purposes

    custom_settings = {
                        'DEPTH_LIMIT': 1,  # Depth n = n-1 degrees of separation
                        'DEPTH_PRIORITY': 10,
                          # 'LOG_LEVEL':'INFO'
                      }

    def parse(self, response):
        print(f'/\/\/\/\/\/\/\[WIKISPIDER] Reached {response.url}.')

        if self.contains_blacklisted_keyword(response.url) or not self.is_valid_url(response.url):
            print(f'/\/\/\/\/\/\/\[WIKISPIDER] ABANDONED {response.url}')
            return

        yield {
                'Title': response.css('h1.firstHeading::text').get()
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
                                    'Template talk:',
                                    '#',
                                    'Main_Page',
                               ]

        return any(map(lambda keyword: keyword in url, blacklisted_keywords))
