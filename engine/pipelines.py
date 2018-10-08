# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersprojectPipeline(object):
    def process_item(self, item, spider):
        return item


class GufengPipeline(object):
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        pass
