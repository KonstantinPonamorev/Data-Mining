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

