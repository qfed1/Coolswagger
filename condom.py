import undetected_chromedriver.v2 as uc
import random
import string
import time  # Importing time module

def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Initialize the options
options = uc.ChromeOptions()

# Using a random user-agent
options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{''.join(random.choices(string.digits, k=2))}.0.{''.join(random.choices(string.digits, k=4))}.{''.join(random.choices(string.digits, k=3))} Safari/537.36")

# Random window size
width = random.randint(800, 1200)
height = random.randint(600, 900)
options.add_argument(f"window-size={width},{height}")

# Generate a random profile directory
random_profile = random_string()
options.add_argument(f"user-data-dir=./profiles/{random_profile}")

# Initialize Chrome driver with options
driver = uc.Chrome(options=options)

# Open some website
driver.get('https://www.google.com')

# Wait for 30 seconds
time.sleep(30)

# Finally, close the browser
driver.quit()
