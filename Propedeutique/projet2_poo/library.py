'''A script that creates the CSV document (w/ all books inside). THE SCRIPT CREATES THE "CATEGORIES" OBJECTS.'''
'''Classe manager (all books) : contient une liste de catégories (chaque item de la liste est une catégorie)'''

'''POUR APPELER UNE METHODE DE LA MËME CLASSE, IL FAUT TOUJOURS AJOUTER SELF'''

import requests
from bs4 import BeautifulSoup
from category import Category

class Library:
    '''Tous les livres'''
    def __init__(self):
        '''Initialise les attributs de la catégorie : elle existe et elle contient une liste de catégories de livres.'''
        self.url = "www.books.toscrape.com"
        self.categories = []

    def scrape_all_categories(self, url):
        '''Scrape les données de toutes les catégories de livres'''
        for category in library.categories:
            print("I heard you; processing now.")
            '''From webpage, extract each book category's URL'''
            categories_URLs = self.extract_categories_url()
            print("Categories URL extracted!")
            '''Loop through the book categories' URLs and call the data scraping function for each URL'''
        for url in categories_URLs:
            category = Category(url)
            category.main_single_category(url)
        print("all done! cheers!")

    def extract_categories_url(self):
            '''Importe les URLs des livres de la catégorie'''
            # '''Declare empty list'''
            # categories_urls = []
            '''Create Soup object that will be parsed'''
            response = requests.get(self.url)
            '''Parse the page'''
            soup = BeautifulSoup(response.content, "html.parser")
            '''Find the sidebar element'''
            sidebar = soup.find("div", class_="side_categories")
            '''Find all the category links except the first link ("all books")'''
            category_links = sidebar.find_all("a")[1:]
            '''Extract the absolute URLs from the category links'''
            absolute_links = [urljoin(self.url, link["href"]) for link in category_links]
            '''Return the absolute links'''
            return absolute_links

library = Library()
'''Crée un library main dans la classe Library'''