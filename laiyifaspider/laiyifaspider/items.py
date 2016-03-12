# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YouhuiItem(scrapy.Item):
    # define the fields for your item here like:
    ori_pic_url = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    price = scrapy.Field()
    mall = scrapy.Field()
    timestamp = scrapy.Field()
    ori_url = scrapy.Field()
    article_id = scrapy.Field()
    category = scrapy.Field()
    pic_url = scrapy.Field()
    source = scrapy.Field()
    # for image pipline
    file_urls = scrapy.Field()
    files = scrapy.Field()
    qiniu_key_generator = scrapy.Field()
    pass

class TagItem(scrapy.Item):
    article_id = scrapy.Field()
    tag = scrapy.Field()
    tags = scrapy.Field()