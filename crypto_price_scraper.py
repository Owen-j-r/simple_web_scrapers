import requests
from bs4 import BeautifulSoup

print('=================================================================')

# Function to fetch the HTML content of a given URL
def fetch_html_content(url):
    response = requests.get(url)
    return response.text

# Function to create a BeautifulSoup object from the HTML content
def create_soup(html_content):
    return BeautifulSoup(html_content, 'html.parser')

# Function to extract the top coins and their prices from the BeautifulSoup object
def extract_top_coins(soup, num_coins=10):
    coin_data = {}

    table_body = soup.tbody
    table_rows = table_body.contents

    for row in table_rows[:num_coins]:
        coin_name_element, price_element = row.contents[2:4]
        coin_name = coin_name_element.p.string
        coin_price = price_element.a.string

        coin_data[coin_name] = coin_price

    return coin_data

# Function to display the top coins and their prices
def display_top_coins(prices):
    for coin, price in prices.items():
        print(f"{coin}: {price}")

# Main script execution
cmc_url = 'https://coinmarketcap.com/'
html_content = fetch_html_content(cmc_url)
soup = create_soup(html_content)

top_coins = extract_top_coins(soup, num_coins=10)
display_top_coins(top_coins)

print('=================================================================')
