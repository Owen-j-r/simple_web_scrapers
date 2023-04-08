# Simple web scrapers

In this repository is just a few examples of simple webscrapers i have made to exercise some methods of data collection

### 1. Newegg Product Scraper

This script is a simple **Newegg product scraper** that takes a search query as input and returns a list of products with their prices and links, sorted by price.

#### Usage
* Run the script
* Enter the product search term you want to search for when prompted
* The script will then display a list of products with their prices and links, sorted by price

#### Features
* **Search Query** : Enter search query to look for products on Newegg
* **Pagination** : The script goes through all available pages for the search query
* **Price Sorting** : The results are sorted by price in ascending order.
* **Output** : The script displays the product name, price, and link for each result.

##### **Example**

What product do you want to search for? SSD

Samsung 870 EVO Series 2.5" 1TB SATA III V-NAND Internal Solid State Drive (SSD) MZ-77E1T0B/AM
$104
https://www.newegg.com/samsung-1tb-870-evo-series/p/N82E16820147794
-------------------------------

Crucial MX500 2.5" 1TB SATA III 3D NAND Internal Solid State Drive (SSD) CT1000MX500SSD1
$109
https://www.newegg.com/crucial-1tb-mx500/p/N82E16820156174
-------------------------------

...and so on.

### 2. CoinMarketCap Crypto Price Scraper

This script fetches the top 10 cryptocurrencies and their prices from CoinMarketCap and displays them in the console.

#### **Usage**

* Run the script

Script will display top 10 cryptocurrencies and their prices in console.

##### **Example**

"=================================================================

Bitcoin: $45,000.00

Ethereum: $3,000.00

Binance Coin: $400.00

Cardano: $2.00

XRP: $0.90

Solana: $140.00

Polkadot: $30.00

Dogecoin: $0.20

Avalanche: $60.00

Chainlink: $25.00

================================================================="

