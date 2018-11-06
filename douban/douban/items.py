# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    moviename=scrapy.Field()#电影名字
    moviebd=scrapy.Field()#电影主演
    moviestar=scrapy.Field()#电影评分
    movieimg=scrapy.Field()#电影图片

