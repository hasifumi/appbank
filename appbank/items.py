# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppbankItem(scrapy.Item):
   #title = scrapy.Field()
   mon_no = scrapy.Field()
   name = scrapy.Field()
   main_prop = scrapy.Field()
   sub_prop = scrapy.Field()
   stars = scrapy.Field()
   costs = scrapy.Field()
   max_lvl = scrapy.Field()
   main_type = scrapy.Field()
   sub_type = scrapy.Field()
