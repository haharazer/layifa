import scrapy
import requests
import json
import time

from scrapy import Request
from laiyifaspider.items import YouhuiItem

class SmzdmSpider(scrapy.Spider):
    name = "smzdm"
    start_urls = ['http://faxian.smzdm.com']

    cookies = {
        "__jsluid": "5831b7336acb86e8ebfe7f409be3b97b",
        "__jsl_clearance": "1429111179.257|0|rtOoffPFrCvcxSCSJEoD1BQfVts%3d"
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
        res = requests.get("http://faxian.smzdm.com/json_more?timesort=" + str(int(time.time())), cookies=self.cookies, headers=self.headers)
        for item in json.loads(res.text):
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
            yield ret

    def start_requests(self):
        return [Request("http://www.baidu.com", callback=self.get_item)]
