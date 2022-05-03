import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'

# On crée une classe
class Scrapper:
	def __init__(self, url):
		self.url = url

	@property
	def soup(self):
		r = requests.get(self.url)
		soup = BeautifulSoup(r.text, 'html.parser')
		return soup	

	def table_analysis(self):
		data = {
			'title': self.soup.find('li',class_="active" ).get_text(),
			'description': self.soup.find("meta", {"name":"description"}).get('content').replace("\n","").strip(),
			'rating': self.soup.find("div",class_="col-sm-6 product_main").select("p:nth-of-type(3)")[0].get('class')[1]
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
				
test = Scrapper('http://books.toscrape.com/catalogue/soumission_998/index.html')
print(test.table_analysis())
