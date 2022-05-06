from operator import delitem
import explorer
import csv

# # Creating a CSV file for each category
categories = explorer.Explorer('https://books.toscrape.com/index.html').url_getter()

for category in categories:
    name = explorer.Explorer(category).category_getter()
    rows = explorer.Explorer.page_scrapper(category)
    field_names = ['title', 'description', 'rating','img','category','url','UPC','Price (excl. tax)', 'Price (incl. tax)', 'Availability']

    with open(f"{name}.csv",'w',encoding="utf-8", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(rows)



# name = explorer.explorer('https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html')
# print(name.category_getter())
