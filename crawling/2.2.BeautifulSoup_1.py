import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r")

# print(raw.text)

html = BeautifulSoup(raw.text, "html.parser")
print(html)