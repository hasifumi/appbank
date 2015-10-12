# -*- coding: utf-8 -*-
import sys
import csv
import sqlite3

con = sqlite3.connect('pdAppbank.db')
con.text_factory = str

cur = con.cursor()


cur.execute("""
  delete from mon_type;
""")

con.commit()

con.close()
