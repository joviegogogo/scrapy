# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from duanzi.items import DuanziItem
from scrapy_redis.spiders import RedisCrawlSpider

class QiushiSpider(RedisCrawlSpider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['https://www.qiushibaike.com/']
    redis_key = 'qiushi:start_urls'


    rules = (
        Rule(LinkExtractor(allow=r'/article/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/text/page/\d+/'),follow=False),
    )

    def parse_item(self, response):
        
        item = DuanziItem()
        item['name'] = response.xpath("//span/text()").extract_first()
        item['content'] = response.xpath("//div[@class='content']/text()").extract_first()
        yield item





