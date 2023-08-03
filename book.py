'''A script that creates a "book" class'''

import requests
from bs4 import BeautifulSoup

class Book:
    """Instancie la classe Livre."""

    def __init__(self, url):
        """Initialise l'état de la classe : son existence, et les caractéristiques à scraper."""
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
        
    def scrape(self):
        """Scrape les données du livre"""
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
