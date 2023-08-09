
import csv
import google_messages
import os

gm = google_messages.GoogleMessages()

class CSVHandler:
    def __init__(self, csv_filename="sent_messages.csv"):
        self.sent_messages_file = csv_filename
        if not os.path.exists(self.sent_messages_file):
            with open(self.sent_messages_file, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['Phone Number', 'Message'])
        self.sent_messages = self.read_csv()

    def read_csv(self):
        sent_messages = {}
        with open(self.sent_messages_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  
            for row in reader:
                sent_messages[row[0]] = row[1]
        return sent_messages

    def write_to_csv(self, phone_number, message):
        with open(self.sent_messages_file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([phone_number, message])

    def send_message(self, phone_number, message):
        gm.send_message(phone_number, message)
