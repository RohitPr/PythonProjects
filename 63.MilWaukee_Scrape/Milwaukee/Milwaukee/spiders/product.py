import scrapy
import json


class ProductSpider(scrapy.Spider):
    name = "product"
    product_url = []
    base_url = "https://www.milwaukeetool.com/Products/"
    with open("data.json", encoding="utf8") as data_file:
        data = json.load(data_file)
        for a in data:
            skucode = a["Sku"]
            product_url.append(base_url + skucode)
    start_urls = [a for a in product_url]

    def parse(self, response):
        url = "https://www.milwaukeetool.com/"
        feature = response.css("div.product-features li::text").getall()
        feature_data = "|".join(feature)
        features = feature_data.replace("	", "")
        specs_data = response.css("div.product-specs__row span::text").getall()
        if len(specs_data) < 1:
            specs_data_key = response.css("dl.tech-specs dt::text").getall()
            specs_data_value = response.css("dl.tech-specs dd::text").getall()
            specs = {
                specs_data_key[i]: specs_data_value[i]
                for i in range(0, len(specs_data_key))
            }
        else:
            specs = {
                specs_data[i]: specs_data[i + 1] for i in range(0, len(specs_data), 2)
            }
        main_image = response.css("div.media-gallery__thumb::attr(data-main)").getall()
        thumbnail = response.css("div.media-gallery__thumb-inn img::attr(src)").getall()
        video_data = response.css(
            "div.media-gallery__thumb-video::attr(data-main)"
        ).extract()
        video_str = "".join(video_data)
        if len(video_str) > 1:
            video = url + video_str
        else:
            video = ""
        images = []
        for a in range(len(main_image)):
            images.append(
                {
                    "Item_Image": url + str(thumbnail[a]),
                    "Detailed_Image": url + str(main_image[a]),
                    "Zoom_Image": url + str(main_image[a]),
                }
            )

        include = response.css("span.product-include__title::text").getall()
        include_data = "|".join(include)
        includes = include_data.replace("												", "")
        yield {
            "URL": response.xpath("//meta[@property='og:url']/@content")[0].extract(),
            "Category": response.xpath("//meta[@property='og:url']/@content")[0]
            .extract()
            .split("/")[4],
            "Sub Category": response.xpath("//meta[@property='og:url']/@content")[0]
            .extract()
            .split("/")[5],
            "Breadcrumb": response.xpath("//meta[@property='og:url']/@content")[0]
            .extract()
            .split(".com/")[1],
            "Title": response.css("title::text").get(),
            "Brand": "Milwaukee Tool",
            "Manufacturer": "Milwaukee Tool",
            "Country": "US",
            "Product SKU": response.xpath("//meta[@property='og:url']/@content")[0]
            .extract()
            .split("/")[-1],
            "Short_Description": response.xpath('/html/head/meta[5]/@content').extract(),
            "Long_Description": response.css(
                "div.product-info__overview p::text"
            ).get(),
            "Features": features,
            "Includes": includes,
            "Specifications": specs,
            "Images": images,
            "Videos": video,
        }
