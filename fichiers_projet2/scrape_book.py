"""A function that scrapes, from a Book page, all the book's requested data"""


import requests
from bs4 import BeautifulSoup


def scrape(product_page_url):
    response = requests.get(product_page_url)
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
        product_page_url,
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


# # TESTING FUNCTION
# url = "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
# result = scrape(url)
# print(result,"scraping finished")
