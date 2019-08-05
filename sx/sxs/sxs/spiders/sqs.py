# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sxs.items import SxsItem
import re

class SqsSpider(CrawlSpider):
    name = 'sqs'
    allowed_domains = ['www.92yyy.com']
    start_urls = ['http://www.92yyy.com/?m=art-type-id-18-pg-2.html']

    rules = (
        Rule(LinkExtractor(allow=r'.+//?m=art-type-id-18-pg-\d.html'),follow=True),
        Rule(LinkExtractor(allow=r'.+//?m=art-detail-id-.+\.html'),callback="parse_item",follow=False),
    )

    def parse_item(self, response):
        title = response.xpath("//div[@class='page_title']/text()").get()
        # title = response.xpath("//div[@class='content']/h1/text()").get()
        wen = response.xpath("//div[@class='content']").extract()
        wen = " ".join(wen).strip('<div class=\"content\">').strip('\n').strip('\t').strip('\n').strip('\t').strip('')
        print(wen)
        item = SxsItem(title=title,wen=wen)
        yield item





