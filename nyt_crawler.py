import requests
from bs4 import BeautifulSoup


def nyt_crawler():
    url = 'http://www.nytimes.com'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    for title in soup.find_all('h2', 'story-heading'):
        print('article title: ' + title.get_text().strip())


nyt_crawler()
