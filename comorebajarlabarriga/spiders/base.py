from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from comorebajarlabarriga.items import ComorebajarlabarrigaItem

class base(BaseSpider):
    name = "base"
    allowed_domains = ['comorebajarlabarriga.com',]
    start_urls = ['http://comorebajarlabarriga.com/category/alimentos-para-adelgazar-barriga/',
    'http://comorebajarlabarriga.com/category/como-adelgazar-barriga/',
    'http://comorebajarlabarriga.com/category/como-rebajar-la-barriga/',
    'http://comorebajarlabarriga.com/category/dietas/',
    'http://comorebajarlabarriga.com/category/ejercicios/',
    'http://comorebajarlabarriga.com/category/incinerador-de-grasa-2/',
    'http://comorebajarlabarriga.com/category/rebajar-la-barriga/',
    'http://comorebajarlabarriga.com/category/recetas/',
    'http://comorebajarlabarriga.com/category/recetas-para-adelgazar-el-abdomen/',
    'http://comorebajarlabarriga.com/category/rutinas-para-abdomen-plano/',
    'http://comorebajarlabarriga.com/category/video-gratis/',
    'http://comorebajarlabarriga.com/category/vientre-plano-2/',]

    rules = (
        Rule(SgmlLinkExtractor(allow = ['http://comorebajarlabarriga.com/category/alimentos-para-adelgazar-barriga/',
        'http://comorebajarlabarriga.com/category/como-adelgazar-barriga/',
        'http://comorebajarlabarriga.com/category/como-rebajar-la-barriga/',
        'http://comorebajarlabarriga.com/category/dietas/',
        'http://comorebajarlabarriga.com/category/ejercicios/',
        'http://comorebajarlabarriga.com/category/incinerador-de-grasa-2/',
        'http://comorebajarlabarriga.com/category/rebajar-la-barriga/',
        'http://comorebajarlabarriga.com/category/recetas/',
        'http://comorebajarlabarriga.com/category/recetas-para-adelgazar-el-abdomen/',
        'http://comorebajarlabarriga.com/category/rutinas-para-abdomen-plano/',
        'http://comorebajarlabarriga.com/category/video-gratis/',
        'http://comorebajarlabarriga.com/category/vientre-plano-2/',], restrict_xpaths=('//div[@id="content"]')), callback = 'parse'),
    )

    def parse(self, response):
        hxs = Selector(response)
        items = []
        for section in hxs.xpath('//div[@id="content"]//div'):
            item = ComorebajarlabarrigaItem()

            title = section.xpath('.//h2[@class="entry-title"]//a/text()').extract()
            if len(title) == 1:
                item ["TITULO"] = title
                item ["FECHA"] = section.xpath('.//div[@class="post-info"]//span[@class="date published time"]/@title').extract()
                item ["CATEGORIA"] = section.xpath('.//div[@class="post-meta"]//span[@class="categories"]//a/text()').extract()
                item ["TAGS"] = section.xpath('.//div[@class="post-meta"]//span[@class="tags"]//a/text()').extract()
                items.append(item)

        return items
