import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup
#current-weather > div.cmp-cur-weather.wbg.wbg-type2.BGDB00 > ul.wrap-1 > li.w-icon.w-temp.no-w > span.tmp
# //*[@id="current-weather"]/div[2]/ul[1]/li[1]/span[4]
url = 'https://www.weather.go.kr/w/index.do#dong/1138065000/37.5783424/126.9006336/%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%9D%80%ED%8F%89%EA%B5%AC%20%EC%88%98%EC%83%89%EB%8F%99/LOC/%EC%9C%84%EA%B2%BD%EB%8F%84(37.58,126.90)'
weather_info = requests.get(url, 'html.parser')
soup = BeautifulSoup(weather_info.text, 'html.parser')

#브라우저가 프로그램 종료 시, 사라지지 않도록 옵션 지정
# Options()가 메서드 체이닝이 안되기 때문에 이렇게 한줄로 따로 작성해줘야함
chrome_option = Options()
chrome_option.add_experimental_option('detach', True)

# 브라우저 열기
driver = webdriver.Chrome(options = chrome_option)
driver.get(url)

#연결 후 5초 기다림(암시적 대기)
#요소가 로드될때까지 대기
driver.implicitly_wait(5)

selenium_el = driver.find_element(by=By.CSS_SELECTOR, value = 'span.tmp')


#beautiful soup은 잘 안됨
print(f"soup.select('span.tmp') : {soup.select('#current-weather #current-weather')}")
print(f'selenium_el.text : {selenium_el.text}')

