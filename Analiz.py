import pandas as pd
#from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv('kvartiry.csv')
data['Square'] = data.Square.astype('float64')
data['Price'] = data.Price.astype('int64')
#data.pivot_table(values='Metro', index='Price').plot(kind='bar', stacked = True)
#data.info()
#data.head()
#print(data)
#data.info()
#data.pivot_table('Number', 'Rooms', 'Price', 'count').plot(kind='bar', stacked = True)

label = LabelEncoder()
dicts = {}

label.fit(data.Rooms.drop_duplicates())
dicts['Rooms'] = list(label.classes_)
data.Rooms = label.transform(data.Rooms)

label.fit(data.Metro.drop_duplicates())
dicts['Metro'] = list(label.classes_)
data.Metro = label.transform(data.Metro)



