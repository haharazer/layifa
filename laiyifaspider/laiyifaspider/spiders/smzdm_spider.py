#coding=utf-8
import scrapy
import requests
import json
import time
import re

from scrapy import Request
from laiyifaspider.items import YouhuiItem

import urllib
from hashlib import md5

class SmzdmSpider(scrapy.Spider):
    name = "smzdm"
    start_urls = ['http://faxian.smzdm.com']

    cookies = {
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "faxian.smzdm.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36"
    }
    picdir = './pics/'

    def get_item(self, response):
        res = requests.get("http://faxian.smzdm.com/json_more?timesort=" + str(int(time.time())), headers=self.headers)
        self.cookies['__jsluid'] = res.headers['set-cookie'].split(';')[0].split('=')[1]
        jsl_clearance = ''
        for cookie_part in re.findall('push\("([\w\.%\|]+)"\)', res.text):
            jsl_clearance += cookie_part
        self.cookies['__jsl_clearance'] = jsl_clearance
        res = requests.get("http://faxian.smzdm.com/json_more?timesort=" + str(int(time.time())), headers=self.headers, cookies=self.cookies)
        for item in json.loads(res.text):
            #下载图片
            img = item['article_pic_url']
            m = md5()
            m.update(img)
            postfix = img.split('.')[-1]
            filename = m.hexdigest()  + '.' + postfix
            urllib.urlretrieve(img, self.picdir + filename)

            ret = YouhuiItem()
            ret['img'] = item['article_pic_url']
            ret['url'] = item['article_url']
            ret['title'] = item['article_title']
            ret['content'] = item['article_content']
            ret['price'] = item['article_price']
            ret['mall'] = item['article_mall']
            ret['timestamp'] = item['timesort']
            ret['articleid'] = '001' + item['article_id']
            ret['link'] = item['article_link']
            ret['category'] = item['article_top_category']
            ret['picfile'] = filename
            yield ret

    def start_requests(self):
        return [Request("http://www.baidu.com", callback=self.get_item)]
