# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QkSpider(CrawlSpider):
    name = 'qk'
    allowed_domains = ['588ku.com']
    start_urls = ['https://588ku.com/ycpng/11938519.html']

    rules = (
        Rule(LinkExtractor(allow=r'/ycpng/\d{1,8}.html'), callback='parse_item', follow=True),
    )

    # https://588ku.com/ycpng/11938519.html

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

