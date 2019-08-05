# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql


class DuanziPipeline(object):
    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host= "192.168.1.136",
            port = 3306,
            user = "root",
            password = "nofail22",
            db = "duanzi",
            charset= "utf8"
        )
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        sql = "INSERT INTO duanzi VALUES(NULL,'%s','%s')" % (item["name"],item["content"])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()
        self.cursor.close()
