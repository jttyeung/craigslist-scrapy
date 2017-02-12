# -*- coding: utf-8 -*-
from scrapy.spiders import Spider, Request
from scrapy_craigslist.items import CraigslistRental


class CraigslistSpider(Spider):
    name = 'craigslist'

    allowed_domains = ['https://craigslist.org']
    start_urls = ['https://sfbay.craigslist.org/search/sfc/apa']


    def parse(self, response):
        rentals = response.xpath('//li[contains(@class,"result-row")]')

        item = CraigslistRental()

        for rental in rentals:
            item['cl_id'] = rental.xpath('a[contains(@href,"/sfc")]/@href').extract()
            item['price'] = rental.xpath('a/span/text()').extract()

            yield item


        # Follows subsequent listing pages
        # next_page = response.xpath('//a[contains(@class, "button next")]/@href').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield Request(next_page, callback=self.parse)
