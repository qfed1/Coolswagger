import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
options = uc.ChromeOptions()

# in case you need to set a specific user agent
options.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'

# start chrome
driver = uc.Chrome(options=options)

driver.get('https://messages.google.com/web/authentication')

# get the initial URL
initial_url = driver.current_url

# an infinite loop to keep the browser open
while True:
    # wait for 5 seconds
    time.sleep(5)

    # check if URL has changed
    if driver.current_url != initial_url:
        print('Link changed to:', driver.current_url)
        initial_url = driver.current_url
