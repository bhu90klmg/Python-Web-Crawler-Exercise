import requests
from bs4 import BeautifulSoup
import csv
import pandas 
for i in range(3,0,-1):
   if i==3:
       url="https://csie.asia.edu.tw/faculty/professors"
       csvfile = "108_CSIE_Faculty_專任教授.csv"
   elif i==2:
       url="https://csie.asia.edu.tw/faculty/associate-professors"
       csvfile = "108_CSIE_Faculty_專任副教授.csv"
   elif i==1:
       url="https://csie.asia.edu.tw/faculty/assistant-professors"
       csvfile = "108_CSIE_Faculty_專任助理教授.csv"
   r = requests.get(url)
   r.encoding = 'utf8'
   soup = BeautifulSoup(r.text, 'lxml')
   tab_table = soup.find(attrs={'class': 'row contact-category'})
   professors = tab_table.find_all('div', class_='col-sm-12')
   with open(csvfile, 'w+', newline='', encoding='big5') as fp:
       field_names = ['姓名', '學歷', '辦公室', '分機', 'E-mail']
       writer = csv.DictWriter(fp, field_names)
       writer.writeheader()
       for professor in professors:
           record_dict = {}
           professor_name = professor.find('h2', 'card-header').string
           record_dict['姓名'] = professor_name
           card_descriptions = professor.find_all('p', class_='card-description')
           for card_description in card_descriptions:
               splited_text = card_description.text.split('：')
               field_name = splited_text[0].strip()
               field_value = splited_text[1].replace('\t', '').replace(' ', '')
               record_dict[field_name] = field_value
           writer.writerow(record_dict)
vms = pandas.read_csv('108_CSIE_Faculty_專任教授.csv', encoding="big5")
users = pandas.read_csv('108_CSIE_Faculty_專任副教授.csv', encoding="big5")
sas =  pandas.read_csv('108_CSIE_Faculty_專任助理教授.csv', encoding="big5")  
merged_df = pandas.concat([vms, users,sas], axis = 1, join = 'outer') 
merged_df.to_csv('108_CSIE_Faculty_蘇邑洋.csv', encoding="big5")                          