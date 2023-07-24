import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options = uc.ChromeOptions()

# in case you need to set a specific user agent
options.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'

# start chrome
driver = uc.Chrome(options=options)

driver.get('https://messages.google.com/web/authentication')

target_url = 'https://messages.google.com/web/conversations'

# flag to check if button has been clicked
button_clicked = False

# an infinite loop to keep the browser open
while True:
    # wait for 5 seconds
    time.sleep(5)

    # check if URL has changed to the target_url
    if driver.current_url == target_url and not button_clicked:
        print('Link changed to:', target_url)
        try:
            # wait for the button to be clickable and then click it
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Start chat')]")))
            button.click()
            button_clicked = True  # set the flag to True after clicking the button
            print('Button clicked')

            # wait for the input to be available and then type into it
            input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type a name, phone number, or email']")))
            input_field.send_keys('303 888 3096')
            print('Input filled')

            # wait for the send button to be clickable and then click it
            send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-e2e-send-to-button]")))
            send_button.click()
            print('Send button clicked')

            # wait for the textarea to be available and then type into it
            textarea_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Text message']")))
            textarea_field.send_keys('test')
            print('Textarea filled')

            # wait for the send SMS button to be clickable and then click it
            send_sms_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'send-button')))
            send_sms_button.click()

            print('Send SMS button clicked')
        except Exception as e:
            print('Could not find or click on the button or fill the input or textarea:', str(e))
    elif button_clicked:
        # do something after the button has been clicked, or do nothing to just keep the browser open
        pass
