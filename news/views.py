from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# GEtting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-28]

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



#Getting news from BBC News

ht_r = requests.get("https://www.bbc.com/news")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("h3", {"class": "gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text"})
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': ht_news})
