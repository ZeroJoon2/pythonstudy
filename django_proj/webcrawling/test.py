from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

업무구분 = Select(driver.find_element(by=By.ID, value="taskClCds"))
업무구분.select_by_value('5')

공고명 = driver.find_element(by=By.ID, value="bidNm")
공고명.send_keys('예측모델')

공고일최근1개월 = driver.find_element(by=By.ID, value="setMonth1_1")
공고일최근1개월.click()

#검색버튼 클릭
#searchForm > div > fieldset:nth-child(1) > ul > li:nth-child(4) > dl > dd.fr > a
검색 = driver.find_element(by=By.CSS_SELECTOR, value="fieldset ul li dl dd.fr a")
검색.click()

하단프레임 = driver.find_element(by=By.CSS_SELECTOR, value='frameset frame#sub')
print(하단프레임)
driver.switch_to.frame(하단프레임)

콘텐츠프레임 = driver.find_element(by=By.CSS_SELECTOR, value='frame[name=main]')
print(콘텐츠프레임)
driver.switch_to.frame(콘텐츠프레임)

입찰공고목록 = driver.find_elements(by=By.CSS_SELECTOR, value='#resultForm table tbody tr')
print(len(입찰공고목록))

for 입찰공고 in 입찰공고목록:
    공고정보 = 입찰공고.find_elements(by=By.TAG_NAME, value="td")
    공고명 = 공고정보[3].text
    공고주소 = 공고정보[3].find_element(by=By.TAG_NAME, value="a").get_property('href')
    print(공고명, 공고주소)