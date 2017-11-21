import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split("&")[0]

    return int(total_pages)

def write_csv(data):
    with open('kvartiry.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow( (data['title'],
                          data['price'],
                          data['address'],
                          data['myurl']) )