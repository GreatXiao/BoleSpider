# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BolespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BoleItem(scrapy.Item):
    title = scrapy.Field()

    # 提取url
    post_url = scrapy.Field()

    # 图片url
    front_image_url = scrapy.Field()

    front_image_path = scrapy.Field()

    # 提取日期
    creat_date = scrapy.Field()

    # 提取数字
    fav_num = scrapy.Field()

