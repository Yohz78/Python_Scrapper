import requests
from bs4 import BeautifulSoup


class Scrapper:
    """Récupère les données d'un produit"""

    def __init__(self, url):
            self.url = url

    @property
    def soup(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def url_extractor(self):
        """Récupère l'URL d'un produit à partir de sa page"""
        r = requests.get(self.url)
        no_open_tag = r.text.replace("<!--", "")
        no_close_tag = no_open_tag.replace("-->", "")
        soupp = BeautifulSoup(no_close_tag, 'html.parser')
        url = "http://books.toscrape.com" + \
            soupp.find('a', class_="btn btn-success btn-sm").get('href')
        return url    

    def table_analysis(self):    
        """Collecte puis enregistre les données d'un produit dans un dictionnaire """
        data = {
                'title': self.soup.find('li', class_="active" ).get_text(),
                #  description : 		comment = self.soup.find("head").select("meta:nth-of-type(3)")[0].get('content'),
                'description': self.soup.find("meta", {"name": "description"}).get('content').replace("\n", "").strip(),
                'rating': self.soup.find("div", class_="col-sm-6 product_main").select("p:nth-of-type(3)")[0].get('class')[1],
                'img': self.soup.find('img').get('src').replace('../..', "http://books.toscrape.com"),
                'category': self.soup.find("ul", class_="breadcrumb").select("li:nth-of-type(3)")[0].get_text().replace("\n", ""),
                'url': self.url_extractor()
            }
        for child in self.soup.find("table", {"class": "table table-striped"}):
            if child.find('th') != -1:
                data[str(child.find('th')).replace("<th>", "").replace("</th>","")] = str(child.find('td')).replace("<td>","").replace("</td>","")
        data.pop("Product Type")
        data.pop("Tax")
        data.pop("Number of reviews")
        data["Price (excl. tax)"] = data["Price (excl. tax)"].replace(
                "Â£", "")
        data["Price (incl. tax)"] = data["Price (incl. tax)"].replace(
                "Â£", "")
        return data
