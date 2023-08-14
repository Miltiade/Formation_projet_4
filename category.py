'''A script that creates a "category" class and every "category" object'''

import requests
from bs4 import BeautifulSoup
from book import Book
from pathlib import Path
from csv import writer

class Category:
    """Catégorie."""

    def __init__(self, url):
        """Initialise les attributs de la catégorie : elle existe et elle contient des livres."""
        print("Initializing class.")
        self.url = url
        self.name = "Unknown Category"
        self.images_directory = None
        self.books = []
        print("Class initialized successfully.")

    def scrape_category(self):
        """Scrape les données d'une catégorie."""
        print("Starting scraping category data.")
        '''Declare empty list'''
        self.books_url = []
        '''Create Soup object that will be parsed'''
        response = requests.get(self.url)
        '''Parse the page'''
        soup = BeautifulSoup(response.content, "html.parser")       
        self.name = soup.find("h1").text
        self.books_url += soup.find_all("article", {"class": "product_pod"})
        '''Parse the next pages'''
        while soup.find("li", {"class": "next"}):
            next_url = soup.find("li", {"class": "next"}).find("a").get("href")
            url = "/".join(self.url.split("/")[:-1]) + "/" + next_url
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            self.books_url += soup.find_all("article", {"class": "product_pod"})
            break
        for link in self.books_url:
            url = link.find("a").get("href")
            target_url = "https://books.toscrape.com/catalogue/" + url.replace("../../../", "")
            book = Book(target_url)
            book.scrape()
            self.books.append(book)
        print("Category data scraped successfully.")

    """Crée un répertoire de destination, puis génère un fichier CSV et l'y enregistre"""
    def generate_csv(self, filename="data.csv"):
        print("generating CSV.")
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
        base_directory = Path("output_files")
        directory = base_directory / self.books[0].category
        directory.mkdir(parents=True, exist_ok=True)
        file_path = directory / filename
        with open(file_path, "w", buffering=-1) as csvfile:
            csv_writer = writer(csvfile)
            csv_writer.writerow(HEADER)
            '''Créer une boucle pour chaque row (indiquer une liste). 
            -- DONE. Dans book: avoir une méthode qui retourne toutes les données dans une liste (dans l'ordre exact demandé par HEADER)
            -- DONE. Créer dans book un def getbookonlist(self), qui va créer une liste'''
            for book in self.books:
                csv_writer.writerow(book.return_data_as_list())
        return ()
    print("csv generated successfully.")

    """Crée des répertoires de destination pour les images"""
    def create_path(self):
        self.images_directory = Path("output_files") / self.name / "images"
        self.images_directory.mkdir(parents=True, exist_ok=True)       

    def download(self, upc, url):
        # Génère une vraie erreur
        # if self.images_directory == None :            
        #         raise ValueError("Image directory is not created")

        response = requests.get(url)
        if response.ok:
            file_path = self.images_directory / upc
            with open(f"{file_path}.jpg", "wb") as file:
                file.write(response.content)
                print(f"Image '{upc}' downloaded successfully.")
        else:
            print("Error downloading image '{upc}'")

    def download_category_images(self):
        '''Enregistre les images des couvertures des livres'''
        for book_data in self.books:
            image_url = book_data.image_url
            upc = book_data.universal_product_code
            full_image_url = image_url.replace("../../", "https://books.toscrape.com/")
            print(full_image_url)
            self.download(upc, full_image_url)

category = Category("https://books.toscrape.com/catalogue/category/books/new-adult_20/index.html")
'''Crée un objet category dans la classe Category'''

category.scrape_category()
category.generate_csv()
category.create_path()
category.download_category_images()