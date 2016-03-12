# -*- coding: utf-8 -*-
import scrapy
import requests
import json
import time
import re

from scrapy import Request
from laiyifaspider.items import YouhuiItem, TagItem

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

    def get_item(self, response):
        res = requests.get("http://faxian.smzdm.com/json_more?timesort=" + str(int(time.time())), headers=self.headers)
        self.cookies['__jsluid'] = res.headers['set-cookie'].split(';')[0].split('=')[1]
        jsl_clearance = ''
        for cookie_part in re.findall('push\("([\w\.%\|]+)"\)', res.text):
            jsl_clearance += cookie_part
        self.cookies['__jsl_clearance'] = jsl_clearance
        res = requests.get("http://faxian.smzdm.com/json_more?timesort=" + str(int(time.time())), headers=self.headers, cookies=self.cookies)
        for item in json.loads(res.text):
            ret = YouhuiItem()
            ret['ori_pic_url'] = item['article_pic_url']
            ret['url'] = item['article_url']
            ret['title'] = item['article_title']
            ret['content'] = item['article_content']
            ret['price'] = item['article_price']
            ret['mall'] = item['article_mall']
            ret['timestamp'] = str(item['timesort'])
            ret['article_id'] = '001' + item['article_id']
            ret['ori_url'] = item['article_link']
            ret['category'] = item['article_top_category']
            ret['source'] = u'smzdm'
            ret['file_urls'] = [ret['ori_pic_url']]
            def pic_name_generator(url):
                postfix = url.split('.')[-1]
                pic_name = md5(url).hexdigest()  + '.' + postfix
                return { 'bucket': 'laiyifapic', 'key':pic_name }
            ret['qiniu_key_generator'] = pic_name_generator
            yield ret
            yield scrapy.Request(ret['url'], self.parse_detail)

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
        return [Request("http://www.baidu.com", callback=self.get_item)]




