# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import ArticleItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//h1[@class="title"]/text()').get()
        avatar = response.xpath('//a[@class="avatar"]/img/@src').get()
        author = response.xpath('//span[@class="name"]/a/text()').get()
        pub_time = response.xpath('//span[@class="publish-time"]/text()').get().replace("*","")
        url = response.url
        url1 = url.split("?")[0]
        article_id = url1.split('/')[-1]
        content = response.xpath("//div[@class='show-content-free']").get()
        item = ArticleItem(title=title,avatar=avatar,pub_time=pub_time,origin_url=response.url,article_id=article_id,author=author,content=content)
        yield item






