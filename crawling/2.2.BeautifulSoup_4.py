import requests
from bs4 import BeautifulSoup

#1페이지~10페이지
for n in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=코로나&start="+str(n),
                     headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")

    articles = html.select("ul.type01 > li")

    #한페이지의 기사들
    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text

        print(title, source)