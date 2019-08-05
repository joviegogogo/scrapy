# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import json
import codecs

class CircPipeline(object):
    def process_item(self, item, spider):
        # if spider.name == 'cf':
        #     print(item['title'], item["photo"])
        #     import os, requests
        #     img_path = os.path.join(r"D:\cf", item['title'])
        #     if not os.path.exists(img_path):
        #         os.makedirs(img_path)
        #
        #     # 图片保存到本地
        #     from PIL import Image
        #     from io import BytesIO
        #     for photo in item['photo']:
        #         img_save = os.path.join(img_path, photo)
        #         print(img_save)
        #         res = requests.get(photo)
        #         img = Image.open(BytesIO(res.content))
        #         img.save(img_save)
         pass

