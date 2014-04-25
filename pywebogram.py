#!/usr/bin/env python3

import os
import sys
from gi.repository import Gtk, WebKit

class pyWebogram:
    
    def __init__(self):
        self.view = WebKit.WebView()

        settings = self.view.get_settings()
        settings.set_property('enable-file-access-from-file-uris', True)
        settings.set_property('enable-webaudio', True)
        settings.set_property('default-encoding', 'utf-8')
        settings.set_property('enable-universal-access-from-file-uris', True)
        
        self.window = Gtk.Window()

        self.window.set_title('pyWebogram')
        self.window.set_resizable(False) # D-D-D-DROP THE RESIZE
        self.window.connect("delete-event", Gtk.main_quit)
        self.window.set_icon_from_file(os.path.dirname(os.path.realpath(__file__)) + '/webogram/app/favicon.ico')
        
        self.window.add(self.view)

    def _js(self, code):
        self.view.execute_script(code)

    def run(self):
        self.view.set_size_request(800,400)
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.show_all()
        self.view.open(os.path.join('file://', os.path.dirname(os.path.realpath(__file__)), 'webogram/app/index.html'))
        Gtk.main()


if __name__ == '__main__':
    webo = pyWebogram()
    webo.run()
