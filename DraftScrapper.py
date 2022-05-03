import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
articles = soup.find_all('article',class_="product_pod")

# # on récupère le titre
# titres = [art.find('img').get('alt') for art in articles]

# # on récupère les prix
# prices = [art.find(class_='price_color').get_text() for art in articles]	

# # on récupère l'URL
# links = [art.find("a").get('href') for art in articles]

# # on récupère la disponibilité
# dispos = [art.find(class_="instock availability").get_text().replace("\n","").strip() for art in articles]

# On enregistre direct les éléments dans un dico
formatted_articles = []

for art in articles:
	data = {
		'title': art.find('a').get('title'),
		"url": art.find("a").get('href'),
		"price": art.find(class_='price_color').get_text(),
		"dispo": art.find(class_="instock availability").get_text().replace("\n","").strip()
	}
	formatted_articles.append(data)

print(formatted_articles)
