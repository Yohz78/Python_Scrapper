import requests
from bs4 import BeautifulSoup

# Class explorer: Gère les pages
class explorer:
	def __init__(self,url):
		self.url = url

	@property	
	def soup(self):
		r = requests.get(self.url)
		soup = BeautifulSoup(r.text, 'html.parser')
		return soup

	def get_articles(self):
		articles = self.soup.find_all('article',class_='product_pod')
		urls = [art.find("a").get('href').replace("../../..","http://books.toscrape.com/catalogue") for art in articles]
		return urls
	
	def get_next_page(self):
			next_page = self.soup.find('li',class_="next")
			if next_page:
				page = self.soup.find('li',class_="next").select('a')[0].get('href')
				print('a fonctionné')
				return page
			else:
				print("n'a pas fonctionné")
				return None

	def data_geter(self):
		articles = self.soup.find_all('article',class_='product_pod')
		urls = [art.find("a").get('href').replace("../../..","http://books.toscrape.com/catalogue") for art in articles]
		datas = [Scrapper(url).table_analysis() for url in urls]
		return datas

# Class Scrapper: scrappe les infos d'une page produit
class Scrapper:
	def __init__(self, url):
		self.url = url

	@property
	def soup(self):
		r = requests.get(self.url)
		soup = BeautifulSoup(r.text, 'html.parser')
		return soup	

	def url_extractor(self):
		r = requests.get(self.url)
		no_open_tag = r.text.replace("<!--","")
		no_close_tag = no_open_tag.replace("-->","")
		soupp = BeautifulSoup(no_close_tag, 'html.parser')
		url = "http://books.toscrape.com" + soupp.find('a',class_="btn btn-success btn-sm").get('href')
		return url

	def table_analysis(self):
		data = {
			'title': self.soup.find('li',class_="active" ).get_text(),
			#  description : 		comment = self.soup.find("head").select("meta:nth-of-type(3)")[0].get('content'),
			'description': self.soup.find("meta", {"name":"description"}).get('content').replace("\n","").strip(),
			'rating': self.soup.find("div",class_="col-sm-6 product_main").select("p:nth-of-type(3)")[0].get('class')[1],
			'img': self.soup.find('img').get('src').replace('../..',"http://books.toscrape.com"),
			'category': self.soup.find("ul", class_="breadcrumb").select("li:nth-of-type(3)")[0].get_text().replace("\n",""),
			'url': self.url_extractor()
		}
		for child in self.soup.find("table", {"class":"table table-striped"}):
			if child.find('th') != -1:
				data[str(child.find('th')).replace("<th>","").replace("</th>","")]=str(child.find('td')).replace("<td>","").replace("</td>","")
		data.pop("Product Type")
		data.pop("Tax")
		data.pop("Number of reviews")
		data["Price (excl. tax)"] = data["Price (excl. tax)"].replace("Â£","")
		data["Price (incl. tax)"] = data["Price (incl. tax)"].replace("Â£","")
		return data		

def page_scrapper(url):	
	url_tool = url.replace('index.html','')
	urls = explorer(url)
	datas = urls.data_geter()
	next_page = urls.get_next_page()
	while next_page:	
		page = explorer(url_tool + next_page)
		datas.append(page.data_geter())
		next_page = page.get_next_page()			
	return datas


# Tester :
test = page_scrapper('https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html')

print(test)
				


