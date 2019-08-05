# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yihao.items import YihaoItem


class YhdSpider(CrawlSpider):
    name = 'yhd'
    allowed_domains = ['www.yhd.com']
    start_urls = ['https://search.yhd.com/c0-0/mbname-b/a-s0-v4-p1-price-d0-f0b-m1-rt0-pid-mid0-color-size-k%E7%94%B5%E8%84%91/#page=1&sort=0']

    rules = (
        Rule(LinkExtractor(allow=r'https://search.yhd.com/c0-0/mbname-b/a-s0-v4-p1-price-d0-f0b-m1-rt0-pid-mid0-color-size-k%E7%94%B5%E8%84%91/#page=1&sort=0'),follow=True),
        Rule(LinkExtractor(allow=r'https://item.yhd.com/10000\d.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = YihaoItem()
        print(response.url)

        return item
