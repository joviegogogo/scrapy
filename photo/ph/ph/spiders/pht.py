# -*- coding: utf-8 -*-
import scrapy
from ph.items import PhItem
import logging
import requests

class PhtSpider(scrapy.Spider):
    name = 'pht'
    allowed_domains = ['www.jd.com']
    start_urls = ['https://item.jd.com/{}.html'.format(num) for num in range(1,300)]

    # 29967331748

    def parse(self, response):
        # title = response.xpath("//div[@class='classList']//li/a/text()")
        print(response.url)



