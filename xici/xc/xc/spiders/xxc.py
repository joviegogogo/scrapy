# -*- coding: utf-8 -*-
import scrapy
from xc.items import XcItem

class XxcSpider(scrapy.Spider):
    name = 'xxc'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/']

    def start_requests(self):
        reqs=[]
        for i in range(1,3668):
            req = scrapy.Request('https://www.xicidaili.com/nn/%s'%i)
            reqs.append(req)
        return reqs

    def parse(self, response):
        ip_list = response.xpath('//table[@id="ip_list"]')
        trs = ip_list[0].xpath('tr')
        items=[]
        #
        for ip in trs[1:]:
            pre_item = XcItem()
            pre_item['IP'] = ip.xpath("td[2]/text()")[0].extract()
            pre_item['PORT'] = ip.xpath("td[3]/text()")[0].extract()
            pre_item['POSITION'] = ip.xpath('string(td[4])')[0].extract().strip()
            pre_item['TYPE'] = ip.xpath('td[6]/text()')[0].extract()
            items.append(pre_item)

        return items
