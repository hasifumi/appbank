# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from appbank.items import AppbankItem


class Pdmon2Spider(CrawlSpider):
    name = 'pdmon2'
    allowed_domains = ['pd.appbank.net']
    #start_urls = ['http://pd.appbank.net/ml1']
    start_urls = ['http://pd.appbank.net/ml23']

    rules = (
        #Rule(LinkExtractor(allow=r'/m\d\d\d$'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/m226\d'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'/m\d\d\d.php'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
	#title = response.css('h3::text').extract_first()
	#item = AppbankItem(title=title)
        name = response.css('div#monster h3.title-pattern-darkblue::text').extract_first()
        #stars = response.css('div#monster div.detail p.icon-attr::text').extract()
        props = response.css('div#monster div.detail p.icon-attr i[class*=icon]::attr(class)').extract()
        types = response.css('div#monster div.detail p.icon-mtype i[class*=icon-mtype]::attr(class)').extract()
	item = AppbankItem(
                name = name,
                main_prop = props,
                main_type = types,
        )
                #stars=stars,
	return item
