import gi
import time
import csv
import google_messages
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

gm = google_messages.GoogleMessages()

class MessageSenderAndCSVReaderWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Google Message Sender and CSV Reader")
        self.sent_messages_file = "sent_messages.csv"

        if not os.path.exists(self.sent_messages_file):
            with open(self.sent_messages_file, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['Phone Number', 'Message'])

        self.sent_messages = {}
        with open(self.sent_messages_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  
            for row in reader:
                self.sent_messages[row[0]] = row[1]

        self.layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.layout)

        self.phone_number_entry = Gtk.Entry()
        self.phone_number_entry.set_text("303 888 3096")
        self.layout.pack_start(self.phone_number_entry, True, True, 0)

        self.message_entry = Gtk.Entry()
        self.message_entry.set_text("This works fam")
        self.layout.pack_start(self.message_entry, True, True, 0)

        self.send_button = Gtk.Button(label="Send Message")
        self.send_button.connect("clicked", self.on_send_button_clicked)
        self.layout.pack_start(self.send_button, True, True, 0)

        self.open_csv_button = Gtk.Button(label="Open CSV")
        self.open_csv_button.connect("clicked", self.on_open_csv_button_clicked)
        self.layout.pack_start(self.open_csv_button, True, True, 0)

        self.process_csv_button = Gtk.Button(label="Process CSV")
        self.process_csv_button.connect("clicked", self.on_process_csv_button_clicked)
        self.layout.pack_start(self.process_csv_button, True, True, 0)
        self.process_csv_button.set_sensitive(False) 

        self.list_store = Gtk.ListStore(str, str)