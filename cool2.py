import google_messages
import time

gm = google_messages.GoogleMessages()

while True:
    try:
        gm.send_message('303 888 3096', 'This works fam')
        time.sleep(5)  # wait for a while before sending the next message
    except Exception as e:
        print(f"Exception occurred: {e}")
        time.sleep(10)  # wait for a while before retrying
