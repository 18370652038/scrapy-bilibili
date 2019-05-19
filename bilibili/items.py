# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    sex = scrapy.Field()
    level = scrapy.Field()
    birthday = scrapy.Field()
    follower = scrapy.Field()
    following = scrapy.Field()
    animation = scrapy.Field()
    Life = scrapy.Field()
    Music = scrapy.Field()
    Game = scrapy.Field()
    Dance = scrapy.Field()
    Documentary = scrapy.Field()
    Ghost = scrapy.Field()
    science = scrapy.Field()
    Opera = scrapy.Field()
    entertainment = scrapy.Field()
    Movies = scrapy.Field()
    National = scrapy.Field()
    Digital = scrapy.Field()
    fashion = scrapy.Field()

    pass
