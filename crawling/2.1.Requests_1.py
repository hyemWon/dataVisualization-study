import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r")

print(raw)
print(raw.text)
print(raw.elapsed)