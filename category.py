'''A script that creates a "category" class and every "category" object'''

'''Classe category : contient une liste de livres (chaque item de la liste est une instance d'un livre)'''

class Category:
    """Catégorie."""

    def __init__(self, url):
        """Initialise les attributs de la catégorie : elle existe et elle contient des livres."""
        self.url = url
        self.books = []
    
    def scrape_category(self):
        """Scrape les données d'une catégorie. REMPLIR SELF.BOOKS AVEC AUTANT D'INSTANCES DE BOOKS QU'IL Y A DANS CETTE CATEGORIE"""
        '''appeler la méthode "get URL"'''
        for url in urls:
            book = Book(url)
            self.books.append(book)
        '''Instituer une boucle for'''
    def generate_csv
        for book in self.books:
            books.title
            books.url
            '''etc.'''
        """Génère un fichier CSV et l'enregistre dans le répertoire idoine"""
    def download_images
        """Crée des répertoires de destination et y enregistre les images des couvertures des livres"""
    
category = Category()
'''Crée un objet category dans la classe Category'''