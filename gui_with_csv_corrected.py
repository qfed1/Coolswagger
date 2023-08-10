
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

        self.layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.layout)

        # Single message sender section
        self.single_message_section = self.create_single_message_section()
        self.layout.pack_start(self.single_message_section, True, True, 0)

        # Horizontal box for two tables
        self.csv_tables_layout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        
        # Create two CSV loading tables side by side
        self.table1 = self.create_csv_table(self.csv_handler1)
        self.table2 = self.create_csv_table(self.csv_handler2)

        self.csv_tables_layout.pack_start(self.table1, True, True, 0)
        self.csv_tables_layout.pack_start(self.table2, True, True, 0)

        self.layout.pack_start(self.csv_tables_layout, True, True, 0)

    def create_single_message_section(self):
        section_layout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        
        phone_number_entry = Gtk.Entry()
        message_entry = Gtk.Entry()
        send_button = Gtk.Button(label="Send Message")
        send_button.connect("clicked", self.send_single_message, phone_number_entry, message_entry)
        
        section_layout.pack_start(phone_number_entry, True, True, 0)
        section_layout.pack_start(message_entry, True, True, 0)
        section_layout.pack_start(send_button, True, True, 0)
        
        return section_layout

    def send_single_message(self, widget, phone_number_entry, message_entry):
        phone_number = phone_number_entry.get_text()
        message = message_entry.get_text()
        self.csv_handler1.write_to_csv(phone_number, message)
        self.csv_handler1.send_message(phone_number, message)

    def create_csv_table(self, csv_handler):
        table_layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        csv_file_entry = Gtk.Entry()
        load_button = Gtk.Button(label="Load CSV")
        send_bulk_button = Gtk.Button(label="Send Bulk Messages")
        
        load_button.connect("clicked", self.load_csv, csv_file_entry, csv_handler)
        send_bulk_button.connect("clicked", self.send_bulk_messages, csv_handler)
        
        table_layout.pack_start(csv_file_entry, True, True, 0)
        table_layout.pack_start(load_button, True, True, 0)
        table_layout.pack_start(send_bulk_button, True, True, 0)
        
        return table_layout

    def load_csv(self, widget, csv_file_entry, csv_handler):
        csv_file = csv_file_entry.get_text()
        # Logic to load CSV file (not fully implemented here)
        pass

    def send_bulk_messages(self, widget, csv_handler):
        # Logic to send bulk messages based on loaded CSV data
        pass

if __name__ == "__main__":
    window = MessageSenderAndCSVReaderWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()
