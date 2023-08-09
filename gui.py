
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from backend import CSVHandler

class MessageSenderAndCSVReaderWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Google Message Sender and CSV Reader")
        
        # Initialize two CSVHandler instances
        self.csv_handler1 = CSVHandler("sent_messages1.csv")
        self.csv_handler2 = CSVHandler("sent_messages2.csv")

        self.layout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.add(self.layout)

        # Create two tables side by side
        self.table1 = self.create_table(self.csv_handler1)
        self.table2 = self.create_table(self.csv_handler2)

        self.layout.pack_start(self.table1, True, True, 0)
        self.layout.pack_start(self.table2, True, True, 0)

    def create_table(self, csv_handler):
        table_layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        phone_number_entry = Gtk.Entry()
        message_entry = Gtk.Entry()
        send_button = Gtk.Button(label="Send Message")
        send_button.connect("clicked", self.send_message, phone_number_entry, message_entry, csv_handler)
        
        table_layout.pack_start(phone_number_entry, True, True, 0)
        table_layout.pack_start(message_entry, True, True, 0)
        table_layout.pack_start(send_button, True, True, 0)
        
        return table_layout

    def send_message(self, widget, phone_number_entry, message_entry, csv_handler):
        phone_number = phone_number_entry.get_text()
        message = message_entry.get_text()
        csv_handler.write_to_csv(phone_number, message)
        csv_handler.send_message(phone_number, message)

if __name__ == "__main__":
    window = MessageSenderAndCSVReaderWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()
