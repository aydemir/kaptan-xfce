#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import os
import gtk

from aboutdialog import AboutDialog

class MainWindow:
    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file('kaptan_xfce/ui/kaptan-xfce.glade')
        self.builder.connect_signals({
            'on_about_button_clicked': self.aboutdialog,
            'gtk_main_quit': gtk.main_quit,
            })

        self.mainWindow = self.builder.get_object('mainWindow')
        self.mainWindow.fullscreen()

        self.mainWindow.show_all()

    def aboutdialog(self, widget = None):
        AboutDialog()

    def quit(self):
        gtk.main_quit()

    def main(self):
        gtk.main()
