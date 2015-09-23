# -*- coding: utf-8 -*-
import re
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
        Rule(LinkExtractor(allow=r'/m226[0-2]'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'/m\d\d\d.php'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        no_and_name = response.css('div#monster h3.title-pattern-darkblue::text').extract()
        regex = u'No.(?P<num>[\d]+)\s(?P<str>.*$)'
        match = re.search(regex, no_and_name[0], re.U)
        mon_no = match.group('num')
        name = match.group('str')
        props = response.css('div#monster div.detail p.icon-attr i[class*=icon]::attr(class)').extract()
        types = response.css('div#monster div.detail p.icon-mtype i[class*=icon-mtype]::attr(class)').extract()
	item = AppbankItem(
                mon_no = mon_no,
                name = name,
                main_prop = props[0],
                sub_prop = props[1] if len(props) > 1 else "",
                main_type = types,
                sub_type = types[1] if len(types) > 1 else "",
        )
	return item
