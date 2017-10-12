import requests
from bs4 import BeautifulSoup


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')

    for ad in ads:
        # title, price, adress, url
        try:
            title = ad.find('div', class_='description').find('h3', class_= 'title').text.strip()
        except:
            title = ''

        try:
            myurl = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3', class_= 'title').find('a').get('href')
        except:
            myurl = ''

        try:
            price = ad.find('div', class_='about').text.strip()
        except:
            price = ''

        try:
            address = ad.find('p', class_='address').text.strip()
        except:
            address = ''

        data = {'title':title,
               'price':price,
               'address':address,
               'myurl':myurl}