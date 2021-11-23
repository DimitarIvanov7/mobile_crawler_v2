from bs4 import BeautifulSoup as bs4
import requests
# import pandas as pd
import time
# from email_sending import *
from append_json import *
import schedule

link_list = []

def job():
    pages = []
    pages_to_scrape = 1
    for i in range(1, pages_to_scrape+1):
        url = ('https://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=ma0qqp&f1=1')
        pages.append(url)
    for item in pages:
        page = requests.get(item)
        soup = bs4(page.text, 'html.parser')
        for i in soup.findAll("a", {"class": "mmm"}):

            link = i['href']
            check_data(link)

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)