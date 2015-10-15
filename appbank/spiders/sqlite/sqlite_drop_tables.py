# -*- coding: utf-8 -*-
import sys
import csv
import sqlite3

con = sqlite3.connect("pdAppbank.db")
con.text_factory = str

cur = con.cursor()

cur.execute("drop table skill")

#cur.execute("drop table leader")

#cur.execute("drop table awaken")

cur.execute("drop table monster")

#cur.execute("drop table mon_awaken")

#cur.execute("drop table mon_type")

#cur.execute("drop table mon_prop")

con.commit()

con.close()
