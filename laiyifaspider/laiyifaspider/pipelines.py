# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log
from scrapy.exceptions import DropItem
from items import YouhuiItem, TagItem

import pymysql.cursors


class MySQLStorePipeline(object):
    def __init__(self, connection):
        self.connection = connection

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
        connection = pymysql.connect(**dbargs)
        return cls(connection)

    def process_item(self, item, spider):
        cursor = self.connection.cursor()
        if isinstance(item, TagItem):
            sql = "select * from discounts where article_id = %s"
            cursor.execute(sql, (item['article_id'],))
            result = cursor.fetchone()
            if result:
                cursor.execute(
                        "UPDATE `discounts` SET `tags` = %s, `tag` = %s WHERE `discounts`.`article_id` = %s; ", (
                             item['tags'],
                             item['tag'],
                             item['article_id'],
                        )
                    )
                self.connection.commit()
            else:
                raise DropItem("not found discount when add tag %s" % item)
        else:
            sql = "select * from discounts where article_id = %s"
            cursor.execute(sql, (item['article_id'],))
            result = cursor.fetchone()
            if result:
                log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
            else:
                item['pic_url'] = item['files'][0]['key']
                cursor.execute(
                    "insert into discounts (`id`, `url`, `title`, `content`, `price`, `mall`, `timestamp`, `ori_url`, `ori_pic_url`, `article_id`, `category`, `pic_url`, `source`) "
                    "values (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                         item['url'],
                         item['title'],
                         item['content'],
                         item['price'],
                         item['mall'],
                         item['timestamp'],
                         item['ori_url'],
                         item['ori_pic_url'],
                         item['article_id'],
                         item['category'],
                         item['pic_url'],
                         item['source'],
                    )
                )
                self.connection.commit()
                log.msg("Item stored in db: %s" % item, level=log.DEBUG)
        return item


