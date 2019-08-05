# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxhh.items import WxhhItem


class WexhSpider(CrawlSpider):
    name = 'wexh'
    allowed_domains = ['weixinqn.com']
    start_urls = ['http://www.weixinqn.com/weixin-index-id-48-p-1.html']
    #http://www.weixinqn.com/weixin-index-id-48-p-1.html
    rules = (
        Rule(LinkExtractor(allow=r'.+weixin-index-id-48-p-\d.html'), follow=True),
        Rule(LinkExtractor(allow=r'.+weixin-show-id-\d.html'), callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        # wech = response.xpath("//span[@class='des_info_text2']/text").get()
        print(response.url)


