# -*- coding: utf-8 -*-
import sys
import csv
import json
import sqlite3

json_file = '../pdmon.json'
csv_file = '../pdmon.csv'
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
    for index, value in enumerate(row["props"]):
        t = (row["mon_no"], index + 1, value)
        cur.execute("insert into mon_prop values(?, ?, ?)", t)

con.commit()

con.close()

#cur.execute("""
#  create table mon_awaken(
#        mon_no integer,
#        seq integer,
#        awaken_skill_no integer
#        );
#""")

# {"mon_no": "1", "name": "ティラ", "leader_skill_no": "1", "mon_no_evolution_before": "1929", "costs": "2", "stars": "2", "props": ["fire"], "awaken_skills": [], "types": ["dragon"], "skill_no": "1"}
