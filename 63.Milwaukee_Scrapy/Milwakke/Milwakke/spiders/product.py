import scrapy


class ProductSpider(scrapy.Spider):
    name = "product"
    start_urls = ["https://www.milwaukeetool.com/Products"]

    def parse(self, response):
        for item in response.css('div.container'):
            yield{
                "ID": item.css('div.result-title__wrap::text').get(),
            }
