# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb.cursors
from scrapy import log


class MySQLStorePipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

        return item

    def _conditional_insert(self, tx, item):
        # create record if doesn't exist.
        # all this block run on it's own thread
        tx.execute("select * from discounts where article_id = %s", (item['article_id'], ))
        result = tx.fetchone()
        if result:
            log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
        else:
            item['pic_url'] = item['files'][0]['key']
            tx.execute(
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
            log.msg("Item stored in db: %s" % item, level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)

