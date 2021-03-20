import os
import requests
import schedule
import time
import yagmail
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

FROM_EMAIL = os.getenv('FROM_EMAIL')
TO_EMAIL = os.getenv('TO_EMAIL')
KEY = os.getenv('KEY')
DAILY_EMAIL=os.getenv('DAILY_EMAIL')
URL = 'https://www.bestbuy.com/site/asus-zenbook-14-laptop-amd-ryzen-5-8gb-memory-nvidia-geforce-mx350-256gb-ssd-light-gray/6403819.p?skuId=6403819'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

def check_availability():
    html = requests.get(URL, headers=headers)
    price_class = BeautifulSoup(html.content, 'html.parser').find(class_='priceView-hero-price priceView-customer-price')
    price_block = price_class.contents[0]
    price = str(price_block.contents).strip("'[$]")

    if float(price) < 576:
        send_good_price_mail()
    else:
        print("Price is still too high")

def send_good_price_mail():
    with yagmail.SMTP(FROM_EMAIL, KEY) as yag:
        yag.send(TO_EMAIL, 'Asus price under $576!!', URL)
        print('Price email sent successfully')

# def send_daily_mail():
    # with yagmail.SMTP(FROM_EMAIL, KEY) as yag:
    #     yag.send(DAILY_EMAIL, 'Pinebook script is still running')
    #     print('Daily email sent')

# schedule.every().day.at("07:30").do(send_daily_mail)

while True:
    check_availability()
    # schedule.run_pending()
    time.sleep(600)

