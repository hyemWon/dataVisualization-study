import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, "html.parser")

movie = html.select("dl.lst_dsc")
for m in movie:
    title = m.select_one("dt.tit a")
    print("="*50)
    print("제목:", title.text)

    url = "https://movie.naver.com" + title.attrs['href']

    raw_each = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html_each = BeautifulSoup(raw_each.text, 'html.parser')

    # 포스터의 src 속성값 찾기
    poster = html_each.select_one("div.mv_info_area div.poster img")
    poster_src = poster.attrs["src"]

    urlretrieve(poster_src, "poster/" + title.text[:2] + ".png")