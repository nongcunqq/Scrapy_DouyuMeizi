# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # 存放图片的url
    image_urls = scrapy.Field()
    # 存放图片的结果
    images = scrapy.Field()
