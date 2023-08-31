import gi
import time
import csv
import google_messages
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

gm = google_messages.GoogleMessages()

class MessageSenderAndCSVReaderWindow(Gtk.Window):
    
        # ... (previous code)

    def __init__(self):
        # ... (previous code)
        
        # Add this line to initialize a list to store the CSV data
        self.csv_data = []

        # ... (rest of the code)

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

    def load_csv(self, file_path):
        self.csv_data.clear()  # Clear the existing data

        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                self.csv_data.append(row[:2])  # Add the data to self.csv_data

    def on_process_csv_button_clicked(self, widget):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text="Would you like to skip the header row of the CSV file?",
        )
        dialog.format_secondary_text(
            "Please be sure to answer correctly, as the header row usually contains column names instead of valid data."
        )
        response = dialog.run()

        start_index = 1 if response == Gtk.ResponseType.YES else 0
        dialog.destroy()

        for row in self.csv_data[start_index:]:  # Use self.csv_data instead of self.list_store
            phone_number, message = row
            self.send_message(phone_number, message)

    # ... (rest of your code)


    def load_csv(self, file_path):
        self.list_store.clear()

        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                self.list_store.append(row[:2])

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
        except Exception as e:
            print(f"Exception occurred: {e}")
            time.sleep(10)


win = MessageSenderAndCSVReaderWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
