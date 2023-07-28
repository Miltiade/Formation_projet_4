'''A script that creates a "book" class'''

import requests
from bs4 import BeautifulSoup

class Book:
    """Instancie la classe Livre."""

    def __init__(self, url, product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url):
        """Initialise l'état de la classe : son existence, et les caractéristiques à scraper."""
        self.url = url
        self.product_page_url = product_page_url
        self.universal_product_code : universal_product_code
        self.title = title
        self.price_including_tax = price_including_tax
        self.price_excluding_tax = price_excluding_tax
        self.number_available = number_available
        self.product_description = product_description,
        self.category = category
        self.review_rating = review_rating
        self.image_url = image_url
        
    def scrape(url):
        """Scrape les données du livre"""
        response = requests.get(url)
        book = BeautifulSoup(response.content, "html.parser")
        universal_product_code = (
            book.find("th", string="UPC").find_parent().find("td").text.strip()
        )
        div = book.find("div", class_="product_main")
        title = div.find("h1").text
        table = book.find("table", class_="table table-striped")
        table_td = table.find_all("td")
        price_including_tax = table_td[3].text
        price_excluding_tax = table_td[2].text
        number_available = table_td[5].text
        product_description = book.find_all("p")[3].text
        category = book.find_all("a")[3].text
        review_rating = div.find("p", class_="star-rating").attrs["class"][1]
        image_url = book.find("img").attrs["src"]
        return [
            url,
            universal_product_code,
            title,
            price_including_tax,
            price_excluding_tax,
            number_available,
            product_description,
            category,
            review_rating,
            image_url,
        ]
            
url = "https://books.toscrape.com/"
book = Book()
"""TEST. Crée un objet book dans la classe Book. ATTENTION : c'est dans Category que seront créés automatiquement les objets book"""