import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
import time
import os

class GoogleMessages:
    driver = None

    def __init__(self, url='https://messages.google.com/web/authentication'):
        if GoogleMessages.driver is None:
            if not self.is_driver_running():
                options = uc.ChromeOptions()
                options.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
                GoogleMessages.driver = uc.Chrome(options=options)
        self.url = url

    def is_driver_running(self):
        # check if 'chromedriver' is currently running on system
        output = os.popen('pgrep -x chromedriver').read()
        return True if output else False

    def authenticate(self):
        self.driver.get(self.url)
        while True:
            if self.driver.current_url == "https://messages.google.com/web/conversations":
                break
            time.sleep(5)

    def send_message(self, phone_number, message_text):
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

        # send the message
        try:
            send_sms_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "floating-button")))
            send_sms_button.click()
        except ElementNotInteractableException:
            print("Button is not interactable at the moment.")
