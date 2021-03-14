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
URL = 'https://pine64.com/product/14%E2%80%B3-pinebook-pro-linux-laptop-ansi-us-keyboard/?v=0446c16e2e66'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

def check_availability():
    html = requests.get(URL, headers=headers)
    page_title = BeautifulSoup(html.content, 'lxml').find('h1').get_text()

    if 'Out' not in page_title:
        send_in_stock_mail()
    else:
        print("Pinebook Pro is out of stock")

def send_in_stock_mail():
    with yagmail.SMTP(FROM_EMAIL, KEY) as yag:
        yag.send(TO_EMAIL, 'Pinebook available!!', URL)
        print('Available email sent successfully')

def send_daily_mail():
    with yagmail.SMTP(FROM_EMAIL, KEY) as yag:
        yag.send(DAILY_EMAIL, 'Pinebook script is still running')
        print('Daily email sent')

schedule.every().day.at("07:30").do(send_daily_mail)

while True:
    check_availability()
    schedule.run_pending()
    time.sleep(60)
