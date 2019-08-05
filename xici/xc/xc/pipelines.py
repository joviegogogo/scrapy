# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class XcPipeline(object):
    def process_item(self, item, spider):
        DBKWARGS = spider.setting.get('DBKWARGS')
        con = MySQLdb.connect(**DBKWARGS)
        cur = con.cursos()


        return item
