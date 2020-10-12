import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn")
html = BeautifulSoup(raw.text, "html.parser")

movie = html.select("dl.lst_dsc")

for m in movie:
    title = m.select_one("dt.tit a")

    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")

    genre_all = m.select_one("dl.info_txt1 dd:nth-of-type(1) span.link_txt")
    if "액션" not in genre_all.text:
        continue

    print("="*50)
    print("제목:", title.text)

    print("장르:", end="")
    for g in genre:
        print(g.text, end=", ")
    print()

