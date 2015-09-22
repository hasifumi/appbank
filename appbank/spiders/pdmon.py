# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from appbank.items import AppbankItem


class PdmonSpider(CrawlSpider):
    name = 'pdmon'
    allowed_domains = ['pd.appbank.net']
    start_urls = ['http://pd.appbank.net/ml1']

    rules = (
        Rule(LinkExtractor(allow=r'/m\d\d\d$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
                'title': response.css('h3::text').extract_first(),
        }

