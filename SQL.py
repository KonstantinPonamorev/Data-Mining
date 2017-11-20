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
