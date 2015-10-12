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

cur.execute("""
  create table leader(
        leader_skill_no integer,
        name text,
        function text);
""")

#cur.execute("""
#  create table awaken(
#        awaken_skill_no integer,
#        name text,
#        function text);
#""")

con.commit()

con.close()
