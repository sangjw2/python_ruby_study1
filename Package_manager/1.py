import requests
from bs4 import BeautifulSoup
r = requests.get("https://codingeverybody.github.io/scraping_sample/1.html")
soup = BeautifulSoup(r.text, 'html.parser')
print('Title : '+soup.title.string)
articles = soup.findAll("div", {"class": "em"})
print('Article : '+articles[0].text)
print("=================================")
r2 = requests.get("https://codingeverybody.github.io/scraping_sample/2.html")
soup2 = BeautifulSoup(r2.text, 'html.parser')
print('Title : '+soup2.title.string)
articles2 = soup2.findAll("div", {"class": "strong"})
print("Article : "+articles2[0].text)