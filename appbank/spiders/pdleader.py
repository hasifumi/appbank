# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from appbank.items import LeaderSkillItem

class PdLeaderSpider(CrawlSpider):
    name = 'pdleader'
    allowed_domains = ['pd.appbank.net']
    start_urls = ['http://pd.appbank.net/leader/list']

    rules = (
        Rule(LinkExtractor(allow=r'/100[\d]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        regex = u'leader/(\d+)'
        match = re.search(regex, response.url, re.U)
        leader_skill_no = match.group(1)

        name_and_function = response.css('div#skill div.space p::text').extract()
        name = name_and_function[0]
        function = name_and_function[1]

        item = LeaderSkillItem(
                leader_skill_no = leader_skill_no,
                name = name,
                function = function,
        )
        return item
