import gi
import time
import csv
import google_messages

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

gm = google_messages.GoogleMessages()

class MessageSenderWindow(Gtk.Window):
    # ... Existing Code ...

class CSVReaderWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="CSV Reader")

        self.layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.layout)

        self.button = Gtk.Button(label="Open CSV")
        self.button.connect("clicked", self.on_button_clicked)
        self.layout.pack_start(self.button, True, True, 0)

        self.list_store = Gtk.ListStore(str, str)
        self.tree_view = Gtk.TreeView(self.list_store)

        for i, column_title in enumerate(["Column 1", "Column 2"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.tree_view.append_column(column)

        self.layout.pack_start(self.tree_view, True, True, 0)

    def on_button_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self,
            action=Gtk.FileChooserAction.OPEN,
            buttons=("Open", Gtk.ResponseType.OK, "Cancel", Gtk.ResponseType.CANCEL)
        )

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            self.load_csv(dialog.get_filename())

        dialog.destroy()

    def load_csv(self, file_path):
        self.list_store.clear()

        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                self.list_store.append(row[:2])

win = MessageSenderWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

csv_win = CSVReaderWindow()
csv_win.connect("destroy", Gtk.main_quit)
csv_win.show_all()

Gtk.main()
