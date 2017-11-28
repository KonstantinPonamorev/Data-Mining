# -*- coding: utf-8 -*- 
#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import csv
import sys


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
        writer.writerow( (data['title'],
                          data['price'],
                          data['address'],
                          data['myurl'] )  )
        #sys.exit(0)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    #print(soup)
    ads = soup.find('div', class_='catalog-list', recursive = True).find_all('div', class_='item_table')
    for ad in ads:
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
        write_csv(data)


def main():
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