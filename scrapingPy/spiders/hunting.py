from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapingPy.items import ScrapingpyItem

class hunting(BaseSpider):
    name = "hunting"
    allowed_domains = ['keswickhuntclub.com',]
    start_urls = ['http://www.keswickhuntclub.com/fox-hunting/a-glossary-of-fox-hunting-terms/',]

    rules = {
        Rule(SgmlLinkExtractor(restrict_xpaths = ('//div[@id="post"]'))),
        Rule(SgmlLinkExtractor(allow = ("http://www.keswickhuntclub.com/fox-hunting/a-glossary-of-fox-hunting-terms/",)), callback = 'parse'),
    }

    def parse(self, response):
        hxs = Selector(response)
        items = []
        for section in hxs.xpath('//tr'):
            item = ScrapingpyItem()
            item ["title"] = section.xpath('.//td/text()').extract()[0]
            item ["definition"] = section.xpath('.//td/text()').extract()[1]
            items.append(item)
        return items
