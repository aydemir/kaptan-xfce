#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import gtk

# FIX ME: Url show does not work.
#~ from gnome import url_show
from common import getFile
from common import SUMMARY, APPNAME, AUTHORS, TRANSLATOR_CREDITS, \
                    VERSION, LICENSE, COPYRIGHT, WEBSITE

class AboutDialog(gtk.AboutDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()

        self.set_comments(SUMMARY)
        self.set_name(APPNAME)
        self.set_authors(AUTHORS.split('\n'))
        self.set_translator_credits(TRANSLATOR_CREDITS)
        self.set_version(VERSION)
        self.set_license(LICENSE)
        #~ gtk.about_dialog_set_url_hook(lambda self, url: url_show(url))
        self.set_website(WEBSITE)
        self.set_website_label(WEBSITE)
        self.set_copyright(COPYRIGHT)
        self.set_logo(gtk.gdk.pixbuf_new_from_file(getFile("kaptan-logo.png")))
        self.set_icon(gtk.gdk.pixbuf_new_from_file(getFile("kaptan-logo.png")))

        self.show_all()
        self.run()
        self.destroy()
