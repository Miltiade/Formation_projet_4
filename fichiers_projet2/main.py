""" A script to:
-- generate 1 CSV file (containing scraped data)
-- and download every book's image
for each book category"""

from utils.extract_categories_urls import extract_categories_url
from utils.scrape_category import main_single_category

print("I heard you; processing now.")

'''Define homepage as webpage to scrape'''
url = "https://books.toscrape.com/"

'''From homepage, extract each book category's URL'''
categories_URLs = extract_categories_url(url)
print("Categories URL extracted!")

'''Loop through the book categories' URLs and call the data scraping function for each URL'''
for url in categories_URLs:
    main_single_category(url)
print("all done! cheers!")
