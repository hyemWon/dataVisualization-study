from selenium import webdriver
import time

#다운받은 웹드라이버를 통해 Chrome을 켜겠다. driver는 켜진 웹드라이버를 가르킴
#webdriver.Chrome("드라이버 위치") : 드라이버 변수 생성, 크롬을 켠다.
driver = webdriver.Chrome("./chromedriver.exe")

#url에 접속
driver.get("https://v4.map.naver.com/")

#네이버 지도 업데이트 안내끄기
driver.find_elements_by_css_selector("button.btn_close")[1].click()


#검색창에 검색어 입력하기
#select_one()과 같은 역할 (select() = elements
#send_keys() : <input>,<textarea> 등에 원하는 내용을 입력
search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("치킨")

# 검색버튼 누르기 // 검색버튼: button.spm
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()

time.sleep(1)

stores = driver.find_elements_by_css_selector("div.lsnx")
for store in stores:
    name = store.find_element_by_css_selector("dt > a").text
    addr = store.find_element_by_css_selector("dd.addr").text
    phone = store.find_element_by_css_selector("dd.tel").text

    print("="*50)
    print("가게명:", name)
    print("주소:", addr)
    print("전화번호:", phone)

driver.close()

