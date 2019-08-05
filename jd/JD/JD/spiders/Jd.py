# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JdSpider(CrawlSpider):
    name = 'Jd'
    allowed_domains = ['item.jd.com']
    start_urls = ['https://item.jd.com/29967331748.html']

    rules = (
        Rule(LinkExtractor(allow=r'.+/\d{1,11}.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        print(response.url)
