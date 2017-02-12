# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CraigslistRental(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cl_id = scrapy.Field()
    price = scrapy.Field()
