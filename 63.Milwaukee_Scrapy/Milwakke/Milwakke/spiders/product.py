from os import scandir
import scrapy
import json


class ProductSpider(scrapy.Spider):
    name = "product"
    product_url = []
    base_url = "https://www.milwaukeetool.com/Products"
    with open("data.json", encoding="utf8") as data_file:
        data = json.load(data_file)
        for a in data:
            skucode = a["Sku"]
            product_url.append(base_url+"/"+skucode)
    start_urls = [a for a in product_url]

    def parse(self, response):
        yield{
            "Product_ID": response.css("span.tab__title::text").get(),
            "Title": response.css("h1.product-info__title::text").get(),
            "Product_description": response.css("div.product-info__overview p::text").get(),
            "Includes": response.css("div.product-includes span::text").getall(),
            "Images": response.css("div.media-gallery img::attr(src)").getall(),
            "Features": response.css("div.product-features li::text").getall(),
            "Specifications": response.css("div.product-specs__row span::text").getall(),
            "Reviews": response.css("div.bv-inline-form-container::text"),
        }
