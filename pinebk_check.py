import requests
import time
from bs4 import BeautifulSoup
import yagmail

URL = 'https://pine64.com/product/14%E2%80%B3-pinebook-pro-linux-laptop-ansi-us-keyboard/?v=0446c16e2e66'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

def check_availability():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    title = soup.find('h1').get_text()

    if 'Out' not in title:
        send_mail()
    else:
        print("Pinebook Pro is out of stock.")

def send_mail():
    user = FROM_EMAIL
    app_password = EMAIL_PASSWORD
    to = TO_EMAIL

    subject = 'Pinebook Pro is in stock!!'
    content = ['mail body content']

    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject, content)
        print('Sent email successfully')

while True:
    fifteen_minutes = 900
    check_availability()
    time.sleep(fifteen_minutes)
