import scrapy
# use Anaconda3 to open

class My_spider1(scrapy.Spider):
    name = 'myspider1'

    def start_requests(self, response):
        start_URLs = ['https://blog.ycombinator.com/',]
        

    def parse(self, response):
        for article in response.css('div.loop-section'):
            yield{
                'title':response.css('a.article-title::text').extract(),
                'link':response.css('a.article-title::attr("href")').extract(),
                'author':response.css('a.author::text').extract(),
                'tags':response.css('ul.post-categories > li a::text').extract()
            }
            '''
            next_page = response.css('div.nav-previous a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            '''
