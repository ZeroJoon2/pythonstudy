import requests
from bs4 import BeautifulSoup
import re
import pymysql

pattern = re.compile(r'[\t\r\n 적정가격]+')

url = 'https://www.paxnet.co.kr/stock/report/report?wlog_rpt=jm&menuCode=2222'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

#contents > div.cont-area > div.board-type > ul > li:nth-child(2) > div:nth-child(1) > strong > a

link_list = []
for i in soup.select('#contents div.cont-area div:nth-child(1) a'):
    #print(i['href'])
    print(i)
    if i['href'] != '#':
        link_list.append([i.text, i['href']])
    else:
        pass

#contents > div.cont-area > div.board-type > ul > li:nth-child(17) > div:nth-child(2) > p > a
title_list = []
for i in soup.select('#contents p a'):
    #print(i.text)
    title_list.append(pattern.sub(' ', i.text))

#title_list에 안 보이는 텍스트가 있는데 어차피 zip으로 묶을꺼라 괜찮아보임
#zip은 작은 숫자로 매핑

soup.select('#contents > div.cont-area > div.board-type div:nth-child(5)')
investment_list = []
for i in soup.select('#contents > div.cont-area > div.board-type div:nth-child(5)'):
    #print(i.text)
    if i.text != '제공출처':
        investment_list.append(i.text)
    else:
        pass


#contents > div.cont-area > div.board-type > ul > li:nth-child(20) > div:nth-child(6)
soup.select('#contents > div.cont-area > div.board-type div:nth-child(5)')
post_date = []
for i in soup.select('#contents > div.cont-area > div.board-type div:nth-child(6)'):
    #print(i.text)
    if i.text != '작성일':
        post_date.append(i.text)
    else:
        pass


#contents > div.cont-area > div.board-type > ul > li:nth-child(2) > div:nth-child(3)
price_list = []
for i in soup.select('#contents div:nth-child(3)')[1:]:
    # 첫줄에 적정가격 header가 있어서 1이후부터 끝까지

    #여러 공백 문자가 있지만, 위에 정규식으로 처리
#     i.text.strip().replace('	','').replace(' ','').replace('''
#  ''','')
    print(pattern.sub('',i.text))
    price_list.append(pattern.sub('',i.text))

color_class = ['line3 color-black',
          'line3 color-red',
          'line3 color-blue']

soup.findAll('div', class_ = color_class)

position_list = []
for i in soup.findAll('div', class_ = color_class):
    position_list.append(pattern.sub('',i.text))

#link_list 건들이기 싫어서 list 새로 만듦
final_list = []

for i,j,y,z, a,b in zip(link_list, title_list, investment_list, post_date, price_list, position_list):
    tmp_list = []
    tmp_list.append(i[0])
    tmp_list.append(i[1])
    tmp_list.append(j)
    tmp_list.append(y)
    tmp_list.append(z)    
    tmp_list.append(a)
    tmp_list.append(b)
    final_list.append(tmp_list)

final_list
#이러면 final_list에 6개 컬럼 들어감
#종목 | 세부링크 | 게시물 제목 | |투자사 | 작성일 | 투자 포지셔닝


#csv로 저장함

import pandas as pd

df = pd.DataFrame(final_list, columns = ['stock','url', 'title','investment', 'date', 'price', 'position'])
df

df.to_csv('13_project_stock_py.csv', index = False, encoding = 'cp949')

#다른 파일 실행하기
with open('db_config.py', mode= 'r', encoding= 'utf-8') as f:
    code = f.read()
    exec(code)

with open('query3.py', mode = 'r', encoding = 'utf-8') as f:
    code = f.read()
    exec(code)