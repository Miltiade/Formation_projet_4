"""MAIN_SINGLE_CATEGORY:
a script that scrapes data from a Books category webpage,
then saves scraped data in a CSV file,
then saves each book's image in a specified directory"""

import requests
from bs4 import BeautifulSoup

from utils.scrape_book import scrape

from pathlib import Path
from csv import writer


"""A function that SCRAPES, from a Books category page, all the books' requested data"""


def scrape_category(url):
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


# TESTING scrape_category with url https://books.toscrape.com/catalogue/category/books/travel_2/index.html
# url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
# result = scrape_category(url)
# print(result)

"""A function that:
-- creates local DIRECTORIES
-- generates 1 CSV file with scraped data as values
-- and SAVES the CSV file in one of the directories """


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


def generate_and_save(values, filename="data.csv"):
    base_directory = Path("output_files")
    directory = base_directory / values[0][CATEGORY_INDEX]
    directory.mkdir(parents=True, exist_ok=True)
    file_path = directory / filename
    with open(file_path, "w", buffering=-1) as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow(HEADER)
        csv_writer.writerows(values)
    return ()


"""A function that downloads and SAVES IMAGE FILE of each book.
NB1: filename = [booksUPC].jpeg
NB2: file saved in "[category]/images/" directory"""


'''Create destination directories'''


def download(upc, url, category):
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


'''Download and save images'''


def download_category_images(values):
    category_name = values[0][7]
    for book_data in values:
        image_url = book_data[9]
        upc = book_data[1]
        full_image_url = image_url.replace("../../", "https://books.toscrape.com/")
        print(full_image_url)
        download(upc, full_image_url, category_name)


'''MAIN_CATEGORY: a function that combines all tasks above: scraping, generating CSV, downloading image files'''


def main_single_category(url):
    print("Scraping category : " + url)
    result = scrape_category(url)
    generate_and_save(result)
    download_category_images(result)


# TESTING: MAIN_SINGLE_CATEGORY
# print("I heard you; processing...")
# url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
# result = main_single_category(url)
# print("all done! cheers!")
