from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapingPy.items import ScrapingpyItem

class climbingdictionary(BaseSpider):
    name = "paragliding"
    allowed_domains = ['hanggliding.org',]
    start_urls = ['http://www.hanggliding.org/wiki/HG_Glossary',]

    rules = {
        Rule(SgmlLinkExtractor(restrict_xpaths = ('//div[@id="mw-content-text"]'))),
        Rule(SgmlLinkExtractor(allow = ("http://www.hanggliding.org/wiki/HG_Glossary",)), callback = 'parse'),
    }

    def parse(self, response):
        hxs = Selector(response)
        items = []
        for section in hxs.xpath('//dl'):
            item = ScrapingpyItem()
            item ["title"] = section.xpath('.//dt/text()').extract()
            item ["definition"] = section.xpath('.//dd/text()').extract()
            items.append(item)
        return items
