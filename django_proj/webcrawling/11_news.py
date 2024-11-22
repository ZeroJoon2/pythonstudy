from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

url = 'https://fs.jtbc.co.kr/RSS/economy.xml'

jtbc_news = requests.get(url)

soup = BeautifulSoup(jtbc_news.content, 'xml')
#print(soup)

link_list = soup.select('item > link')
#print(link_list[0].text)

# head > meta:nth-child(91)


news_list = []
for num, i in enumerate(link_list):
    tmp_url = i.text
    tmp_res = requests.get(tmp_url)
    tmp_soup = BeautifulSoup(tmp_res.content, 'html.parser')

    title_el = tmp_soup.find('meta', {'name':'twitter:title'})
    description_el = tmp_soup.find('meta', {'name':'twitter:description'})
    title = title_el['content']
    description = description_el['content']

    # print(f'''
    # title : 
    # {title}
    # ''')

    # print(f'''
    # description :
    # {description}
    # ''')

    news_list.append([num+1, title, description, i.text])

#print(news_list)

import pandas as pd
df = pd.DataFrame(news_list, columns = ['idx', 'title','description', 'url'])
print(df)

df.to_csv('jtbc_news_list.csv', index = False, encoding='cp949')

df.to_pickle('test.pickle')