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
    t = (row["mon_no"], row["name"], row["skill_no"], row["leader_skill_no"])
    cur.execute("insert into monster values(?, ?, ?, ?)", t)

con.commit()

con.close()

# cur.execute("""
#   create table monster(
#         mon_no integer,
#         name text,
#         skill_no integer,
#         leader_skill_no integer
#         );
# """)

# {"mon_no": "1", "name": "ティラ", "leader_skill_no": "1", "mon_no_evolution_before": "1929", "costs": "2", "stars": "2", "props": ["fire"], "awaken_skills": [], "types": ["dragon"], "skill_no": "1"}
