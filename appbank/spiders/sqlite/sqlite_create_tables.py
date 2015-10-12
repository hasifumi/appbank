# -*- coding: utf-8 -*-
import sys
import csv
import sqlite3

#dbFName = 'c:\Users\fumio\MyProject\scrapy\appbank\appbank\spiders\pdAppbank.db'

#con = sqlite3.connect(dbFName)
con = sqlite3.connect('pdAppbank.db')
con.text_factory = str

cur = con.cursor()

#cur.execute("""
#  create table skill(
#        skill_no integer,
#        name text,
#        turn_init integer,
#        level_max integer,
#        turn_max integer,
#        function text,
#        PRIMARY KEY(skill_no));
#""")

#cur.execute("""
#  create table leader(
#        leader_skill_no integer,
#        name text,
#        function text);
#""")

#cur.execute("""
#  create table awaken(
#        awaken_skill_no integer,
#        name text,
#        function text);
#""")

#cur.execute("""
#  create table monster(
#        mon_no integer,
#        name text,
#        skill_no integer,
#        leader_skill_no integer
#        );
#""")

#cur.execute("""
#  create table mon_awaken(
#        mon_no integer,
#        seq integer,
#        awaken_skill_no integer,
#        PRIMARY KEY(mon_no, seq)
#        );
#""")

cur.execute("""
  create table mon_prop(
        mon_no integer,
        seq integer,
        prop text,
        PRIMARY KEY(mon_no, seq)
        );
""")

cur.execute("""
  create table mon_type(
        mon_no integer,
        seq integer,
        type text,
        PRIMARY KEY(mon_no, seq)
        );
""")

con.commit()

con.close()


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
