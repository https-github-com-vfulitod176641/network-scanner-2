#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2008 Adriano Monteiro Marques
#
# Author: Francesco Piccinno <stack.box@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

from umit.plugin.Containers import setup

setup(
    name='Context menu',
    version='1.0',
    author='Francesco Piccinno',
    url='http://snippets.pornosecurity.org',
    start_file='main',
    provides='=context-menu-1.0',
    description='a context menu for host list',
    scripts=['sources/main.py'],
    data_files=[('data', ['dist/logo.png'])],
    output='ContextMenu.ump'
)
