# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from huwen.items import HuwenItem

class HwenSpider(CrawlSpider):
    name = 'hwen'
    allowed_domains = ['pzzxyx.com']
    start_urls = ['http://pzzxyx.com/art-type-id-16-pg-1.html']

    rules = (
        Rule(LinkExtractor(allow=r'.+/art-type-id-16-pg-\d.html'),follow=True),
        Rule(LinkExtractor(allow=r'.+/art-detail-id-.+-pg-.html'),callback='parse_item',follow=False)
    )
    def parse_item(self, response):
        title = response.xpath("//div[@class='ming']/text()").extract()
        wen = response.xpath("//div[@class='news']//text()").extract()
        wen = "".join(wen).strip("\r\n")
        item = HuwenItem(title=title,wen=wen)
        yield item




