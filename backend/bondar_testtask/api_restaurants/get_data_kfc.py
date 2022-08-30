import re

import requests
from bs4 import BeautifulSoup

s = requests.Session()
s.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36 '
})


def load_restaurant_data(session):
    url = 'https://www.kfc.ru/restaurants'
    request = session.get(url)
    return request.text


def contain_restaurant_data(text):
    soup = BeautifulSoup(text)
    restaurant_list = soup.find('div', {'class': '_1JEleOn1UX'})
    return restaurant_list is not None


page = 1
while True:
    data = load_restaurant_data(s)
    if contain_restaurant_data(data):
        with open('./page_%d.html' % page, 'w') as output_file:
            output_file.write(data.encode('cp1251'))
            page += 1
    else:
        break


def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    return text


def parse_user_datafile_bs(filename):
    results = []
    text = read_file(filename)

    soup = BeautifulSoup(text)
    restaurant_list = soup.find('div', {'class': '_1JEleOn1UX'})
    items = restaurant_list.find_all('div', {'class': ['_1iEaYvElzW']})
    for item in items:
        # getting name and franchise
        name = item.find('div', {'class': '_1p8oADYhWg t-xl mb-24 condensed'}).text
        franchise = re.findall('\w+', name)[0]
        # getting city and address
        address = item.find('div', {'class': '_32rXCPXxSH t-m-sm mt-8'}).text
        city = re.findall('\w+', name)[0]
        # getting phone
        phone = item.find('div', {'class': '_1Gj6uG1m9b t-m-sm mt-8'}).text

        results.append({
            'franchise': franchise,
            'name': name,
            'city': city,
            'address': address,
            'phone': phone,
        })
    return results
