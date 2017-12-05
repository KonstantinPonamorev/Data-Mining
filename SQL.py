# -*- coding: utf-8 -*- 
#!/usr/bin/python

import sqlite3 as db
import csv
import sys
import pandas as pd
import math

df = pd.read_csv('kvartiry.csv')
strok=math.floor(len(open('kvartiry.csv', 'r', encoding='utf-8').readlines())/2)-2
my_dict = dict()
for l in range(strok):
	my_dict[df.loc[l,'Address']] = df.loc[l]
v = list(my_dict.values())
with open('kvartirysql.csv', 'a', encoding='utf-8') as f:
	writer = csv.writer(f)
	writer.writerow(('Number','Rooms','Square','Price','Metro','Address','Url'))
	for j in range(len(my_dict)):
		writer = csv.writer(f)
		writer.writerow(v[j])

#in_file = open('kvartirysql.csv', 'r', encoding='utf-8')
#out_file = open('kvartirysql1.csv', 'w', encoding='utf-8')
#writer = csv.writer(out_file)
#for row in csv.reader(in_file):
    #if any(field.strip() for field in row):
      #  writer.writerow(row)
#in_file.close()
#out_file.close()


c = db.connect(database='kvartiry.db')
c.text_factory = str
cu = c.cursor()

try:
	cu.execute('''
		CREATE TABLE kv  
		  ( kvaddress Text Primary Key,
			kvmetro Text,
			kvrooms Text,
			kvsquare Text,
			kvprice Integer,
			kvurl Text );
			''')
except: 
	print('Файл уже создан');
c.commit()
c.close()


#input_file = pd.read_csv('kvartiry.csv', encoding='utf-8')
#input_file = input_file.drop(['Number'], axis=1)
	
#input_file = input_file.drop(0, axis=0)
#print(input_file)
#sys.exit(0)
#rdr = csv.DictReader(input_file,
	#fieldnames = ['Number', 'Rooms','Square','Price','Metro','Address','Url'])

c = db.connect(database='kvartiry.db')
cu = c.cursor()
with open('kvartirysql.csv','rt', encoding='utf-8') as input_file:
	creader = csv.DictReader(input_file, delimiter=',')
	to_db = [(i['Address'], i['Metro'], i['Rooms'], i['Square'], i['Price'], i['Url']) for i in creader]
cu.executemany('''INSERT INTO kv
	(kvaddress, kvmetro, kvrooms, kvsquare, kvprice, kvurl)
	VALUES (?,?,?,?,?,?);''', to_db)
#for rec in input_file:
	#print(rec[1])
	#print(rec[3])
	#sys.exit(0)
	#cu.execute('''INSERT INTO kv
		#(kvrooms, kvsquare, kvprice, kvmetro, kvaddress, kvurl)
		#VALUES (
			#?, ?, ?, ?, ?, ?);''', (rec, rec, rec, rec, rec, rec))
c.commit()
c.close()