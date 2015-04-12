# -*- coding: utf-8 -*-

# Scrapy settings for laiyifaspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

# BOT_NAME = 'laiyifaspider'

SPIDER_MODULES = ['laiyifaspider.spiders']
NEWSPIDER_MODULE = 'laiyifaspider.spiders'

FEED_URI = 'out.txt'
FEED_FORMAT = 'jsonlines'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36'
