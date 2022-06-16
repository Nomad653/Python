# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 20:21:55 2022

@author: ASUS
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://bina.az/alqi-satqi"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")


item = soup.find_all('div', attrs={"items-i"})

info = []
for i in item:
    parameters = i.find("div", {"class": "card_params"})
    abs_block = parameters.find("div", {"class": "abs_block"})
    price_value = abs_block.find("span", {"class": "price-val"})
    price_currency = abs_block.find("span", {"class": "price-cur"})
    if abs_block.find("span", {"class": "price-per"}) != None:
        price_monthly = True
    else:
        price_monthly = False
    location = parameters.find("div", {"class": "location"})

    info.append([location.text, price_value.text, price_currency.text, price_monthly])
    print("***********************")
    print(price_value.text)
    print(price_currency.text)
    print(price_monthly)
    print(location.text)

df = pd.DataFrame(info, columns=["Location", "Price_value", "Price_currency", "Price_monthly"])
print(df.head())
df.to_csv("Yeni2.csv")