from google_messages import GoogleMessages

def main():
    gm = GoogleMessages()
    gm.authenticate()
    gm.send_message('303 888 3096', 'This is a test message')

if __name__ == "__main__":
    main()
