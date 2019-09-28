# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class DoubanbookspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'book'

    id = Field()            # id
    cover = Field()         # 封面
    name = Field()          # 书名
    Originalname = Field()  # 原作名
    author = Field()        # 作者
    publisher = Field()     # 出版社
    publishdate = Field()   # 出版日期
    pages = Field()         # 页数
    price = Field()         # 价格
    rating_num = Field()    # 评分
    rating_people = Field() # 评价人数


