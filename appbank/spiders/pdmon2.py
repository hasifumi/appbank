# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from appbank.items import AppbankItem


class Pdmon2Spider(CrawlSpider):
    name = 'pdmon2'
    allowed_domains = ['pd.appbank.net']
    start_urls = ['http://pd.appbank.net/ml']
    #start_urls = ['http://pd.appbank.net/ml23']
    #start_urls = ['http://pd.appbank.net/ml24']
    #start_urls = ['http://pd.appbank.net/ml14']

    rules = (
        #Rule(LinkExtractor(allow=r'/m\d\d\d$'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'/m23\d\d'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'/m1325'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/m\d'), callback='parse_item', follow=True),
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

        table_data = response.css('div#monster div.space table tr td::text').extract()
        print table_data
        hp_init       = table_data[6].replace(",","")  if table_data[6].replace(",","").isdigit() else 0
        attack_init   = table_data[7].replace(",","")  if table_data[7].replace(",","").isdigit() else 0
        recovery_init = table_data[8].replace(",","")  if table_data[8].replace(",","").isdigit() else 0
        hp_max        = table_data[11].replace(",","") if table_data[11].replace(",","").isdigit() else 0
        attack_max    = table_data[12].replace(",","") if table_data[12].replace(",","").isdigit() else 0
        recovery_max  = table_data[13].replace(",","") if table_data[13].replace(",","").isdigit() else 0
        hp_plus       = table_data[16].replace(",","") if ( len(table_data) >15 and table_data[16].replace(",","").isdigit()) else 0
        attack_plus   = table_data[17].replace(",","") if ( len(table_data) >15 and table_data[17].replace(",","").isdigit()) else 0
        recovery_plus = table_data[18].replace(",","") if ( len(table_data) >15 and table_data[18].replace(",","").isdigit()) else 0

        skill_no = response.css('div#monster p.skill-name a[href*=skill]::attr(href)').extract()
        skill_no = self.format_etc(skill_no[0]) if len(skill_no) > 0 else None

        leader_skill_no = response.css('div#monster p.skill-name a[href*=leader]::attr(href)').extract()
        leader_skill_no = self.format_etc(leader_skill_no[0]) if len(leader_skill_no) > 0 else None

        awakens = response.css('div#monster p.skill-name a[href*=kakusei]::attr(href)').extract()
        awaken_skills = []
        for i in awakens:
            awaken_skills.append(self.format_etc(i))

        mon_no_evolution_before = response.css('div#monster div.evo-monster a::attr(href)').extract()
        mon_no_evolution_before = self.format_etc(mon_no_evolution_before[0]) if len(mon_no_evolution_before) > 0 else None

	item = AppbankItem(
                mon_no = mon_no,
                name = name,
                props = props,
                types = types,
                stars = stars,
                costs = costs,
                skill_no = skill_no,
                leader_skill_no = leader_skill_no,
                awaken_skills = awaken_skills,
                mon_no_evolution_before = mon_no_evolution_before,
                hp_init = hp_init,
                hp_max = hp_max,
                hp_plus = hp_plus,
                attack_init = attack_init,
                attack_max = attack_max,
                attack_plus = attack_plus,
                recovery_init = recovery_init,
                recovery_max = recovery_max,
                recovery_plus = recovery_plus,
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

    def format_etc(self, etc):
        regex = u'([\d]+)'
        match = re.search(regex, etc, re.U)
        return match.group()

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
#   awaken_skills = scrapy.Field()
#   mon_no_evolution_before = scrapy.Field()
