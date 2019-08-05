# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from huangtu.items import HuangtuItem
from scrapy import Request

class DySpider(CrawlSpider):
    name = 'dy'
    allowed_domains = ['www.hhhgmmg.com']
    start_urls = ['http://www.hhhgmmg.com/newslist/40/index-1.html']

    rules = (
        #匹配每一页的网址d{}正则表达式匹配
        Rule(LinkExtractor(allow=r'.+/newslist/40/index-\d.html'), follow=True),
        #匹配每一页的url正则匹配进去提取出来
        Rule(LinkExtractor(allow=r'.+/news/\d{1,5}.html'),callback='parse_item',follow=False)
    )
    # http://www.hhhgmmg.com/news/3958.html

    def parse_item(self, response):
        item = HuangtuItem()
        item['title'] = response.xpath("//div[@class='title']/text()").extract_first()
        item['img_url'] = response.xpath("//div[@class='n_bd']/img/@src").extract()
        yield item
        # print(item['title'],item['img_url'])
        #  title 标题的匹配 title xpath匹配
        # img_url 每一个url的匹配










