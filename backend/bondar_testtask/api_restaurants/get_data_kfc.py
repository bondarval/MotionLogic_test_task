import os
import re


import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

filename = './restaurant_data/restaurants.html'
url = 'https://www.kfc.ru/restaurants'


def parse_restaurant_datafile_bs(filename):
    data = []
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    button = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/button[2]')))
    button.click()
    search_box = driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/form/input')
    search_box.send_keys("москва")
    html = driver.page_source
    soup = BeautifulSoup(html, features='lxml')
    restaurant_list = soup.find('div', attrs={'class': '_1JEleOn1UX'})
    items = restaurant_list.find_all('div', attrs={'class': '_1iEaYvElzW'})
    for item in items:
        # getting name and franchise
        name = item.find(
            'div',
            {'class': '_1p8oADYhWg t-xl mb-24 condensed'}).text
        franchise = re.findall(r'\w+', name)[0]
        # getting city and address
        address = item.find(
            'div',
            {'class': '_32rXCPXxSH t-m-sm mt-8'}).text
        city = re.findall(r'\w+', address)[0]
        # getting phone
        phone = item.find(
            'div',
            {'class': '_1Gj6uG1m9b t-m-sm mt-8'}).text

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


def convert_data_kfc():
    data = parse_restaurant_datafile_bs(filename)
    data_restaurants_kfc_df = pd.DataFrame(data)
    data_restaurants_kfc_df.to_csv('kfc_restaurants', encoding='utf-8')


load_data_to_directory()
convert_data_kfc()
