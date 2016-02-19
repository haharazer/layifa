# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb.cursors
from scrapy import log


class MySQLStorePipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                                            db='youhui',
                                            user='root',
                                            passwd='123456',
                                            cursorclass=MySQLdb.cursors.DictCursor,
                                            charset='utf8',
                                            use_unicode=True,
                                            host='db',
                                            port=3306)
    def process_item(self, item, spider):
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

        return item

    def _conditional_insert(self, tx, item):
        # create record if doesn't exist.
        # all this block run on it's own thread
        tx.execute("select * from discounts where articleid = %s", (item['articleid'], ))
        result = tx.fetchone()
        if result:
            log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
        else:
            tx.execute(
                "insert into discounts (`id`, `url`, `title`, `content`, `price`, `mall`, `timestamp`, `link`, `img`, `articleid`, `category`, `picfile`) "
                "values (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (item['url'],
                 item['title'],
                 item['content'],
                 item['price'],
                 item['mall'],
                 item['timestamp'],
                 item['link'],
                 item['img'],
                 item['articleid'],
                 item['category'],
                 item['picfile'],
                )
            )
            log.msg("Item stored in db: %s" % item, level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)

