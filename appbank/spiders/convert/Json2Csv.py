# -*- coding: utf-8 -*-

import sys
import json
import csv

# define parameters

#pathName = 'C:\Users\fumio\MyProject\scrapy\appbank\appbank\spiders'
jsonFName = 'pdskill_short.json'
#csvFName = 'pdskill.csv'

# read json file
#jsonFile = open(pathName + '\\' + jsonFName, 'r')
jsonFile = open(jsonFName)
jsonData = json.load(jsonFile)

print json.dumps(jsonData, sort_keys= True, ensure_ascii = False, indent = 2)

