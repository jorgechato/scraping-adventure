# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
import csv
import os

class ComorebajarlabarrigaPipeline(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        nodes = open(os.path.expanduser('~/Desktop/Posts_%s.csv' % spider.name), 'w+b')
        self.files[spider] = nodes
        self.exporter1 = CsvItemExporter(nodes, fields_to_export=['TITULO','FECHA','CATEGORIA','TAGS'])
        self.exporter1.start_exporting()

        self.edges = []
        self.edges.append(['TITULO','FECHA','CATEGORIA','TAGS'])
        self.num = 1

    def spider_closed(self, spider):
        self.exporter1.finish_exporting()
        file = self.files.pop(spider)
        file.close()

        writeCsvFile(getcwd()+r'\edges.csv', self.edges)

    def process_item(self, item, spider):
        self.exporter1.export_item(item)
        return item
