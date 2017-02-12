# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CraigslistRental(scrapy.Item):
    cl_id = scrapy.Field()
    price = scrapy.Field()
