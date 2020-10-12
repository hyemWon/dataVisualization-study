import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook('navernews.xlsx')
    sheet = wb.active

except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["제목","언론사"])
    print("새로운 파일을 만들었습니다.")

keyword = input("검색어를 입력해주세요: ")

for n in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=" + keyword
                       + "&start=" + str(n),
                       headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")

    articles = html.select("ul.type01 > li")

    # 반복2: 기사에 대해서 반복하면 세부 정보 수집하기
    # 리스트를 사용한 반복문으로 모든 기사에 대해서 제목/언론사 출력
    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text

        sheet.append([title,source])

    wb.save('navertv.xlsx')