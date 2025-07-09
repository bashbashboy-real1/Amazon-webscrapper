import requests
from bs4 import BeautifulSoup
import time
import datetime
import smtplib
import csv
import pandas as pd 

#u can add a send mail function to alert you 


URL= 'https://www.amazon.sa/-/en/ref=nav_logo'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15", 
    "X-Amzn-Trace-Id": "Root=1-66ab5985-2d5286641e2ca45e76454a67"}

page = requests.get(URL, headers=headers)

soup1= BeautifulSoup(page.content, "html.parser")

soup2= BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id='priceblock_ourprice').get_text()

print(title)
print(price)

price= price.strip()[1:]
title.strip()


today=datetime.date.today()
my_header = ['title', 'price']
data = [title, price, today]

with open('AmazonWebscrapperdataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer= csv.writer(f)
    writer.writerow(my_header)
    writer.writerow(data)
    

df=pd.read_csv("insert filename")

print(df)

def check_price():
    
    URL= 'https://www.amazon.sa/-/en/ref=nav_logo'

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15", 
    "X-Amzn-Trace-Id": "Root=1-66ab5985-2d5286641e2ca45e76454a67"}

    page = requests.get(URL, headers=headers)

    soup1= BeautifulSoup(page.content, "html.parser")

    soup2= BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='priceblock_ourprice').get_text()
    
    price= price.strip()[1:]
    title.strip()
    today=datetime.date.today()
    

while(True):
    check_price()
    time.sleep(5)
