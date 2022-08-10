# Import the whisky_web_scraping class
from Helper import whisky_web_scraping

# Create a scraper object
scraper = whisky_web_scraping()

# Scrape Data
product_df = scraper.scrape_whisky(number_of_pages=5)

# Export to CSV
product_df.to_csv('whiskey_data.csv')
