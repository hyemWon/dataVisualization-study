import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn")
html = BeautifulSoup(raw.text, "html.parser")

movie = html.select("dl.lst_dsc")

for m in movie:
    title = m.select_one("dt.tit a")
    score = m.select_one("div.star_t1 span.num")

    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    directors = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    actors = m.select("dl.info_txt1 dd:nth-of-type(3) a")

    print("="*50)
    print("제목:", title.text)

    print("평점:", score.text)

    print("장르:", end="")
    for g in genre:
        print(g.text, end=", ")
    print()

    print("감독:", end="")
    for d in directors:
        print(d.text, end=", ")
    print()

    print("배우:", end="")
    for a in actors:
        print(a.text, end=", ")
    print()