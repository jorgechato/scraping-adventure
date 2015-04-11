from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapingPy.items import ScrapingpyItem

class diving(BaseSpider):
    name = "diving"
    allowed_domains = ['scubadoctor.com.au',]
    start_urls = ['https://www.scubadoctor.com.au/scuba-diving-glossary.htm',]

    rules = {
        Rule(SgmlLinkExtractor(restrict_xpaths = ('//div[@id="content"]'))),
        Rule(SgmlLinkExtractor(allow = ("https://www.scubadoctor.com.au/scuba-diving-glossary.htm",)), callback = 'parse'),
    }

    def parse(self, response):
        hxs = Selector(response)
        items = []
        title = []
        description = []
        for section in hxs.xpath('//dl'):
            title = section.xpath('.//dt/text()').extract()
            description = section.xpath('.//dd/text()').extract()
        for index in range(len(title)):
            item = ScrapingpyItem()
            item ["title"] = title[index]
            item ["definition"] = description[index]
            items.append(item)
        return items
