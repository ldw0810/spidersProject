# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GufengItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    cover = scrapy.Field()
    link = scrapy.Field()
    update_desc = scrapy.Field()
    update_time = scrapy.Field()
