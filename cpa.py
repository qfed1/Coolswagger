from organic_googler import OrganicGoogler
import undetected_chromedriver.v2 as uc

# Initialize the Chrome driver with undetected_chromedriver
options = uc.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

with uc.Chrome(options=options) as driver:
    googler = OrganicGoogler(driver=driver)
    
    query = 'CPA -intitle:"profiles" -inurl:"dir/ " "gmail" site:linkedin.com/in/ OR site:linkedin.com/pub/'
    
    # Perform organic search
    results = googler.search(query, max_results=10)
    
    # Loop through search results
    for i, result in enumerate(results):
        print(f"{i+1}. {result['url']}")
