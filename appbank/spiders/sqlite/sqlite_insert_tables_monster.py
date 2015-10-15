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
    t = (row["mon_no"], row["name"], row["skill_no"], row["leader_skill_no"],
         row["hp_init"], row["hp_max"], row["hp_plus"],
         row["attack_init"], row["attack_max"], row["attack_plus"],
         row["recovery_init"], row["recovery_max"], row["recovery_plus"])
    cur.execute("insert into monster values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", t)

con.commit()

con.close()

#cur.execute("""
#  create table monster(
#        mon_no integer,
#        name text,
#        skill_no integer,
#        leader_skill_no integer,
#        hp_init integer,
#        hp_max integer,
#        hp_plus integer,
#        attack_init integer,
#        attack_max integer,
#        attack_plus integer,
#        recovery_init integer,
#        recovery_max integer,
#        recovery_plus integer,
#        PRIMARY KEY(mon_no)
#        );
#""")

#{"hp_plus": "4408", "mon_no": "2402", "leader_skill_no": "2357", "recovery_init": "0", "hp_max": "3418", "hp_init": "1367", "mon_no_evolution_before": "2401", "stars": "6", "recovery_max": "20", "costs": "40", "attack_max": "1755", "recovery_plus": "317", "attack_init": "702", "props": ["dark", "light"], "attack_plus": "2250", "awaken_skills": ["27", "21", "29"], "skill_no": "685", "types": ["evil", "dragon"], "name": "覚醒ヘル"}
