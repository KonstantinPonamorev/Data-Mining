# -*- coding: utf-8 -*- 
#!/usr/bin/python

import sqlite3 as db
import csv

c = db.connect(database='kvartiry')
cu = c.cursor()

try:
	cu.execute('''
		CREATE TABLE kv  
		  ( kvrooms VARCHAR,
		    kvsquare VARCHAR,
		    kvprice int,
		    kvmetro VARCHAR,
		    kvaddress VARCHAR,
		    kvurl VARCHAR );
		    ''')
except: 
	print('Файл уже создан');
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