# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from appbank.items import SkillItem

class PdSkillSpider(CrawlSpider):
    name = 'pdskill'
    allowed_domains = ['pd.appbank.net']
    start_urls = ['http://pd.appbank.net/skill/list']

    rules = (
        Rule(LinkExtractor(allow=r'/[\d]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        regex = u'skill/(\d+)'
        match = re.search(regex, response.url, re.U)
        skill_no = match.group(1)

        #name = response.css('div#skill div.space p.skill-name::text').extract()
        res = response.css('div#skill div.space p::text').extract()
        print res
        name = res[0]

        #regex = u'Lv.(\d+).*Lv.(\d+)'
        regex = u'Lv.1\uff1a(\d+).*Lv.(\d+)'
        match = re.search(regex, res[1], re.U)
        turn_init = match.group(1)
        level_max = match.group(2)
        #turn_max = turn_init - level_max + 1

        function = res[2]

        item = SkillItem(
                skill_no = skill_no,
                name = name,
                turn_init = turn_init,
                level_max = level_max,
                turn_max = int(turn_init) - int(level_max) + 1,
                function = function,
        )
        return item

