#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import gtk

class SidebarMenu:
    def __init__(self, builder):
        view = builder.get_object('textview')
        buffer = view.get_buffer()

        self.create_tags(buffer)
        self.insert_text(buffer)

    def create_tags(self, text_buffer):
        import pango

        text_buffer.create_tag("normal", size = 15 * pango.SCALE)
        text_buffer.create_tag("bigger", weight=pango.WEIGHT_BOLD, size=15 * pango.SCALE)

    def insert_text(self, text_buffer):
        iter = text_buffer.get_iter_at_offset(0)

        x = self.verticalMenu()

        text_buffer.insert(iter, x, -1)

        start, end = text_buffer.get_bounds()
        text_buffer.apply_tag_by_name("normal", start, end)

        text_buffer.insert_with_tags_by_name(iter, "\nHello Again! «", "bigger")
        
    def verticalMenu(self):
        menu_list = ["Welcome! «", "Mouse «", "Themes «", "Menu «", "Wallpaper «",
                     "Package «", "Summary «", "Good Bye! «"]

        return '\n'.join(menu_list)
