#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import gtk

from common import SUMMARY, APPNAME, AUTHORS, TRANSLATORS, VERSION, \
                    LICENSE, COPYRIGHT, WEBSITE

class AboutDialog(gtk.AboutDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()

        self.set_comments(SUMMARY)
        self.set_name(APPNAME)
        self.set_authors(AUTHORS.split('\n'))
        #~ self.set_translator_credits(TRANSLATORS.split('\n'))
        self.set_version(VERSION)
        self.set_license(LICENSE)
        self.set_website(WEBSITE)
        self.set_copyright(COPYRIGHT)
#~ self.set_logo(gtk.gdk.pixbuf_new_from_file(get_pixmap("kaptan.png")))
#~ self.set_icon(gtk.gdk.pixbuf_new_from_file(get_pixmap("kaptan.png")))

        self.show_all()
        self.run()
        self.destroy()
