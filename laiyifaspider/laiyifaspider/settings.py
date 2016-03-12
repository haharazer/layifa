# -*- coding: utf-8 -*-

# Scrapy settings for laiyifaspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

# BOT_NAME = 'laiyifaspider'

DOWNLOAD_DELAY = 1

SPIDER_MODULES = ['laiyifaspider.spiders']
NEWSPIDER_MODULE = 'laiyifaspider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36'

ITEM_PIPELINES = {
    'scrapy_qiniu.QiniuPipeline' : 1,
    'laiyifaspider.pipelines.MySQLStorePipeline': 2
}
IMAGES_STORE  = ''

MYSQL_HOST = 'loaclhost'
MYSQL_DBNAME = 'youhui'
MYSQL_USER = 'bbb'
MYSQL_PASSWD = 'aaa'


PIPELINE_QINIU_ENABLED = 1
PIPELINE_QINIU_AK = 'xxx'
PIPELINE_QINIU_SK = 'yyy'
PIPELINE_QINIU_BUCKET = 'zzz'
PIPELINE_QINIU_KEY_PREFIX = 'ccc'