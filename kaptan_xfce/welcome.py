#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import gtk

class Welcome:
    def __init__(self, builder):
        widget = builder.get_object('content_vbox')

        hbox = gtk.HBox(homogeneous = False, spacing = 0)
        widget.pack_start(hbox, expand = False, fill = True, padding = 0)
        
        self.welcome_label(hbox)
        self.welcome_image(hbox)

    def welcome_label(self, widget):
        label = gtk.Label()
        label.set_markup("This application, called Kaptan Desktop, will"
            " help you with your basic but sufficient setup for your"
            " Pardus desktop in a quick manner. Please click Next to"
            " personalize your desktop.\n\n"
            "Pardus is a GNU / Linux distribution, targeting at"
            " computer literate users' basic desktop needs; helps you"
            " connect to internet, read e-mails, work with office"
            " documents and more!")
        label.set_line_wrap(True)

        widget.add(label)
        
    def welcome_image(self, widget):
        from common import get_file

        image = gtk.Image()
        image.set_from_file(get_file('kaptan_welcome.png'))
        
        widget.add(image)
