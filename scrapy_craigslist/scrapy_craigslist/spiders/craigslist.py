# -*- coding: utf-8 -*-
# from scrapy.spider import BaseSpider
# from scrapy.selector import HtmlXPathSelector
# from scrapy_craigslist.items import ScrapyCraigslistItem


class CraigslistSpider(BaseSpider):
    name = "craigslist"
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://sfbay.craigslist.org/search/sfc/apa"]

    def parse(self, response):
        response = HtmlXPathSelector(response)
        rentals = response.xpath('//li[contains(@class,"result-row")]')

        items = []

        for rental in rentals:
            item = ScrapyCraigslistItem()
            item["link"] = 'https://sfbay.craigslist.org' + rental.xpath('a[contains(@href,"/sfc")]/@href').extract()
            item["price"] = rental.xpath('a/span/text()').extract()
            items.append(item)

        return items

        # for rental in rentals:
        #     link = rental.xpath('a[contains(@href,"/sfc")]/@href').extract()
        #     price = rental.xpath('a/span/text()').extract()
        #     print link, price


        # for listing in listing_links:
        #     listing = listing
        #     for price in listing:
        #         item = ScrapyCraigslistItem
        #         items['listing'] = listing
        #         items['price'] = listings.xpath('//li[re:test(@class, "result-row")]//span[re:test(@class, "result-price")]/text()').extract()
        #         return items


        # for rental in rentals:
        #     # item = ScrapyCraigslistItem
        #     # links = rental.xpath("//li").css(".result-row a::attr(href)").extract()
        #     # for link in links:
        #     #     if link != "#":
        #     # items['listing']
        #     if rental.
        #     link = rental.xpath("//li").css(".result-row a::attr(href)").extract()
        #     # items['price']
        #     price = rental.xpath('//li[re:test(@class, "result-row")]//span[re:test(@class, "result-price")]/text()').extract()
        #     print link, price
