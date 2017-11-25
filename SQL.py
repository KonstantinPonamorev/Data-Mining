# -*- coding: utf-8 -*- 
#!/usr/bin/python
import gzip
import sqlite3 as db
import csv

c = db.connect(database='kvartiry')
c.text_factory = str
cu = c.cursor()

try:
	cu.execute('''
		CREATE TABLE IF NOT EXISTS kv( 
		    kvnumber INTEGER,
		    kvrooms TEXT,
		    kvsquare TEXT,
		    kvprice INTEGER,
		    kvmetro TEXT,
		    kvaddress TEXT,
		    kvurl TEXT
		    )''')
except: 
	print('Файл уже создан');
c.commit()
c.close()
c = db.connect(database='kvartiry')
cu = c.cursor()
input_file = open('kvartiry.csv', 'rt', encoding='utf-8')
#rdr = csv.DictReader(input_file,
	#fieldnames = ['Number', 'Rooms','Square','Price','Metro','Address','Url'])
creader = csv.reader('kvartiry.csv', delimiter=',', quotechar='>')
for row in creader:
	cu.execute('''INSERT INTO kv (kvnumber, kvrooms, kvsquare, kvprice, kvmetro, kvaddress, kvurl)
		VALUES (?, ?, ?, ?, ?, ?, ?);''', row)
	input_file.close()
c.commit()