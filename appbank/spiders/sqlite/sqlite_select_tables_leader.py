# -*- coding: utf-8 -*-
import sys
import csv
import sqlite3

con = sqlite3.connect("pdAppbank.db")
con.text_factory = str

cur = con.cursor()

sel = cur.execute("select * from leader")
for row in sel:
    print row[0], row[1], row[2]

#con.commit()

con.close()
