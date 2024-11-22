import selenium
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = chrome_options)
driver.get('https://www.g2b.go.kr/index.jsp')

#업무구분(select 박스)
gubun = Select(driver.find_element(by = By.ID, value = 'taskClCds'))
gubun.select_by_value('5')

#공고명(input)
title = driver.find_element(by=By.ID, value = 'bidNm')
title.send_keys('예측모델')

#최근 1개월 선택(라디오 박스)
period = driver.find_element(by= By.ID, value = 'setMonth1_1')
period.click()

#검색 버튼
#searchForm > div > fieldset:nth-child(1) > ul > li:nth-child(4) > dl > dd.fr > a
search_go = driver.find_element(by = By.CSS_SELECTOR, value = 'fieldset ul li dl dd.fr a')
search_go.click()

#공고 목록 화면 출력

#공고 들어가기

#resultForm > div.results > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > a
#근데 나라장터 페이지는 html이 html을 감싸고 있는 frame 구조

frame1 = driver.find_element(by=By.CSS_SELECTOR, value = 'frameset frame#sub')
print(frame1)
driver.switch_to.frame(frame1) 

frame2 = driver.find_element(by=By.CSS_SELECTOR, value = 'frame[name=main]')
print(frame2)
driver.switch_to.frame(frame2) 

frame3 = driver.find_elements(by=By.CSS_SELECTOR, value = '#resultForm table tbody tr')
print(len(frame3))

#페이지에서 공고내용 추출
for i in frame3:
    post_info = i.find_elements(by = By.TAG_NAME, value = 'td')
    print(f'''
        post_info :
        {post_info}
        *******
        ''')
    post_title = post_info[3].text
    post_url = post_info[3].find_element(by=By.TAG_NAME, value = 'a').get_property('href')
    post_link = post_info[3].find_element(by=By.TAG_NAME, value = 'a')
    # print(f'''
    #       ********************
    #       post_title, post_url : 
    #       {post_title, post_url,
    #        post_link}
    #       ********************
    #       '''
    #       )
    
    # 공고 들어가기
    post_link.click()

    # 공고 들어가서 HTML 불러오기
    res = requests.get(post_url)
    #print(f'res : {res.text}')

    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup)
    supplier = soup.select_one("th:has(p:-soup-contains('supplier'))+td .tb_inner")

    # if supplier.text.strip() == '한국전력공사':
    #     estimate_price = i.


    # if 


#container > div:nth-child(12) > table > tbody > tr:nth-child(2) > td:nth-child(4) > div
#dmdgPrdpay    
    

    if price : 
        price = price.text.strip()
        print(f'''
            여기
            {price}
            *******
              ''')
    else:
        price = '없음'

# 값이 나오면 df로 바꿔봐야함