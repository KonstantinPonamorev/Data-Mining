# -*- coding: utf-8 -*- 
#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import csv
import sys

number=1

def get_html(url):
    r = requests.get(url)
    return r.text



def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages', recursive = True).find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split("&")[0]
    return int(total_pages)



def write_csv(data):
    #print(str(data['title']))
    #print(data['price'])
    #print(data['address'])
    #print(data['myurl'])
    with open('kvartiry.csv', 'a', encoding = 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerow( (data['number'],
                          data['rooms'],
                          data['square'],
                          data['price'],
                          data['metro'],
                          data['address'],
                          data['myurl'] )  )
        #sys.exit(0)



def get_page_data(html):
    global number
    soup = BeautifulSoup(html, 'lxml')
    #print(soup)
    ads = soup.find('div', class_='catalog-list', recursive = True).find_all('div', class_='item_table')
    for ad in ads:
        try:
            rooms = ad.find('div', class_='description').find('h3', class_= 'title').text.strip().split(',')[0]
        except:
            rooms = ''
        try:
            square = ad.find('div', class_='description').find('h3', class_= 'title').text.strip().split(',')[1].split('м')[0].replace(' ', '')
        except:
            square = ''
        try:
            myurl = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3', class_= 'title').find('a').get('href')
        except:
            myurl = ''
        try:
            price = ad.find('div', class_='about').text.strip().split('р')[0].replace(' ','')
        except:
            price = ''
        try:
            metro = ad.find('p', class_='address').text.strip().split('1')[0].split('2')[0].split('3')[0].split('4')[0].split('5')[0].split('6')[0].split('7')[0].split('8')[0].split('9')[0]
        except:
            metro = ''
        try:
            address = ad.find('p', class_='address').text.strip().split(',')[1] + ',' + ad.find('p', class_='address').text.strip().split(',')[2]
        except:
            address = ''
        if price != 'ценанеуказана':
            if price != 'Ценанеуказана':
                data = { 'number':number,
                         'rooms':rooms,
                         'square':square,
                         'price':price,
                         'metro':metro,
                         'address':address,
                         'myurl':myurl}
                write_csv(data)
        number=number+1



def main():
    with open('kvartiry.csv', 'a', encoding = 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(('Number','Rooms','Square','Price','Metro','Address','Url'))
    url = 'https://www.avito.ru/sankt-peterburg/kvartiry/prodam?p=1'
    base_url = 'https://www.avito.ru/sankt-peterburg/kvartiry/prodam?'
    page_part = 'p=' 
    total_pages = get_total_pages(get_html(url))
    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i)
        html = get_html(url_gen)
        get_page_data(html)



if __name__ == '__main__':
    main()