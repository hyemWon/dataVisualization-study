import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, "html.parser")

movie = html.select("dl.lst_dsc")
for m in movie:
    title = m.select_one("dt.tit a")
    print("="*50)
    print(title.text)

    url = "https://movie.naver.com" + title.attrs["href"]
    print(url)

    #url(상세페이지)에 접속, html 파싱
    raw_each = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    html_each = BeautifulSoup(raw_each.text, 'html.parser')

    reply = html_each.select('div.score_result li')
    print("-"*50)
    print("평점과 댓글:")
    for r in reply:
        score = r.select_one('div.star_score em').text
        reply = r.select_one('div.score_reple p').text.strip()
        print(score, reply)