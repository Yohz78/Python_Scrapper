import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'

response = requests.get(url)

if response.ok:
	links = []
	soup = BeautifulSoup(response.text, 'html.parser')
	lis = soup.findAll('li',class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
	for li in lis:
		a = li.findAll('a')
		link = soup.a['href']
		links.append(link)

print(soup)
