#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import gtk

class Welcome:
    def __init__(self, widget):
        vbox = gtk.VBox(homogeneous = False, spacing = 0)
        widget.pack_start(vbox, expand = True, fill = True, padding = 0)

        self.welcomeImage(vbox)
        self.welcomeLabel(vbox)

    def welcomeImage(self, widget):
        from common import getFile

        image = gtk.Image()
        image.set_from_file(getFile('kaptan_welcome.png'))
        widget.add(image)

    def welcomeLabel(self, widget):
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
