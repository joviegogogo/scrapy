# -*- coding: utf-8 -*-
import scrapy
# from dazhong.items import DzItem

class DzSpider(scrapy.Spider):
    name = 'dz'
    allowed_domains = ['www.dianping.com/']
    start_urls = ['http://www.dianping.com/shenzhen/ch20/g33943p{}'.format(num) for num in range(1,50)]

    def parse(self, response):
        # item = DzItem()
        ip_title = response.xpath("//div[@id='shop-all-list']")
        # ip = ip_title[0].xpath('li')

