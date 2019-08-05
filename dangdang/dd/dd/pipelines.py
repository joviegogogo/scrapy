# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# import pymysql
#
#
# class DdPipeline(object):
#     def open_spider(self,spider):
#         self.conn = pymysql.connect(
#             host= "127.0.0.1",
#             port = 3306,
#             user = "root",
#             password = "nofail22",
#             db = "title",
#             charset= "utf8"
#         )
#         self.cursor = self.conn.cursor()
#     def process_item(self, item, spider):
#         sql = "INSERT INTO title VALUES(NULL,'%s')" % (item["title"])
#         self.cursor.execute(sql)
#         self.conn.commit()
#         return item
#
#     def close_spider(self,spider):
#         self.conn.close()
#         self.cursor.close()



import pymysql.cursors
class DdPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='119.23.10.120',  # 数据库地址
            port=13306,  # 数据库端口
            db='videohongbao',  # 数据库名
            user='root',  # 数据库用户名
            passwd='751268..123',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into zf_commodity_info(commodity_name)
            value(%s)""",
            (item['title'],)) # item里面定义的字段和表字段对应
        # 提交sql语句
        self.connect.commit()
        return item  # 必须实现返回


