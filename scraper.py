import requests
from bs4 import BeautifulSoup
import smtplib
import time

goal_price = 1550
url = 'https://www.amazon.com/Apple-iPad-12-9-inch-Wi-Fi-256GB/dp/B0862HNWGK/ref=sr_1_3?dchild=1&keywords=ipad+pro&qid=1590115879&sr=8-3'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

def check_price():
    page = requests.get(url, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id= "priceblock_ourprice").get_text()
    converted_price = float(price[1:2] + price[3:6])

    if(converted_price < goal_price):
        send_email()
    print(converted_price)

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('testuser745235@gmail.com', 'uvpihremxdydhehl')

    subject = 'Price has dropped'
    body = 'The price of the product has dropped! Link:https://www.amazon.com/Apple-iPad-12-9-inch-Wi-Fi-256GB/dp/B0862HNWGK/ref=sr_1_3?dchild=1&keywords=ipad+pro&qid=1590115879&sr=8-3 '
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'testuser745235@gmail.com',
        'thetechosaur2@gmail.com',
        msg
    )

    print('Email has been sent')

    server.quit()

while(True):
    check_price()
    time.sleep(86400)



