from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapingPy.items import ScrapingpyItem

class climbingdictionary(BaseSpider):
    name = "climb"
    allowed_domains = ['abc-of-rockclimbing.com',]
    start_urls = ['http://www.abc-of-rockclimbing.com/climbingdictionary.asp',]

    rules = {
        Rule(SgmlLinkExtractor(restrict_xpaths = ('//div[@class="section_body_content"]'))),
        Rule(SgmlLinkExtractor(allow = ("http://www.abc-of-rockclimbing.com/climbingdictionary.asp",)), callback = 'parse'),
    }

    def parse(self, response):
        hxs = Selector(response)
        items = []
        for section in hxs.xpath('//div[re:test(@class, "alt_row_\d$")]'):
            item = ScrapingpyItem()
            item ["title"] = section.xpath('.//h4/text()').extract()

            for des in section.xpath('.//p/text()'):
                description = des.extract()

            item ["definition"] = description
            items.append(item)
        return items
