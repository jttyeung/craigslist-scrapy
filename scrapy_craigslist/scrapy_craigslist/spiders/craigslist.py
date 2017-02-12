# -*- coding: utf-8 -*-
from scrapy.spiders import Spider, Request
from scrapy.selector import Selector
# from scrapy_craigslist.items import CraigslistRental


class CraigslistSpider(Spider):
    name = 'craigslist'

    allowed_domains = ['https://craigslist.org']
    start_urls = ['https://sfbay.craigslist.org/search/sfc/apa']


    def parse(self, response):
        rentals = response.xpath('//li[contains(@class,"result-row")]')

        item = CraigslistRental()
        # items = {}

        for rental in rentals:
            cl_id = rental.xpath('a[contains(@href,"/sfc")]/@href').extract()
            price = rental.xpath('a/span/text()').extract()

            yield {
                'id': cl_id,
                'price': price
            }

        # Follows subsequent listing pages
        # next_page = response.xpath('//a[contains(@class, "button next")]/@href').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield Request(next_page, callback=self.parse)
