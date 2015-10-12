# -*- coding: utf-8 -*-
import sys
import csv
import sqlite3

con = sqlite3.connect("pdAppbank.db")
con.text_factory = str

cur = con.cursor()

sel = cur.execute("select * from skill")
for row in sel:
    print row[0], row[1], row[2], row[3], row[4], row[5]

#con.commit()

con.close()
