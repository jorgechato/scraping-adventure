from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapingPy.items import ScrapingpyItem

class motorsport(BaseSpider):
    name = "motor"
    allowed_domains = ['parkplacemotorsports.com',]
    start_urls = ['http://www.parkplacemotorsports.com/glossary/',]

    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths = ('//ul[@class="sub-items"]'))),
        Rule(SgmlLinkExtractor(allow = ["http://www.parkplacemotorsports.com/glossary/"], restrict_xpaths=('//div[@id="mw-content-text"]')), callback = 'parse'),
    )

    def parse(self, response):
        hxs = Selector(response)
        items = []
        for section in hxs.xpath('//li'):
            item = ScrapingpyItem()
            item ["title"] = section.xpath('.//h4/text()').extract()
            item ["definition"] = section.xpath('.//div/p/text()').extract()
            items.append(item)
        return items
