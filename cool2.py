import gi
import time
import csv
import google_messages

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

gm = google_messages.GoogleMessages()

class MessageSenderAndCSVReaderWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Google Message Sender and CSV Reader")

        self.layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.layout)

        # Message sender interface
        self.phone_number_entry = Gtk.Entry()
        self.phone_number_entry.set_text("303 888 3096")
        self.layout.pack_start(self.phone_number_entry, True, True, 0)

        self.message_entry = Gtk.Entry()
        self.message_entry.set_text("This works fam")
        self.layout.pack_start(self.message_entry, True, True, 0)

        self.send_button = Gtk.Button(label="Send Message")
        self.send_button.connect("clicked", self.on_send_button_clicked)
        self.layout.pack_start(self.send_button, True, True, 0)

        # CSV reader interface
        self.open_csv_button = Gtk.Button(label="Open CSV")
        self.open_csv_button.connect("clicked", self.on_open_csv_button_clicked)
        self.layout.pack_start(self.open_csv_button, True, True, 0)

        self.process_csv_button = Gtk.Button(label="Process CSV")
        self.process_csv_button.connect("clicked", self.on_process_csv_button_clicked)
        self.layout.pack_start(self.process_csv_button, True, True, 0)
        self.process_csv_button.set_sensitive(False)  # Initially disabled

        self.list_store = Gtk.ListStore(str, str)
        self.tree_view = Gtk.TreeView(self.list_store)

        for i, column_title in enumerate(["Column 1", "Column 2"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.tree_view.append_column(column)

        self.layout.pack_start(self.tree_view, True, True, 0)

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
            self.process_csv_button.set_sensitive(True)  # Enable processing button after loading CSV

        dialog.destroy()

    def on_process_csv_button_clicked(self, widget):
        for row in self.list_store:
            phone_number, message = row
            self.send_message(phone_number, message)

    def load_csv(self, file_path):
        self.list_store.clear()

        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                self.list_store.append(row[:2])

    def send_message(self, phone_number, message):
        try:
            gm.send_message(phone_number, message)
        except Exception as e:
            print(f"Exception occurred: {e}")
            time.sleep(10)


win = MessageSenderAndCSVReaderWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
