from re import A
import requests
from bs4 import BeautifulSoup


class category:
    def __init__(self, url):
        self.url = url

    @property
    def soup(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def url_getter(self):
        ul = self.soup.find('ul',class_="nav nav-list").select('li')[0]
        lis = ul.find_all('li') 
        urls = [("https://books.toscrape.com/") + li.find("a").get('href') for li in lis]
        return urls
