from bs4 import BeautifulSoup
import requests
import re

# function to get the search query from the user
def get_search_query():
    return input("What product do you want to search for? ")

# function to create the URL for the search query and page number
def create_url(search_query, pg_no):
    return f'https://www.newegg.com/p/pl?d={search_query}&N=4131&page={pg_no}'

# function to fetch the HTML content of a given URL
def fetch_html(url):
    response = requests.get(url)
    return response.text

# function to create a BeautifulSoup object from the HTML content
def get_soup(html_content):
    return BeautifulSoup(html_content, 'html.parser')

def get_total_pages(soup):
    pg_text_element = soup.find(class_='list-tool-pagination-text')
    
    # If the pagination element is not found, return 0 pages
    if pg_text_element is None:
        return 0

    pg_text = pg_text_element.strong
    total_pages = int(str(pg_text).split('/')[-2].split('>')[-1][:-1])

    # Check if the total_pages value is greater than a reasonable threshold
    if total_pages > 1000:
        total_pages = 0

    return total_pages

# function to extract the matching items, their prices, and links from the BeautifulSoup object
def extract_items(soup, search_query):
    results = {}
    grid = soup.find(class_='item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell')
    matched_items = grid.find_all(string=re.compile(search_query))

    for match in matched_items:
        anchor = match.parent
        if anchor.name != "a":
            continue

        item_url = anchor['href']
        item_container = match.find_parent(class_='item-container')

        try:
            price_str = item_container.find(class_='price-current').find('strong').string
            results[match] = {'price': int(price_str.replace(',', '')), 'link': item_url}
        except:
            pass

    return results

# function to display the results
def display_results(items):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['price'])

    for item in sorted_items:
        print(item[0])
        print(f"${item[1]['price']}")
        print(item[1]['link'])
        print('-------------------------------')

# main script execution
search_query = get_search_query()
url = create_url(search_query, 1)
html_content = fetch_html(url)
soup = get_soup(html_content)

total_pages = get_total_pages(soup)
all_items = {}

for page_number in range(1, total_pages + 1):
    url = create_url(search_query, page_number)
    html_content = fetch_html(url)
    soup = get_soup(html_content)
    items_on_page = extract_items(soup, search_query)
    all_items.update(items_on_page)

# checking if items were found or not
if len(all_items) == 0:
    print("No items were found for your search.")
else:
    display_results(all_items)
