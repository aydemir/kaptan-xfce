#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import os
import gtk

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

    def quit(self):
        gtk.main_quit()

    def content(self, builder):
        from welcome import Welcome
        
        Welcome(builder)

        self.sidebarMenu(builder, 3)

    def sidebarMenu(self, builder, page_number):
        from sidebarmenu import SidebarMenu

        SidebarMenu(builder, page_number)

    def aboutDialog(self, widget = None):
        from aboutdialog import AboutDialog

        AboutDialog()

    def main(self):
        gtk.main()
