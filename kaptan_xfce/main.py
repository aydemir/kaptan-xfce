#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import os
import gtk

from aboutdialog import AboutDialog
from common import get_file

class MainWindow:
    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file(get_file('kaptan-xfce.glade'))
        self.builder.connect_signals({
            'on_about_button_clicked': self.aboutDialog,
            'gtk_main_quit': gtk.main_quit,
            })

        self.main_window = self.builder.get_object('main_window')
        self.main_window.fullscreen()

        self.content(self.builder)

        self.main_window.show_all()

    def aboutDialog(self, widget = None):
        AboutDialog()

    def quit(self):
        gtk.main_quit()

    def content(self, builder):
        hbox = builder.get_object('content_hbox')

        content_label = gtk.Label('Content Label')
        self.verticalMenu(builder, hbox)

        hbox.pack_end(content_label)

    def verticalMenu(self, builder, hbox):
        menu_items = ["<big><b>Welcome!</b></big>", "Mouse", "Themes", "Menu", \
                      "Wallpaper", "Package", "Summary", "Good Bye!"]

        vertical_menu_label = gtk.Label()
        vertical_menu_label.set_markup('» %s' % '\n'.join(menu_items))

        hbox.pack_start(vertical_menu_label, expand = 0,
                        fill = 0, padding = 5)

    def main(self):
        gtk.main()
