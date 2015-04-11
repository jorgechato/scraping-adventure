# -*- coding: utf-8 -*-

# Scrapy settings for comorebajarlabarriga project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import subprocess

BOT_NAME = 'comorebajarlabarriga'

SPIDER_MODULES = ['comorebajarlabarriga.spiders']
NEWSPIDER_MODULE = 'comorebajarlabarriga.spiders'
ITEM_PIPELINES = ['comorebajarlabarriga.pipelines.ComorebajarlabarrigaPipeline']
FEED_FORMAT = 'csv'
FEED_EXPORTERS_BASE = {
    'csv': 'scrapy.contrib.exporter.CsvItemExporter',
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'comorebajarlabarriga (+http://www.yourdomain.com)'
