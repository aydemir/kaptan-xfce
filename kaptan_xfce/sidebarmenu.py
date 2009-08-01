#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import gtk

class SidebarMenu:
    def __init__(self, builder, page_number):
        view = builder.get_object('textview')
        buffer = view.get_buffer()

        self.create_tags(buffer)
        self.insert_menu(buffer, page_number)

    def create_tags(self, text_buffer):
        import pango

        text_buffer.create_tag("normal", size = 15 * pango.SCALE)
        text_buffer.create_tag("bigger", weight=pango.WEIGHT_BOLD, size=15 * pango.SCALE)

    def insert_menu(self, text_buffer, page_number):
        menu_list = ["Welcome!", "Mouse", "Themes", "Menu", "Wallpaper",
                     "Package", "Summary", "Good Bye!"]

        iter = text_buffer.get_iter_at_offset(0)

        for menu in menu_list:
            if menu == menu_list[page_number]:
                text_buffer.insert_with_tags_by_name(iter, '%s «\n' % menu, 'bigger')
                
            else:
                text_buffer.insert_with_tags_by_name(iter, '%s «\n' % menu, 'normal')
