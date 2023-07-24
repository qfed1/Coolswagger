# Create a new instance of the Chrome driver
from selenium import webdriver


driver = webdriver.Chrome()



# Navigate to google.com
driver.get("http://www.messages.google.com")

# Close the driver after some delay to see the effect
import time
time.sleep(10)  # pause for 5 seconds

# Don't forget to quit the driver after finished
driver.quit()

