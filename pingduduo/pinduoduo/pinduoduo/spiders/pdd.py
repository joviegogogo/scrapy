# -*- coding: utf-8 -*-
import scrapy
from pinduoduo.items import PinduoduoItem

class PddSpider(scrapy.Spider):
    name = 'pdd'
    allowed_domains = ['pinduoduo.com']
    start_urls = ['https://www.pinduoduo.com/home/sports/']

    def parse(self, response):
        item = PinduoduoItem()
        tit = response.xpath("//div[@class='goods-group']//text")

