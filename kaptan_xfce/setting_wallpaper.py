#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import gobject
import gtk
import os

from glob import glob
from string import capitalize

class WallpaperInformation:
    def __init__(self, widget):
        widget.hide_all()

        self.image(widget)
        self.label(widget)

    def image(self, widget):
        from common import getFile
        
        image = gtk.Image()
        image.set_from_file(getFile('wallpaper.png'))
        
        widget.pack_start(image, expand = False, fill = False, padding = 0)

    def label(self, widget):
        label = gtk.Label()
        label.set_markup("Infromation about WallpaperSettings. ")
        label.set_line_wrap(True)
        
        widget.pack_start(label, expand = False, fill = False)

class Columns:
    (IMAGE, NAME, DESCRIPTION) = range(3)

class WallpaperSettings:
    def __init__(self, widget):
        wallpapers = '/usr/share/xfce4/backdrops/*'
        self.list_wallpaper = glob(wallpapers)
        self.thumbnails = {}
        for image in self.list_wallpaper:
            # FIX ME!
            wallpaper = gtk.gdk.pixbuf_new_from_file(image)
            self.thumbnails[image] = wallpaper.scale_simple(72, 72, gtk.gdk.INTERP_BILINEAR)

        hbox = gtk.HBox(homogeneous = False, spacing = 5)
        widget.pack_start(hbox, expand = True, fill = True, padding = 0)

        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        hbox.pack_start(sw, expand = True, fill = True, padding = 0)

        # create tree model
        model = self.__create_model()

        # create tree view
        treeview = gtk.TreeView(model)
        treeview.set_rules_hint(True)
        treeview.set_search_column(Columns.NAME)
        treeview.set_property('headers-visible', False)
        treeview.set_property('enable-search', False)
        treeview.connect('cursor-changed', self.actions)

        sw.add(treeview)

        # add columns to the tree view
        self.__add_columns(treeview)
        
        vbox = gtk.VBox(homogeneous = False, spacing = 0)
        hbox.pack_end(vbox, expand = False, fill = False, padding = 0)

        WallpaperInformation(vbox)

    def __create_model(self):
        lstore = gtk.ListStore(gobject.TYPE_OBJECT,
                               gobject.TYPE_STRING,
                               gobject.TYPE_STRING)

        for item in self.list_wallpaper:
            iter = lstore.append()
            lstore.set(iter, Columns.IMAGE, self.thumbnails[item],
                             Columns.NAME, os.path.split(item)[1],
                             Columns.DESCRIPTION, item)

        return lstore

    def __add_columns(self, treeview):
        renderer = gtk.CellRendererPixbuf()
        column = gtk.TreeViewColumn("Image", renderer)
        column.set_cell_data_func(renderer, self.__cell_renderer_image)
        treeview.append_column(column)

        renderer = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Name", renderer, text = Columns.NAME)
        column.set_cell_data_func(renderer, self.__cell_renderer_message)
        treeview.append_column(column)

    def __cell_renderer_image(self, column, cell, store, position):
        image = store.get_value(position, Columns.IMAGE)

        cell.set_property('pixbuf', image)

    def __cell_renderer_message(self, column, cell, store, position):
        image_name = store.get_value(position, Columns.NAME)
        image_name = capitalize(image_name.replace('.png', '').replace('-', ' '))
        image_path = store.get_value(position, Columns.DESCRIPTION)
        markup = "<b>%s</b>\n<small>%s</small>" % (image_name, image_path)

        cell.set_property('markup', markup)

    def actions(self, treeview, data = None):
        # FIX ME!
        cursor = treeview.get_cursor()

        print('clicked %s.' % self.list_wallpaper[cursor[0][0]])
