# -*- coding: utf-8 -*- 
#!/usr/bin/python

import sqlite3 as db
import csv
import sys
import pandas as pd


c = db.connect(database='kvartiry')
cu = c.cursor()

try:
	cu.execute('''
		CREATE TABLE kv  
		  ( kvrooms VARCHAR,
		    kvsquare VARCHAR,
		    kvprice VARCHAR,
		    kvprice VARCHAR,
		    kvmetro VARCHAR,
		    kvaddress VARCHAR,
		    kvurl VARCHAR );
		    ''')
except: 
	print('Файл уже создан');
c.commit()
c.close()



input_file = pd.read_csv('kvartiry.csv', encoding='utf-8')
input_file = input_file.drop(['Number'], axis=1)
	
#input_file = input_file.drop(0, axis=0)
#print(input_file)
#sys.exit(0)
#rdr = csv.DictReader(input_file,
	#fieldnames = ['Number', 'Rooms','Square','Price','Metro','Address','Url'])

c = db.connect(database='kvartiry')
cu = c.cursor()
for rec in input_file:
	#print(rec[1])
	#print(rec[3])
	#sys.exit(0)
	cu.execute('''INSERT INTO kv
		(kvrooms, kvsquare, kvprice, kvmetro, kvaddress, kvurl)
		VALUES (
			?, ?, ?, ?, ?, ?);''', (rec, rec, rec, rec, rec, rec))
c.commit()
c.close()

c = db.connect(database='kvartiry')
cu = c.cursor()
input_file = open('kvartiry.csv', 'rt', encoding='utf-8')
#rdr = csv.DictReader(input_file,
	#fieldnames = ['Number', 'Rooms','Square','Price','Metro','Address','Url'])
for row in input_file:
	cu.execute('''INSERT INTO kv
		(kvrooms, kvsquare, kvprice, kvmetro, kvaddress, kvurl)
		VALUES (?, ?, ?, ?, ?, ?);''', (row, row, row, row, row, row))
c.commit()
input_file.close()

