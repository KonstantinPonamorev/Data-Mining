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
