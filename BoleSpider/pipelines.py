# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import codecs
import json
# 对item 进行清洗可设置图片处理 setting设置图片下载


class BolespiderPipeline(object):
    def process_item(self, item, spider):
        print("have return")
        return item


class ImagespathPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        image_file_value = [value["path"] for ok, value in results if ok]
        item["front_image_path"] = image_file_value
        return item


class JsonWithEncodingPipeline(object):
    # 打开json文件
    def __init__(self):
        self.file = codecs.open("article.json", "w", encoding="utf-8")

    # 写入文件
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    # 关闭文件
    def spider_close(self,spider):
        self.file.close()


