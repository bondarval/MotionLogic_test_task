import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://burgerkingrus.ru/restaurants'


def parse_restaurant_datafile_bs():
    data = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features='lxml')
    restaurant_list = soup.find(
        'div',
        attrs={'class': 'bk-restaurants-list bk-restaurants-list__query'})
    items = restaurant_list.find_all('div', attrs={'class': 'bk-restaurant-card'})
    for item in items:
        name = item.find(
            'div',
            {'class': 'bk-restaurant-card__tags'}).text
        franchise = "Burger King"
        address = item.find(
            'div',
            {'class': 'bk-restaurant-card__name'}).text
        city = "Москва"
        phone = item.find(
            'div',
            {'class': 'bk-restaurant-card__phone'}).text

        data.append({
            'franchise': franchise,
            'name': name,
            'city': city,
            'address': address,
            'phone': phone,
        })
    return data


def convert_data_bk():
    data = parse_restaurant_datafile_bs()
    data_restaurants_kfc_df = pd.DataFrame(data)
    data_restaurants_kfc_df.to_csv('bk_restaurants', encoding='utf-8')


convert_data_bk()
