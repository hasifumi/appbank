# -*- coding: utf-8 -*-
import sys
import csv
import json
import sqlite3

json_file = '../pdskill.json'
db_file = '../pdAppbank.db'

con = sqlite3.connect(db_file)
con.text_factory = str

cur = con.cursor()

##fp = open('c:\user\fumio\myproject\scrapy\appbank\appbank\spider\pdskill.csv')
#fp = open('pdskill.csv')
#
#rdr = csv.reader(fp)
#
#for row in rdr:
#    t = (row[0], row[1], row[2],
#            row[3], row[4], row[5])
#    cur.execute("insert into skill values(?, ?, ?, ?, ?, ?)", t)

#fp = open('pdskill.json')

data = []
for line in open(json_file):
    data.append(json.loads(line))

for row in data:
    t = (row["skill_no"], row["name"], row["turn_init"],
            row["level_max"], row["turn_max"], row["function"])
    print t[0], t[1]
    cur.execute("insert into skill values(?, ?, ?, ?, ?, ?)", t)

con.commit()

con.close()


#  create table skill(
#        skill_no integer,
#        name text,
#        turn_init integer,
#        level_max integer,
#        turn_max integer,
#        function text);
