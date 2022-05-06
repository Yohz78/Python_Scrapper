from operator import delitem
import explorer
import pandas as pd
import numpy as np
import csv

# export using CSV module
category = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
rows = explorer.explorer.page_scrapper(category)
field_names = ['title', 'description', 'rating','img','category','url','UPC','Price (excl. tax)', 'Price (incl. tax)', 'Availability']

with open('Products.csv','w',encoding="utf-8", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(rows)

# Testeur :
# test = explorer.explorer('https://books.toscrape.com/index.html')
# print(test.site_getter())