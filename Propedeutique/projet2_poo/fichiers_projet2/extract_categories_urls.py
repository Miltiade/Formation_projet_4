"""A script to extract URLs of all books categories from the website's homepage (https://books.toscrape.com/)"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "http://books.toscrape.com/index.html"


def extract_categories_url(url):
    '''Declare empty list'''
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

# # TESTING THE FUNCTION ON THE HOMEPAGE URL:
# url = "http://books.toscrape.com/index.html"
# result = extract_categories_url(url)
# print(result)
