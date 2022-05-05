# Class explorer: Gère les pages
import requests
from bs4 import BeautifulSoup
import scrapper


class explorer:
    """liste les produits d'une catégorie et stock leurs données"""

    def __init__(self, url):
        self.url = url

    @property
    def soup(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def get_next_page(self):
        """Vérifie si la page suivant existe et la renvoie le cas échéant"""
        next_page = self.soup.find('li', class_="next")
        if next_page:
            page = self.soup.find('li', class_="next").select('a')[
                    0].get('href')
            return page
        else:
            return None

    def data_geter(self):
        """Récupère toutes les infos des produits d'une page"""
        articles = self.soup.find_all('article', class_='product_pod')
        urls = [art.find("a").get('href').replace(
        "../../..", "http://books.toscrape.com/catalogue") for art in articles]
        datas = [scrapper.Scrapper(url).table_analysis() for url in urls]
        return datas
