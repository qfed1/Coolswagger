
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class HelloWorldWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        
        label = Gtk.Label(label="Hello, World!")
        self.add(label)

win = HelloWorldWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
