# -*- coding: utf-8 -*-
import scrapy
import sys

from scrapy.http.request import Request

from engine.items import GufengItem

reload(sys)
sys.setdefaultencoding('utf-8')


class GufengSpider(scrapy.Spider):
    name = 'gufeng'
    allowed_domains = ['www.gufengmh.com']
    start_urls = ['http://www.gufengmh.com/list/click/?page=1']
    num = 0

    def parseItem(self, response):
        manhuaList = response.xpath('//li[@class="item-lg"]')
        for manhua in manhuaList:
            item = GufengItem()
            item['name'] = manhua.xpath('./a/@title').extract_first()
            item['link'] = manhua.xpath('./a/@href').extract_first()
            item['cover'] = manhua.xpath('./a/img/@src').extract_first()
            item['update_desc'] = manhua.xpath('./a/span[@class="tt"]/text()').extract_first()
            item['update_time'] = manhua.xpath('./span[@class="updateon"]/text()').extract_first().strip()
            yield item

    def parse(self, response):
        self.parseItem(response)
        total_page = int(response.xpath('//li[@class="last"]/a/@data-page').extract_first())
        for i in range(1, total_page):
            next_url = self.start_urls[0].replace("page=1", "page=" + str(i + 1))
            yield Request(url=next_url, callback=self.parseItem)
