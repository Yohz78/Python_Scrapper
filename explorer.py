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
        """Vérifie si la page suivante existe et la renvoie le cas échéant"""
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

    def page_scrapper(url):
        """Renoie une liste de toutes les données des produits d'une catégorie"""
        url_tool = url.replace('index.html', '')
        urls = explorer(url)
        datas = urls.data_geter()
        next_page = urls.get_next_page()
        while next_page:
            page = explorer(url_tool + next_page)
            datas.append(page.data_geter())
            next_page = page.get_next_page()
        return datas

    def url_getter(self):
        """renvoie une liste de toutes les URLs des catégories du site"""
        ul = self.soup.find('ul',class_="nav nav-list").select('li')[0]
        lis = ul.find_all('li') 
        urls = [("https://books.toscrape.com/") + li.find("a").get('href') for li in lis]
        return urls    

    def site_getter(self):
        """renvoie toutes les datas de tous les articles du site : YOLO """
        categories = self.url_getter()
        datas = [explorer.page_scrapper(category) for category in categories]
        return datas 