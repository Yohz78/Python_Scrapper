import explorer
import pandas as pd 

# Testeur :
test = explorer.explorer('https://books.toscrape.com/index.html')
print(test.site_getter())