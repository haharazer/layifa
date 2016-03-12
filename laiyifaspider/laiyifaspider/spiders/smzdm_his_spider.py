# -*- coding: utf-8 -*-
import scrapy
import pymysql.cursors

from scrapy import Request
from laiyifaspider.items import TagItem


class SmzdmSpider(scrapy.Spider):
    name = "smzdmhis"

    def parse_detail(self, response):
        tag_divs = response.xpath("//div[@class='crumbsCate']")
        tags = []
        for div in tag_divs:
            tags.append(div.xpath("./a/span/text()").extract()[0])
        tags = tags[1:]
        item = TagItem()
        item['article_id'] = '001' + response.url.split('/')[-2]
        item['tags'] = ','.join(tags)
        item['tag'] = tags[-1]
        yield item

    def start_requests(self):
        dbargs = dict(
            host=self.settings.get('MYSQL_HOST'),
            db=self.settings.get('MYSQL_DBNAME'),
            user=self.settings.get('MYSQL_USER'),
            passwd=self.settings.get('MYSQL_PASSWD'),
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
        connection = pymysql.connect(**dbargs)
        cursor = connection.cursor()
        sql = "select * from discounts where tag_id = 0"
        cursor.execute(sql)
        result = cursor.fetchall()
        ret = []
        for item in result:
            ret.append(Request(item['url'], callback=self.parse_detail))
        return ret




