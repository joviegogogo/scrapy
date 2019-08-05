# -*- coding: utf-8 -*-
import scrapy
from jdbook.items import JdbookItem

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=9987,653,655&page={}&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'.format(num) for num in range(1,140)]

    def parse(self, response):
         item = JdbookItem()
         title = response.xpath("//div[@class='p-name']/a/em/text()").extract()
         print(title)














# https://list.jd.com/list.html?cat=9987,653,655&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main
# https://list.jd.com/list.html?cat=9987,653,655&page=2&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=10#J_main
# https://list.jd.com/list.html?cat=9987,653,655&page=3&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main
# https://list.jd.com/list.html?cat=9987,653,655&page=4&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main
# https://list.jd.com/list.html?cat=9987,653,655&page=5&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main








