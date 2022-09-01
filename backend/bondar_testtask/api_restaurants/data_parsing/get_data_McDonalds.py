import os
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://tastyandpoint.com/moscow/'


def parse_restaurant_datafile():
    html = requests.get(url).text
    soup = BeautifulSoup(html, features='lxml')
    table = soup.find('tbody', attrs={'class': 'row-hover'})
    output = []
    for row in table.find_all('tr'):
        new_row = []
        for cell in row.find_all(['td', 'th']):
            new_row.append(cell.get_text().strip())
        output.append(new_row)
    return output


def load_data_to_directory():
    results = []
    filename = './restaurant_data/restaurants.html'
    for filename in os.listdir('./restaurant_data/'):
        results.extend(parse_restaurant_datafile())
    return results


def convert_data_mc_donalds():
    data = parse_restaurant_datafile()
    data_restaurants_mcd_df = pd.DataFrame(data)
    data_restaurants_mcd_df.to_csv('mcd_restaurants', encoding='utf-16')


load_data_to_directory()
convert_data_mc_donalds()
