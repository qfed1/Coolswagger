import gi
import time
import google_messages

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

gm = google_messages.GoogleMessages()

class MessageSenderWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Google Message Sender")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.phone_number_entry = Gtk.Entry()
        self.phone_number_entry.set_text("303 888 3096")
        vbox.pack_start(self.phone_number_entry, True, True, 0)

        self.message_entry = Gtk.Entry()
        self.message_entry.set_text("This works fam")
        vbox.pack_start(self.message_entry, True, True, 0)

        self.button = Gtk.Button(label="Send Message")
        self.button.connect("clicked", self.on_button_clicked)
        vbox.pack_start(self.button, True, True, 0)

    def on_button_clicked(self, widget):
        phone_number = self.phone_number_entry.get_text()
        message = self.message_entry.get_text()
        try:
            gm.send_message(phone_number, message)
        except Exception as e:
            print(f"Exception occurred: {e}")
            # This delay has been kept here to mimic the original script but may not be necessary.
            time.sleep(10)  

win = MessageSenderWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
