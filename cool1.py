import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
import time

options = uc.ChromeOptions()
options.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
driver = uc.Chrome(options=options)

driver.get('https://messages.google.com/web/authentication')

# wait for URL change
while True:
    if driver.current_url == "https://messages.google.com/web/conversations":
        break
    time.sleep(5)

# click start chat button
start_chat_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-e2e-start-button]")))
start_chat_button.click()

# add number to input field
number_input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-e2e-contact-input]")))
number_input_field.send_keys("111 111 1111")

# press send to button
send_to_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-e2e-send-to-button]")))
send_to_button.click()

# input message into textarea
# ... the rest of your code

# input message into textarea
message_input_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@data-e2e-message-input-box]")))
message_input_field.send_keys("test")

# send the message
try:
    send_sms_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-e2e-send-text-button and not(@disabled)]")))
    send_sms_button.click()
except ElementNotInteractableException:
    print("Button is not interactable at the moment.")

# Keep the webdriver open
while True:
    time.sleep(5)
