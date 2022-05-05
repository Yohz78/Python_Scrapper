import explorer
import category

# Execute le code : Extrait toutes les données produits de toutes les pages d'une catégorie à partir de sa page d'acceuil
def page_scrapper(url):	
	url_tool = url.replace('index.html','')
	urls = explorer.explorer(url)
	datas = urls.data_geter()
	next_page = urls.get_next_page()
	while next_page:	
		page = explorer.explorer(url_tool + next_page)
		datas.append(page.data_geter())
		next_page = page.get_next_page()			
	return datas

# Testeur :
# test = page_scrapper('https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html')
test = category.category('https://books.toscrape.com/index.html')
test_print = test.url_getter()
print(test_print)