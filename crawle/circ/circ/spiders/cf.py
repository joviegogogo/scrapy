# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from circ.items import CircItem

class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['www.92yyy.com']
    start_urls = ['http://www.92yyy.com/?m=art-type-id-1-pg-2.html']

    rules = (Rule(LinkExtractor(allow=r'.+/\?m=art-type-id-2-pg-\d{1,3}.html'),follow=True ),
             Rule(LinkExtractor(allow=r'.+/\?m=art-detail-id-\d{1,6}.html'),callback="parse_item",follow=False)
    )

    def parse_item(self, response):
        title = response.xpath("//div[@class='page_title']/text()").extract()
        img_urls = response.xpath("//div[@class='content']/img/@src").extract()
        print(title,img_urls)
        item = CircItem(title=title, img_urls=img_urls)
        yield item






