import os

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

filename = './restaurant_data/restaurants.html'
url = 'https://burgerkingrus.ru/restaurants'


def parse_restaurant_datafile_bs(filename):
    data = []
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    search_box = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         '//*[@id="__layout"]/div/div/div/div/div[3]/input')))
    search_box.send_keys("москва", Keys.ENTER)
    html = driver.page_source
    soup = BeautifulSoup(html, features='lxml')
    restaurant_list = soup.find(
        'div',
        attrs={'class': 'bk-restaurants-list bk-restaurants-list__query'})
    items = restaurant_list.find_all('div', attrs={'class': 'bk-restaurant-card'})
    for item in items:
        # getting name and franchise
        name = item.find(
            'div',
            {'class': 'bk-restaurant-card__tags'}).text
        franchise = "Burger King"
        # getting city and address
        address = item.find(
            'div',
            {'class': 'bk-restaurant-card__name'}).text
        city = "Москва"
        # getting phone
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


def load_data_to_directory():
    results = []
    for filename in os.listdir('./restaurant_data/'):
        results.extend(parse_restaurant_datafile_bs(filename))
    return results


def convert_data_bk():
    data = parse_restaurant_datafile_bs(filename)
    data_restaurants_kfc_df = pd.DataFrame(data)
    data_restaurants_kfc_df.to_csv('bk_restaurants', encoding='utf-8')


load_data_to_directory()
convert_data_bk()
