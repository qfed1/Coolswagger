import gi
import time
import csv
import pandas as pd
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

    def on_send_button_clicked(self, widget):
        phone_number = self.phone_number_entry.get_text()
        message = self.message_entry.get_text()
        self.send_message(phone_number, message)

    def on_open_csv_button_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self,
            action=Gtk.FileChooserAction.OPEN,
            buttons=("Open", Gtk.ResponseType.OK, "Cancel", Gtk.ResponseType.CANCEL)
        )

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            self.load_csv(dialog.get_filename())
            self.process_csv_button.set_sensitive(True)

        dialog.destroy()

    def on_process_csv_button_clicked(self, widget):
        start_row = int(input("Enter the row number to start from (0-based index): "))
        while True:
            try:
                for index, row in self.df.iloc[start_row:].iterrows():
                    phone_number = row.iloc[0]  # First column
                    message = row.iloc[1]  # Second column
                    self.send_message(str(phone_number), str(message))
            except Exception as e:
                print(f"Exception occurred: {e}")
                input("Press ENTER to continue...")
            else:
                break

    def load_csv(self, file_path):
        self.df = pd.read_csv(file_path)

    def send_message(self, phone_number, message):
        if phone_number in self.sent_messages:
            dialog = Gtk.MessageDialog(
                transient_for=self,
                flags=0,
                message_type=Gtk.MessageType.WARNING,
                buttons=Gtk.ButtonsType.YES_NO,
                text=f"A message was already sent to {phone_number}. Do you still want to send another message?",
            )
            response = dialog.run()
            dialog.destroy()

            if response == Gtk.ResponseType.NO:
                return

        try:
            gm.send_message(phone_number, message)
            self.sent_messages[phone_number] = message
            with open(self.sent_messages_file, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([phone_number, message])
            print(f"Successfully sent message to: {phone_number}")
        except Exception as e:
            print(f"Exception occurred: {e}")

win = MessageSenderAndCSVReaderWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
