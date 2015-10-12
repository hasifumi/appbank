# -*- coding: utf-8 -*-

import sys
import json
import csv
import codecs

#csvFName = 'pdskill_short.csv'
csvFName = 'pdskill.csv'
jsonFName = 'pdskill_fromCSV.json'

csvFile = open(csvFName, 'r')
jsonFile = codecs.open(jsonFName, 'w', "utf-8")

fieldnames = ("function", "turn_max", "name", "level_max", "skill_no", "turn_init")

reader = csv.DictReader(csvFile, fieldnames)

for row in reader:
    json.dump(row, jsonFile, ensure_ascii = False)
    jsonFile.write(',\n')
