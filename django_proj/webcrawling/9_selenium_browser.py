import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#브라우저가 프로그램 종료 시, 사라지지 않도록 옵션 지정
# Options()가 메서드 체이닝이 안되기 때문에 이렇게 한줄로 따로 작성해줘야함
chrome_option = Options()
chrome_option.add_experimental_option('detach', True)

# 브라우저 열기
driver = webdriver.Chrome(options = chrome_option)
driver.get('https://www.python.org')


#검색어 입력요소에 'python'을 입력 3가지중 라이브러리가 제공하는 객체 사용하는 게 추천됨
#input_el = driver.find_element(by='id', value = 'id-search-field')
#input_el = driver.find_element(by='css selector', value = '#id-search-field')
#input_el = driver.find_element(by=By.ID, value = 'id-search-field')
input_el = driver.find_element(by=By.CSS_SELECTOR, value = '#id-search-field')
input_el.send_keys('pycon')
input_el.send_keys(Keys.RETURN)

#검색 결과를 추출
# #content > div > section > form > ul > li:nth-child(2) > h3 > a
input_el = driver.find_elements(by=By.CSS_SELECTOR, value = 'form li h3 > a')
for i in input_el:
    print(i.text)