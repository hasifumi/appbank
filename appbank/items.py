# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppbankItem(scrapy.Item):
   mon_no = scrapy.Field()
   name = scrapy.Field()
   props = scrapy.Field()
   stars = scrapy.Field()
   costs = scrapy.Field()
   max_lvl = scrapy.Field()
   types = scrapy.Field()
   hp_init = scrapy.Field()
   hp_max = scrapy.Field()
   hp_plus = scrapy.Field()
   attack_init = scrapy.Field()
   attack_max = scrapy.Field()
   attack_plus = scrapy.Field()
   recovery_init = scrapy.Field()
   recovery_max = scrapy.Field()
   recovery_plus = scrapy.Field()
   skill_no = scrapy.Field()
   leader_skill_no = scrapy.Field()
   awaken_skills = scrapy.Field()
   mon_no_evolution_before = scrapy.Field()

class SkillItem(scrapy.Item):
    skill_no = scrapy.Field()
    name = scrapy.Field()
    turn_init = scrapy.Field()
    turn_max = scrapy.Field()
    level_max = scrapy.Field()
    function = scrapy.Field()

class LeaderSkillItem(scrapy.Item):
    leader_skill_no = scrapy.Field()
    name = scrapy.Field()
    function = scrapy.Field()

class AwakenSkillItem(scrapy.Item):
    awaken_skill_no = scrapy.Field()
    name = scrapy.Field()
    function = scrapy.Field()


