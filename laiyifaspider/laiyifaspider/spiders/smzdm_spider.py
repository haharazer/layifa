import scrapy

from scrapy import Request
from laiyifaspider.items import YouhuiItem

class SmzdmSpider(scrapy.Spider):
    name = "smzdm"
    start_urls = ['http://faxian.smzdm.com']

    cookies = {
        "smzdm_user_view": "B5689BF119765F9B7D9B74E787D05B89",
        "smzdm_user_source": "F03B74888487FC1119C3A92346201048",
        "__gads": "ID=5854ae4c60ba3d8e:T=1428828331:S=ALNI_MYq7Yt9Ay7qzIFYLx7INAxmfYblCQ",
        "PHPSESSID": "5s42bvq5s7sjtmgkh35q2d9r72",
        "_ga": "GA1.2.1732137778.1428828333",
        "__jsluid": "14cdb53a882c0e5442ed7628159e9fae",
        "__jsl_clearance": "1428836893.902|0|RHBT4z5dd4p0Oy0bwwT6j1D41dw%3d",
        "count_i": "1",
        "Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58": "1428828334",
        "Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58": "1428833305",
        "AJSTAT_ok_pages": "6",
        "AJSTAT_ok_times": "1",
        "_ga": "GA1.3.1732137778.1428828333",
        "amvid": "c2ae90dfdb6e5207f9d7fde49653f0ff"
    }

    def parse(self, response):
        item_list = response.xpath("//ul[@class='leftWrap discovery_list']/li[@class='list']")
        for item in item_list:
            ret = YouhuiItem()
            ret['img'] = item.xpath("a[@class='picBox']/img/@src").extract()
            ret['url'] = item.xpath("div[@class='listItem']/h2[@class='itemName']/a/@href").extract()
            ret['title'] = item.xpath("div[@class='listItem']/h2[@class='itemName']/a/span[@class='black']/text()").extract()
            ret['content'] = item.xpath("div[@class='listItem']/p/text()").extract()
            ret['price'] = item.xpath("div[@class='listItem']/h2[@class='itemName']/a/span[@class='red']/text()").extract()
            ret['mall'] = item.xpath("div[@class='mall']/span[@class='mall_word']/text()").extract()
            ret['timestamp'] = item.xpath("@timesort").extract()
            ret['articleid'] = item.xpath("@articleid").extract()
            ret['link'] = item.xpath("div[@class='listItem']/div[@class='item_buy_mall']/a[@class='directLink']/@href").extract()
            yield ret

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies=self.cookies)