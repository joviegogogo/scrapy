# -*- coding: utf-8 -*-
import scrapy
from dd.items import DdItem
from scrapy.http import Request

class DangdangSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['http://www.resgain.net']
    start_urls = ['http://www.resgain.net/esite/index.rhtml?id={}'.format(num) for num in range(100000, 999999)]

    def parse(self, response):
        item = DdItem()
        item['title'] = response.xpath("//ol[@class='breadcrumb']/li/text()").get()
        #
        #
        yield item
























    # allowed_domains = ['http://category.dangdang.com']
    # start_urls = ['http://category.dangdang.com/pg{}-cid4002385.html'.format(num) for num in range(2,20)]

    # def parse(self, response):
    #     item = DdItem()
    #     item['title'] = response.xpath("//a[@name='itemlist-shop-name']/text()").get()
    #     # item['link'] = response.xpath("//a[@name='itemlist-shop-name']/@href").extract()
    #     # item['comment'] = response.xpath("//a[@name='itemlist-review']/text()").extract()
    #     # print(item['title'])
    #     yield item
        # for i in range(2,21):
        #     url = 'http://search.dangdang.com/?key=%CA%D6%BB%FA&act=input&page_index='+str(i)
        #     yield Request(url,callback=self.parse)






        # title = ''.join(title).strip('当当自营')
        # item['link'] = response.xpath("//a[@name='itemlist-shop-name']/@href").extract()
        # item['comment'] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        # print(item['title'])
        # item = DdItem(title=title)
        # yield item
        # for i in range(2,21):
        #     url = 'http://search.dangdang.com/?key=%CA%D6%BB%FA&act=input&page_index='+str(i)
        #     yield Request(url,callback=self.parse)

