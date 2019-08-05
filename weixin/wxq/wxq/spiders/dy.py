# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxq.items import WxqItem

class DySpider(CrawlSpider):
    name = 'dy'
    allowed_domains = ['www.jinnianduoda.com']
    start_urls = ['http://www.jinnianduoda.com/list/194-0-0.html']

    rules = (
        Rule(LinkExtractor(allow=r'.+/list/194-0-\d.html'),follow=True),
        Rule(LinkExtractor(allow=r'.+/group/.+.html'),callback = 'parse_item',follow=False)
    )

    def parse_item(self, response):
        title = response.xpath("//div[@class='code_info']/h1//text()").get()
        wxh = response.xpath("//div[@class='green_bg']/p[1]/span[@class='bold']/text()").get()
        item = WxqItem(title=title,wxh=wxh)
        yield item
        print(item)
        # print(response.urls)
