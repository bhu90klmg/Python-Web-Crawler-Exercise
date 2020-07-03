# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:01:29 2020

@author: CFuser
"""


import requests
from bs4 import BeautifulSoup
url="https://www.ptt.cc/bbs/food/index.html"
import csv
csvfile = "蘇邑洋_StaticWebPages.csv"
def get_href(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.select("div.title")
        with open(csvfile, 'w+', newline='', encoding='big5') as fp:
           writer = csv.writer(fp)
           field_names = ['標題','網址']
           writer.writerow(field_names)
           for item in results:
               title = item.text.replace("\u6ca2","").replace("\u83d3","").replace("\u9244","").replace("\t","").replace(" ","").strip()
               yes_item=item.select_one('a')
               b=yes_item.get('href')
               field_names[0]=title
               field_names[1]='https://www.ptt.cc'+b
               if yes_item:
                    print(field_names)
                    writer.writerow(field_names)
                   
        
for page in range(1,3):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    ptt_btn = soup.select('div.btn-group > a')
    page = ptt_btn[3]['href']
    nextpage = 'https://www.ptt.cc' + page
    url = nextpage
    get_href(url = url)