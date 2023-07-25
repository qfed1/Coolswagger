from google_messages import GoogleMessages

gm = GoogleMessages()
gm.authenticate()
gm.send_message('303 888 3096', 'This works fam')
