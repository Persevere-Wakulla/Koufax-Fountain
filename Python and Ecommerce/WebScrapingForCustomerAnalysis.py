"""Web Scraping for Competitor Analysis: Python can be used to scrape competitor websites for pricing, product offerings, and customer reviews, helping you stay competitive.
    """

import requests
from bs4 import BeautifulSoup

# Define competitor URL
url = "https://www.competitor.com/new-arrivals"

# Send GET request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract product information
products = soup.find_all("div", class_="product-item")
for product in products:
    name = product.find("h2", class_="product-title").text
    price = product.find("span", class_="product-price").text
    print(f"Product: {name}, Price: {price}")
