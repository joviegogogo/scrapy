# -*- coding: utf-8 -*-
import scrapy


class RenrenloginSpider(scrapy.Spider):
    name = 'renrenlogin'
    allowed_domains = ['renrne.com']
    start_urls = ['http://renrne.com/']

    def start_requests(self):
        url = 'http://www.renren.com/SysHome.do'
        data = {
            "email":'',
            "password":""
        }
        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request

    def parse_page(self,response):
        with open('renren.html','w',encoding='utf-8')as fp:
            fp.write(response.text)
