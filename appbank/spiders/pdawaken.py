# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from appbank.items import AwakenSkillItem

class PdAwakeSpider(CrawlSpider):
    name = 'pdawaken'
    allowed_domains = ['pd.appbank.net']
    start_urls = ['http://pd.appbank.net/kakusei/list']

    rules = (
        Rule(LinkExtractor(allow=r'/\d'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        regex = u'kakusei/(\d+)'
        match = re.search(regex, response.url, re.U)
        print match.group(1)
        awaken_skill_no = match.group(1)

        name_and_function = response.css('div#skill div.space p::text').extract()
        name = name_and_function[0]
        function = name_and_function[1]

        item = AwakenSkillItem(
                awaken_skill_no = awaken_skill_no,
                name = name,
                function = function,
        )
        return item



