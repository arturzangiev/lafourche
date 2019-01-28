# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['lafourche.fr']
    start_urls = [
        'https://lafourche.fr/collections/epicerie-salee?page=1',
        'https://lafourche.fr/collections/epicerie-sucree?page=1',
        'https://lafourche.fr/collections/pains-et-petit-dejeuner?page=1',
        'https://lafourche.fr/collections/pates-riz-graines-et-cereales?page=1',
        'https://lafourche.fr/collections/vrac?page=1',
        'https://lafourche.fr/collections/boissons?page=1',
        'https://lafourche.fr/collections/produits-bebe?page=1',
        'https://lafourche.fr/collections/beaute-hygiene?page=1',
        'https://lafourche.fr/collections/entretien-et-linge?page=1',
        'https://lafourche.fr/collections/sans-gluten?page=1',
        'https://lafourche.fr/collections/vegan?page=1'
    ]

    def parse(self, response):
        urls = response.xpath('//h2[@class="productitem--title"]/a/@href').extract()
        for url in urls:
            full_url = response.urljoin(url)
            yield scrapy.Request(full_url, callback=self.individual_page)

        # Calling next page
        for page in range(2, 10):
            next_page_url = str(response.url.split('=')[0]) + "=" + str(page)
            yield scrapy.Request(url=next_page_url)

    def individual_page(self, response):
        fields = dict()
        fields["base_price"] = response.xpath('//div[@class="price--compare-at visible"]/span/text()').re_first('(\d+\,\d+)')
        fields["discounted_price"] = response.xpath('//div[@class="price--main"]/span/text()').re_first('(\d+\,\d+)')
        fields["product_name"] = response.xpath('//h1[@class="product-title"]/text()').extract_first().strip()
        fields["category"] = response.url.split("/")[4]
        fields["brand"] = response.xpath('//div[@class="product-vendor"]/text()').extract_first().strip()
        fields["description"] = response.xpath('//meta[@property="og:description"]/@content').extract_first()

        yield fields