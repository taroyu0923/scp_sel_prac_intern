import scrapy


class My_spider1(scrapy.spider):
    name = 'myspider1'    

    def start_requests(self, response):
        start_URLs = [
        'https://www.dcard.tw/f',
        'https://www.dcard.tw/f?home=true&latest=true'
        ]
        for url in start_URLs:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'tests-%s.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Save file %s' % filename)
        
