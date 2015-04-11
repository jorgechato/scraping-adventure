from twisted.internet import reactor

from scrapy import log, signals
from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings
from scrapy.xlib.pydispatch import dispatcher
import logging

from comorebajarlabarriga.spiders.base import base

def stop_reactor():
    reactor.stop()

dispatcher.connect(stop_reactor, signal=signals.spider_closed)
spider = base()
settings = get_project_settings()
crawler = Crawler(settings)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start(loglevel=logging.DEBUG)
log.msg('Running reactor...')
reactor.run()  # the script will block here until the spider is closed
log.msg('Reactor stopped.')
