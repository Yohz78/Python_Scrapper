import explorer
import csv
import requests

URL = 'https://books.toscrape.com/index.html'

# # Creating a CSV file and download the products images for each category
categories = explorer.Explorer(
    URL).url_getter()

for category in categories:
    name = explorer.Explorer(category).category_getter()
    rows = explorer.Explorer.page_scrapper(category)
    image_count = 1

    # Download les images de la catégorie
    for row in rows:
        image_url = row['image_url']
        image_title = row['category'] + '_' + str(image_count) + '.jpg'
        img_data = requests.get(image_url).content
        with open(image_title, 'wb') as handler:
            handler.write(img_data)
        image_count += 1

    # Crée le fichier CSV
    field_names = ['title', 'product_description', 'review_rating', 'image_url', 'category', 'product_page_url',
                   'universal_ product_code (upc)', 'price_including_tax', 'price_excluding_tax', 'number_available']
    with open(f'{name}.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=field_names, dialect='unix')
        writer.writeheader()
        writer.writerows(rows)

    break
