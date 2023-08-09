'''A script that creates a "category" class and every "category" object'''

import requests
from bs4 import BeautifulSoup
from fichiers_projet2.scrape_book import scrape
from pathlib import Path
from csv import writer

class Category:
    """Catégorie."""

    def __init__(self, url):
        """Initialise les attributs de la catégorie : elle existe et elle contient des livres."""
        self.url = url
        self.books = []

    '''Instituer une boucle for'''
    for book in self.books:
        book.universal_product_code
        book.title
        book.url
        book.price_including_tax
        book.price_excluding_tax
        book.number_available
        book.category
        book.review_rating
        book.image_url

    '''Appelle la méthode "get URL"'''
    for url in urls:
        book = Book(url)
        book.scrape()
        self.books.append(book)

    def scrape_category(self):
        """Scrape les données d'une catégorie. REMPLIR SELF.BOOKS AVEC AUTANT D'INSTANCES DE BOOKS QU'IL Y A DANS CETTE CATEGORIE"""
        '''Declare empty list'''
        books = []
        '''Create Soup object that will be parsed'''
        response = requests.get(url)
        '''Parse the page'''
        soup = BeautifulSoup(response.content, "html.parser")
        books += soup.find_all("article", {"class": "product_pod"})
        '''Parse the next pages'''
        while soup.find("li", {"class": "next"}):
            next_url = soup.find("li", {"class": "next"}).find("a").get("href")
            url = "/".join(url.split("/")[:-1]) + "/" + next_url
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            books += soup.find_all("article", {"class": "product_pod"})
            break
        values = []
        for link in books:
            url = link.find("a").get("href")
            target_url = "https://books.toscrape.com/catalogue/" + url.replace("../../../", "")
            values.append(scrape(target_url))
        return values

    def extract_categories_url(url):
        '''Importe les URLs des livres de la catégorie'''
        # '''Declare empty list'''
        # categories_urls = []
        '''Create Soup object that will be parsed'''
        response = requests.get(url)
        '''Parse the page'''
        soup = BeautifulSoup(response.content, "html.parser")
        '''Find the sidebar element'''
        sidebar = soup.find("div", class_="side_categories")
        '''Find all the category links except the first link ("all books")'''
        category_links = sidebar.find_all("a")[1:]
        '''Extract the absolute URLs from the category links'''
        absolute_links = [urljoin(url, link["href"]) for link in category_links]
        '''Return the absolute links'''
        return absolute_links

    HEADER = [
        "product_page_url",
        "universal_product_code",
        "title",
        "price_including_tax",
        "price_excluding_tax",
        "number_available",
        "product_description",
        "category",
        "review_rating",
        "image_url",
    ]
    CATEGORY_INDEX = 7

    """Génère un fichier CSV et l'enregistre dans le répertoire idoine"""
    def generate_csv(values, filename="data.csv"):
        base_directory = Path("output_files")
        directory = base_directory / values[0][CATEGORY_INDEX]
        directory.mkdir(parents=True, exist_ok=True)
        file_path = directory / filename
        with open(file_path, "w", buffering=-1) as csvfile:
            csv_writer = writer(csvfile)
            csv_writer.writerow(HEADER)
            csv_writer.writerows(values)
        return ()

    def download(self, upc, url, category):
        """Crée des répertoires de destination"""
        images_directory = Path("output_files") / category / "images"
        images_directory.mkdir(parents=True, exist_ok=True)
        response = requests.get(url)
        if response.ok:
            file_path = images_directory / upc
            with open(f"{file_path}.jpg", "wb") as file:
                file.write(response.content)
                print(f"Image '{upc}' downloaded successfully.")
        else:
            print("Error")        
    
    def download_category_images(values):
        '''Enregistre les images des couvertures des livres'''
        category_name = values[0][7]
        for book_data in values:
            image_url = book_data[9]
            upc = book_data[1]
            full_image_url = image_url.replace("../../", "https://books.toscrape.com/")
            print(full_image_url)
            download(upc, full_image_url, category_name)


category = Category()
'''Crée un objet category dans la classe Category'''