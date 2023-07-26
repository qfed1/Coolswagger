import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
import time

class GoogleMessages:
    def __init__(self, url='https://messages.google.com/web/authentication'):
        options = uc.ChromeOptions()
        options.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
        self.driver = uc.Chrome(options=options)
        self.url = url
        self.authenticate()

    def authenticate(self):
        while True:
            try:
                self.driver.get(self.url)
                while True:
                    if self.driver.current_url == "https://messages.google.com/web/conversations":
                        break
                    time.sleep(5)
                break  # exit the loop if no exceptions were thrown
            except Exception as e:
                print(f"Exception occurred: {e}")
                time.sleep(10)  # wait a bit before retrying

    def send_message(self, phone_number, message_text):
        try:
            # click start chat button
            start_chat_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-e2e-start-button]")))
            start_chat_button.click()

            # add number to input field
            number_input_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-e2e-contact-input]")))
            number_input_field.send_keys(phone_number)

            # press send to button
            send_to_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-e2e-send-to-button]")))
            send_to_button.click()

            # input message into textarea
            message_input_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@data-e2e-message-input-box]")))
            message_input_field.send_keys(message_text)

            # send the message with ENTER key
            message_input_field.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Exception occurred: {e}")
