import scrapy
from .. import items
class dcard_spider(scrapy.Spider):
    name = 'dcard_spider'

    def start_requests(self, response):
        start_URLs = 'https://www.dcard.tw/f?home=true&latest=true'
        yield scrapy.Request(start_URLs, callback=self.parse)

    def parse(self, response):
        item = items.Test1Item()
        item["content"] = response.css('PostEntry_root').extract()
        yield item