'''A script that creates a "book" class and every "book" object'''
'''NB : Classe book > objet book (état, méthodes)'''

class Book:
    """Instancie la classe Livre."""

    def __init__(self, title, author, UPC):
        """Initialise l'état de la classe : son existence, et les caractéristiques à scraper."""
        self.title = title
        self.author = author
        self.UPC = UPC
    
    def scrape_book():
        """Scrape les données du livre"""

book = Book()
"""Crée un objet book dans la classe Book"""