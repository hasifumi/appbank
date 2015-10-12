# -*- coding: utf-8 -*-
import sys
import csv
import json
import sqlite3

json_file = '../pdawaken.json'
csv_file = '../pdawaken.csv'
db_file = 'pdAppbank.db'

con = sqlite3.connect(db_file)
con.text_factory = str

cur = con.cursor()

##fp = open('c:\user\fumio\myproject\scrapy\appbank\appbank\spider\pdskill.csv')
#fp = open(csv_file)
#
#rdr = csv.reader(fp)
#
#for row in rdr:
#    t = (row[4], row[2], row[5],
#            row[3], row[1], row[0])
#    cur.execute("insert into skill values(?, ?, ?, ?, ?, ?)", t)

data = []
for line in open(json_file):
    data.append(json.loads(line))

for row in data:
    t = (row["awaken_skill_no"], row["name"], row["function"])
    #print t[0], t[1]
    cur.execute("insert into awaken values(?, ?, ?)", t)

con.commit()

con.close()

# cur.execute("""
#   create table awaken(
#         awaken_skill_no integer,
#         name text,
#         function text);
# """)

# awaken_skill_no,function,name

