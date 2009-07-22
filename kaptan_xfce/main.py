#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import gobject
import gtk

import webkit

gobject.threads_init()

class MainWindow:
    def __init__(self):
        self.mainView = webkit.WebView()

        self.builder = gtk.Builder()
        self.builder.add_from_file('kaptan_xfce/ui/main.glade')
        self.builder.connect_signals({
            'gtk_main_quit': gtk.main_quit,
            })

        self.mainWindow = self.builder.get_object('mainWindow')
        self.mainWindow.fullscreen()
        self.mainWindow.add(self.content())

        self.mainWindow.show_all()
        
    def content(self):
        self.mainView = webkit.WebView()
        self.mainView.open("file:///usr/share/doc/midori/user/midori.html")

        return self.mainView

    def main(self):
        gtk.main()
