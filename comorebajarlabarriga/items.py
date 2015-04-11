# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComorebajarlabarrigaItem(scrapy.Item):
    # define the fields for your item here like:
    TITULO = scrapy.Field()
    FECHA = scrapy.Field()
    CATEGORIA = scrapy.Field()
    TAGS = scrapy.Field()
    # pass
