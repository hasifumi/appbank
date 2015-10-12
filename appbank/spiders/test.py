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
    start_urls = ['http://pd.appbank.net/ml24']

    rules = (
        #Rule(LinkExtractor(allow=r'/m\d\d\d$'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/m2392'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'/m\d'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'/m\d\d\d.php'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        no_and_name = response.css('div#monster h3.title-pattern-darkblue::text').extract()
        regex = u'No.(?P<num>[\d]+)\s(?P<str>.*$)'
        match = re.search(regex, no_and_name[0], re.U)
        mon_no = match.group('num')
        name = match.group('str')

        stars_and_costs = response.css('div#monster div.detail p.icon-attr::text').extract()
        #print stars_and_costs
        strs2 = re.sub(u'\s', '', stars_and_costs[1])
        strs3 = re.split(u'\/', strs2)
        stars = strs3[1][1:2]
        costs = strs3[2][4:6]

        icon_props = response.css('div#monster div.detail p.icon-attr i[class*=icon]::attr(class)').extract()
        props = map(self.format_prop, icon_props)

        icon_types = response.css('div#monster div.detail p.icon-mtype i[class*=icon-mtype]::attr(class)').extract()
        types = map(self.format_type, icon_types)

        #leader_skill_no = response.css('div#monster p.skill-name::text').extract()
        leader_skill_no = response.css('div#monster p.skill-name a[href*=skill]::attr(href)').extract()
        print "*+*+*+*+*+*"
        print leader_skill_no
        print "*+*+*+*+*+*"

	item = AppbankItem(
                mon_no = mon_no,
                name = name,
                props = props,
                types = types,
                stars = stars,
                costs = costs,
                leader_skill_no = leader_skill_no,
        )
	return item

    def format_prop(self, prop):
        regex = u'icon-attr-(?P<prop>[\w]+)'
        match = re.search(regex, prop, re.U)
        m = match.group('prop')
        return m

    def format_type(self, type):
        regex = u'icon-mtype-(?P<type>[\w]+)'
        match = re.search(regex, type, re.U)
        m = match.group('type')
        return m


#class AppbankItem(scrapy.Item):
#   mon_no = scrapy.Field()
#   name = scrapy.Field()
#   props = scrapy.Field()
#   stars = scrapy.Field()
#   costs = scrapy.Field()
#   max_lvl = scrapy.Field()
#   types = scrapy.Field()
#   hp_init = scrapy.Field()
#   hp_max = scrapy.Field()
#   hp_plus = scrapy.Field()
#   attack_init = scrapy.Field()
#   attack_max = scrapy.Field()
#   attack_plus = scrapy.Field()
#   recovery_init = scrapy.Field()
#   recovery_max = scrapy.Field()
#   recovery_plus = scrapy.Field()
#   skill_no = scrapy.Field()
#   leader_skill_no = scrapy.Field()
#   awaked_skills = scrapy.Field()
#   mon_no_evolution_before = scrapy.Field()
