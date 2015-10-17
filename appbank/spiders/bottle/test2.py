# -*- coding: utf-8 -*-

from os import path
import sqlite3

#print path.dirname(path.abspath(__file__))

dirname = path.dirname(path.abspath(__file__))
dirname = dirname.replace('bottle', '')
#print dirname
db_dir = dirname + 'sqlite\\'
print db_dir

conn = sqlite3.connect(db_dir + 'pdAppbank.db')
c = conn.cursor()
c.execute('select * from monster')
result = c.fetchall()
print result
