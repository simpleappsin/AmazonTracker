import pyttsx3
import sys,time,os
from bs4 import BeautifulSoup
import requests
import smtplib
import time

URL = "https://www.amazon.com/Planar-Helium-PCT2235-Resolution-Monitor/dp/B01E06JSI4/ref=sr_1_1_sspa?crid=2856X74WL04W2&dchild=1&keywords=computer+monitor&qid=1592035960&s=electronics&sprefix=com%2Celectronics%2C167&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRVE3MTNPTjZNNkNHJmVuY3J5cHRlZElkPUEwOTY0NzQ5UlFNVFdWRzM0TlRHJmVuY3J5cHRlZEFkSWQ9QTA3MzUzODAzR0lNVUtJU0dBQzYzJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
PRIC = 100

def check_price():
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content , 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text().strip()[1:4] 
    print(title)
    print(price)
    return price

def TrackThePrice():
    price = int(check_price())
    if price == PRIC:
        print("It is still same")
    else:
        print("It is cheaper now")



if __name__ == "__main__":
    while True:
        TrackThePrice()
        time.sleep(2)