'''A script that creates the CSV document (w/ all books inside). THE SCRIPT CREATES THE "CATEGORIES" OBJECTS.'''
'''Classe manager (all books) : contient une liste de catégories (chaque item de la liste est une catégorie)'''

from category import extract_categories_url
from category import main_single_category

class Main:
    '''Tous les livres'''
    def __init__(self):
        '''Initialise les attributs de la catégorie : elle existe et elle contient une liste de catégories de livres.'''
        # self.url = "www.books.toscrape.com"
        self.categories = []

    def scrape_all_categories(url):
        '''Scrape les données de toutes les catégories de livres'''
        for category in self.categories:
            print("I heard you; processing now.")
            '''Define webpage to scrape'''
            url = "https://books.toscrape.com/"
            '''From webpage, extract each book category's URL'''
            categories_URLs = extract_categories_url(url)
            print("Categories URL extracted!")
            '''Loop through the book categories' URLs and call the data scraping function for each URL'''
        for url in categories_URLs:
            main_single_category(url)
        print("all done! cheers!")

main = Main()
'''Crée un objet main dans la classe Main'''

    def extract_categories_url(url):
            '''Importe les URLs des livres de la catégorie'''
            '''Declare empty list'''
            categories_urls = []
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

