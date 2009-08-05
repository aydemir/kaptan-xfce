#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import os
import gtk

from common import getFile

class MainWindow:
    def __init__(self):
        self.page_number = 0

        self.builder = gtk.Builder()
        self.builder.add_from_file(getFile('kaptan-xfce.glade'))
        self.builder.connect_signals({
            'gtk_main_quit': gtk.main_quit,
            'on_about_button_clicked': self.aboutDialog,
            'on_button_next_clicked': self.nextPage,
            'on_button_previous_clicked': self.previousPage,
            })

        self.main_window = self.builder.get_object('main_window')
        self.main_window.show_all()

        self.content(self.builder, self.page_number)

    def quit(self):
        gtk.main_quit()

    def content(self, builder, id):
        widget = builder.get_object('content_vbox')
        
        #~ if id == 0:
            #~ from welcome import Welcome
#~ 
            #~ Welcome(widget)
#~ 
        #~ elif id == 1:
            #~ from setting_wallpaper import WallpaperSettings
#~ 
            #~ widget.remove(vbox)
#~ 
            #~ WallpaperSettings(widget)
            
        #~ else:
            #~ print('bu kadar yeter şimdilik')
            #~ exit(1)

        #~ self.sidebarMenu(builder, id)

    def sidebarMenu(self, builder, page_number):
        from sidebarmenu import SidebarMenu

        SidebarMenu(builder, page_number)

    def aboutDialog(self, widget = None):
        from aboutdialog import AboutDialog

        AboutDialog()

    def nextPage(self, widget = None):
        self.page_number = self.page_number + 1
        
        self.content(self.builder, self.page_number)

    def previousPage(self, widget = None):
        if not self.page_number == 0:
            self.page_number = self.page_number - 1

    def main(self):
        gtk.main()
