# -*- coding: utf-8 -*- 
#!/usr/bin/python

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import sys
import matplotlib.pyplot as plt
from pylab import *


plt.style.use('ggplot')
plt.rcParams['figure.figsize']=(15,5)



data = pd.read_csv('kvartiry.csv')
data['Square'] = data.Square.astype('float64')
data['Price'] = data.Price.astype('int64')
data['Metro']=data.Metro.astype('str')



data_metro = data['Metro'].value_counts()
data_metro.plot(kind='bar')
xlabel('Metro')
ylabel('Numbers')
plt.show()

data_rooms = data['Rooms'].value_counts()
data_rooms.plot(kind='bar')
xlabel('Rooms')
ylabel('Numbers')
plt.show()

metro_mean = data.groupby(data.Metro).Price.mean()
metro_mean.plot(kind='bar')
xlabel('Metro')
ylabel('Mean price, rub')
plt.show() 

rooms_mean = data.groupby(data.Rooms).Price.mean()
rooms_mean.plot(kind='bar')
xlabel('Rooms')
ylabel('Mean price, rub')
plt.show()

rooms_square = data.groupby(data.Rooms).Square.mean()
rooms_square.plot(kind='bar')
xlabel('Rooms')
ylabel('Mean square, m^2')
plt.show()






sys.exit(0)

label = LabelEncoder()
dicts = {}

label.fit(data.Rooms.drop_duplicates())
dicts['Rooms'] = list(label.classes_)
data.Rooms = label.transform(data.Rooms)

label.fit(data.Metro.drop_duplicates())
dicts['Metro'] = list(label.classes_)
data.Metro = label.transform(data.Metro)

metro_mean = data.groupby(data.Metro).Price.mean()


#sys.exit(0)


#print(label.inverse_transform(data.Metro))
#data.to_csv('')