import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/chart/index.htm'
header = header = {'User-Agent': 'Mozila/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
# 멜론은 python 응답을 막아놔서, header 지정 필요

res = requests.get(url, headers = header)
melon_soup = BeautifulSoup(res.text, 'html.parser')
print(f'{res.text}')
print(f'{melon_soup}')

music_title = melon_soup.select("div.ellipsis.rank01 a")
music_singer = melon_soup.select("div.ellipsis.rank02 span")
title_list = [i.text for i in music_title]
singer_list = [j.text for j in music_singer]

if len(music_title) == len(music_singer):
    for num, i in enumerate(music_title):
        for num2, j in enumerate(music_singer):
            if num == num2 :
                print(f'{num+1}위 | 제목 {i.text} | 가수 {j.text}')
                