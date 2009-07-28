#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
# @license: GPLv3
#

import os
import pkg_resources

# General applications informations
APPNAME = "Kaptan"
VERSION = "0.1"
WEBSITE = "http://www.gokmengorgen.net"
AUTHORS = """\
Gökmen Görgen, <gkmngrgn@gmail.com>
"""
TRANSLATOR_CREDITS = """\
translator-credits
"""
COPYRIGHT = "Copyright \302\251 2009 Gökmen Görgen, <gkmngrgn@gmail.com>"
LICENSE = """\
Pardus Kaptan lets you configure your desktop on first login.
%s

Kaptan is a free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

Pati is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.\
""" % COPYRIGHT
SUMMARY = "Pardus Captain"

# Common functions
def get_file(filename):
    return pkg_resources.resource_filename('kaptan_xfce',
                                            os.path.join('ui', filename))
