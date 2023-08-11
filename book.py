'''A script that creates a "book" class'''

import requests
from bs4 import BeautifulSoup

class Book:
    """Instancie la classe Livre."""

    def __init__(self, url):
        """Initialise l'état de la classe : son existence, et les caractéristiques à scraper."""
        print("Initializing class.")
        self.url = url
        self.product_page_url = None
        self.universal_product_code = None
        self.title = None
        self.price_including_tax = None
        self.price_excluding_tax = None
        self.number_available = None
        self.product_description = None
        self.category = None
        self.review_rating = None
        self.image_url = None
        print("Class initialized successfully.")
        
    def scrape(self):
        """Scrape les données du livre"""
        print("Scraping book data.")
        response = requests.get(self.url)
        book = BeautifulSoup(response.content, "html.parser")
        self.universal_product_code = (
            book.find("th", string="UPC").find_parent().find("td").text.strip()
        )
        div = book.find("div", class_="product_main")
        self.title = div.find("h1").text
        table = book.find("table", class_="table table-striped")
        table_td = table.find_all("td")
        self.price_including_tax = table_td[3].text
        self.price_excluding_tax = table_td[2].text
        self.number_available = table_td[5].text
        self.product_description = book.find_all("p")[3].text
        self.category = book.find_all("a")[3].text
        self.review_rating = div.find("p", class_="star-rating").attrs["class"][1]
        self.image_url = book.find("img").attrs["src"]
        print("Book data scraped successfully.")

    def return_data_as_list(self):
        '''méthode qui retourne toutes les données dans une liste (dans l'ordre exact demandé par HEADER)'''
        scraped_data_list = [
        self.product_page_url,
        self.universal_product_code,
        self.title,
        self.price_including_tax,
        self.price_excluding_tax,
        self.number_available,
        self.product_description,
        self.category,
        self.review_rating,
        self.image_url]
        return scraped_data_list
    print("Returning scraped data as list.")

# book = Book("https://books.toscrape.com/catalogue/worlds-elsewhere-journeys-around-shakespeares-globe_972/index.html")
# book.scrape()
# print(book.return_data_as_list())