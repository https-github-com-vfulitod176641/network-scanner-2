#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005-2006 Insecure.Com LLC.
# Copyright (C) 2007-2008 Adriano Monteiro Marques
#
# Author: Adriano Monteiro Marques <adriano@umitproject.org>
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import gtk

from higwidgets.higexpanders import HIGExpander
from higwidgets.higboxes import HIGVBox, HIGHBox, hig_box_space_holder
from higwidgets.higlabels import HIGEntryLabel
from higwidgets.higtables import HIGTable

from umit.gui.Icons import get_os_logo

from umit.core.I18N import _

na = _('Not available')

class ScanHostDetailsPage(HIGExpander):
    def __init__(self, label):
        HIGExpander.__init__(self, label)
        
        self.host_details = HostDetails()
        self.hbox._pack_expand_fill(self.host_details)

class HostDetails(HIGVBox):
    os_table = None
    os_hbox = None

    def __init__(self):
        HIGVBox.__init__(self)
        
        self.__create_widgets()
    
    def __create_widgets(self):
        self.host_status_expander = gtk.Expander('<b>'+_('Host Status')+'</b>')
        self.address_expander = gtk.Expander('<b>'+_('Addresses')+'</b>')
        self.hostnames_expander = gtk.Expander('<b>'+_('Hostnames')+'</b>')
        self.os_expander = gtk.Expander('<b>'+_('Operating System')+'</b>')
        self.portsused_expander = gtk.Expander('<b>'+_('Ports used')+'</b>')
        self.osclass_expander = gtk.Expander('<b>'+_('OS Class')+'</b>')
        self.tcp_expander = gtk.Expander('<b>'+_('TCP Sequence')+'</b>')
        self.ip_expander = gtk.Expander('<b>'+_('IP ID Sequence')+'</b>')
        self.tcpts_expander = gtk.Expander('<b>'+_('TCP TS Sequence')+'</b>')
        self.comment_expander = gtk.Expander('<b>'+_('Comments')+'</b>')
        self.os_image = gtk.Image()
        self.vulnerability_image = gtk.Image()
        
        # Host Status expander
        self.host_state_label = HIGEntryLabel(_('State:'))
        self.info_host_state_label = HIGEntryLabel(na)
        
        self.open_label = HIGEntryLabel(_('Open ports:'))
        self.info_open_ports = HIGEntryLabel(na)
        
        self.filtered_label = HIGEntryLabel(_('Filtered ports:'))
        self.info_filtered_label = HIGEntryLabel(na)
        
        self.closed_label = HIGEntryLabel(_('Closed ports:'))
        self.info_closed_ports = HIGEntryLabel(na)
        
        self.scanned_label = HIGEntryLabel(_('Scanned ports:'))
        self.info_scanned_label = HIGEntryLabel(na)
        
        self.uptime_label = HIGEntryLabel(_('Up time:'))
        self.info_uptime_label = HIGEntryLabel(na)
        
        self.lastboot_label = HIGEntryLabel(_('Last boot:'))
        self.info_lastboot_label = HIGEntryLabel(na)
        
        
        # Addresses expander
        self.ipv4_label = HIGEntryLabel(_('IPv4:'))
        self.info_ipv4_label = HIGEntryLabel(na)
        
        self.ipv6_label = HIGEntryLabel(_('IPv6:'))
        self.info_ipv6_label = HIGEntryLabel(na)
        
        self.mac_label = HIGEntryLabel(_('MAC:'))
        self.info_mac_label = HIGEntryLabel(na)
        
        self.vendor_label = HIGEntryLabel(_('Vendor:'))
        self.info_vendor_label = HIGEntryLabel(na)
    
    def create_table_hbox(self):
        table = HIGTable()
        hbox = HIGHBox()
        
        hbox._pack_noexpand_nofill(hig_box_space_holder())
        hbox._pack_noexpand_nofill(table)
        
        return table, hbox
    
    def set_host_status(self, status):
        self.host_status_expander.set_use_markup(True)
        self.host_status_expander.set_expanded(True)
        table, hbox = self.create_table_hbox()
        
        try:
            if status['state'] == '': raise Exception
            self.info_host_state_label.set_text(status['state'])
        except:pass
        
        try:
            if status['open'] == '': raise Exception
            self.info_open_ports.set_text(status['open'])
        except:pass
        
        try:
            if status['filtered'] == '': raise Exception
            self.info_filtered_label.set_text(status['filtered'])
        except:pass
        
        try:
            if status['closed'] == '': raise Exception
            self.info_closed_ports.set_text(status['closed'])
        except:pass
        
        try:
            if status['scanned'] == '': raise Exception
            self.info_scanned_label.set_text(status['scanned'])
        except:pass
        
        try:
            if status['uptime'] == '': raise Exception
            self.info_uptime_label.set_text(status['uptime'])
        except:pass
        
        try:
            if status['lastboot'] == '': raise Exception
            self.info_lastboot_label.set_text(status['lastboot'])
        except:pass
        
        table.attach(self.host_state_label,0,1,0,1)
        table.attach(self.info_host_state_label,1,2,0,1)
        
        table.attach(self.open_label,0,1,1,2)
        table.attach(self.info_open_ports,1,2,1,2)
        
        table.attach(self.filtered_label,0,1,2,3)
        table.attach(self.info_filtered_label,1,2,2,3)
        
        table.attach(self.closed_label,0,1,3,4)
        table.attach(self.info_closed_ports,1,2,3,4)
        
        table.attach(self.scanned_label,0,1,4,5)
        table.attach(self.info_scanned_label,1,2,4,5)
        
        table.attach(self.uptime_label,0,1,5,6)
        table.attach(self.info_uptime_label,1,2,5,6)
        
        table.attach(self.lastboot_label,0,1,6,7)
        table.attach(self.info_lastboot_label,1,2,6,7)
        
        table.attach(self.os_image,2,4,0,3,xoptions=1,yoptions=0)
        table.attach(self.vulnerability_image,2,4,4,7,xoptions=1,yoptions=0)
        
        table.set_col_spacing(1, 50)
        
        self.host_status_expander.add(hbox)
        self._pack_noexpand_nofill(self.host_status_expander)

    def set_os_image(self, image):
        self.os_image.set_from_stock(image, gtk.ICON_SIZE_DIALOG)
    
    def set_vulnerability_image(self, image):
        self.vulnerability_image.set_from_stock(image, gtk.ICON_SIZE_DIALOG)

    def set_addresses(self, address):
        self.address_expander.set_use_markup(True)
        table, hbox = self.create_table_hbox()
        self.address_expander.set_expanded(True)
        
        #print '>>> Address:', address
        try:
            if address['ipv4'] == 1: raise Exception
            self.info_ipv4_label.set_text(address['ipv4'])
        except:pass
        
        try:
            if address['ipv6'] == 1: raise Exception
            self.info_ipv6_label.set_text(address['ipv6'])
        except:pass
        
        try:
            if address['mac'] == 1: raise Exception
            self.info_mac_label.set_text(address['mac'])
        except:pass
        
        table.attach(self.ipv4_label,0,1,0,1)
        table.attach(self.info_ipv4_label,1,2,0,1)
        
        table.attach(self.ipv6_label,0,1,1,2)
        table.attach(self.info_ipv6_label,1,2,1,2)
        
        table.attach(self.mac_label,0,1,2,3)
        table.attach(self.info_mac_label,1,2,2,3)
        
        self.address_expander.add(hbox)
        self._pack_noexpand_nofill(self.address_expander)
    
    def set_hostnames(self, hostname):
        if hostname:
            self.hostnames_expander.set_use_markup(True)
            self.hostnames_expander.set_expanded(True)
            table, hbox = self.create_table_hbox()
            
            y1 = 1
            y2 = 2
            
            for h in hostname:
                name = na
                try:name = h['hostname']
                except:pass
                
                type = na
                try:type = h['hostname_type']
                except:pass
                
                table.attach(HIGEntryLabel(_('Name - Type:')),0,1,y1,y2)
                table.attach(HIGEntryLabel(name+' - '+\
                                           type),1,2,y1,y2)
                y1+=1;y2+=1
            
            self.hostnames_expander.add(hbox)
            self._pack_noexpand_nofill(self.hostnames_expander)

    def os_selection_changed(self, widget):
        current_selection = widget.get_active_text()
        self.set_os_image(get_os_logo(current_selection))
        
        for os_match in self.current_os_list:
            if isinstance(os_match, dict) and \
               current_selection == os_match.get('name', None):
                self.os_progress.set_fraction(float(os_match['accuracy'])/100.0)
                self.os_progress.set_text(os_match['accuracy'] + "%")
                self.os_progress.set_sensitive(True)
                break
        else:
            self.os_progress.set_fraction(0.0)
            self.os_progress.set_text(_("Not Available"))
            self.os_progress.set_sensitive(False)

    def set_os_list(self, os_list, os_match):
        # Creating the main widgets for this section
        self.os_expander.set_use_markup(True)
        self.os_expander.set_expanded(True)
        self.os_table, self.os_hbox = self.create_table_hbox()
        self.os_progress = gtk.ProgressBar()
        
        # Setting the current match's details in the widgets
        if len(os_list) > 1:
            self.os_list = gtk.combo_box_new_text()
            
            model = self.os_list.get_model()
            [model.append([os['name']]) for os in os_list if os.has_key("name")]
            self.os_list.set_active(0)
            
            # In case we have the os selection changed, we need to change the
            # icon and the current accuracy. Also, we need to save the selection
            # in the usr result.
            self.os_list.connect("changed", self.os_selection_changed)
        else:
            self.os_list = HIGEntryLabel(os_match.get("name", "Not Available"))
        
        self.os_table.attach(HIGEntryLabel(_('Name:')), 0, 1, 0, 1)
        self.os_table.attach(self.os_list, 1, 2, 0, 1)
        
        # Setting current os_match accuracy
        if os_match.get("accuracy", ''):
            self.os_progress.set_fraction(float(os_match['accuracy']) / 100.0)
            self.os_progress.set_text(os_match['accuracy'] + '%')
            self.os_progress.set_sensitive(True)
        else:
            self.os_progress.set_sensitive(False)
            self.os_progress.set_text(_('Not Available'))
        
        self.os_table.attach(HIGEntryLabel(_('Accuracy:')), 0, 1, 1, 2)
        self.os_table.attach(self.os_progress, 1, 2, 1, 2)
        
        ###################
        ## Setting the list of matches and the list of ports used in the scan
        if os_match.has_key("portsused"):
            self.set_ports_used(os_match["portsused"])
            self.portsused_expander.set_sensitive(True)
        else:
            # In case we don't have any port, we still show the expander widget
            # but in a non-sensitive manner
            self.portsused_expander.set_sensitive(False)
        self.portsused_expander.set_use_markup(True)
        self.os_table.attach(self.portsused_expander, 0, 2, 2, 3)
        
        if os_match.has_key('osclass'):
            self.set_osclass(os_match['osclass'])
            self.osclass_expander.set_sensitive(True)
        else:
            self.osclass_expander.set_sensitive(False)
        self.osclass_expander.set_use_markup(True)
        self.os_table.attach(self.osclass_expander, 0, 2, 3, 4)
        
        self.os_expander.add(self.os_hbox)
        self._pack_noexpand_nofill(self.os_expander)
        
        # Saving os_list and os_match for latter access
        self.current_os_list = os_list
        self.current_os_match = os_match

    def set_ports_used(self, ports=None):
        # Removing old childs
        child = self.portsused_expander.get_child()
        if child is not None:
            self.portsused_expander.remove(child)
        
        if ports is None:
            self.portsused_expander.set_sensitive(False)
            return
        else:
            self.portsused_expander.set_sensitive(True)
        
        self.portsused_expander.set_use_markup(True)
        table, hbox = self.create_table_hbox()
        
        y1=0
        y2=1
        
        for p in ports:
            table.attach(HIGEntryLabel(_('Port-Protocol-State:')), 0, 1, y1, y2)
            table.attach(HIGEntryLabel(p['portid']+' - '+p['proto']+' - '+\
                                       p['state']), 1, 2, y1, y2)
            y1+=1
            y2+=1
        
        self.portsused_expander.add(hbox)

    def set_osclass(self, osclass=None):
        child = self.osclass_expander.get_child()
        if child is not None:
            self.osclass_expander.remove(child)
        
        if osclass is None:
            self.osclass_expander.set_sensitive(False)
            return
        else:
            self.osclass_expander.set_sensitive(True)
            self.osclass_expander.set_use_markup(True)
            table, hbox = self.create_table_hbox()
            
            table.attach(HIGEntryLabel(_('Type')),0,1,0,1)
            table.attach(HIGEntryLabel(_('Vendor')),1,2,0,1)
            table.attach(HIGEntryLabel(_('OS Family')),2,3,0,1)
            table.attach(HIGEntryLabel(_('OS Generation')),3,4,0,1)
            table.attach(HIGEntryLabel(_('Accuracy')),4,5,0,1)
            
            y1=1;y2=2
            
            for o in osclass:
                table.attach(HIGEntryLabel(o['type']),0,1,y1,y2)
                table.attach(HIGEntryLabel(o['vendor']),1,2,y1,y2)
                table.attach(HIGEntryLabel(o['osfamily']),2,3,y1,y2)
                table.attach(HIGEntryLabel(o.get('osgen', '')),3,4,y1,y2)
                
                progress = gtk.ProgressBar()
                progress.set_text(o['accuracy']+'%')
                progress.set_fraction(float(o['accuracy'])/100.0)
                table.attach(progress,4,5,y1,y2)
                y1+=1;y2+=1
            
            self.osclass_expander.add(hbox)
    
    def set_tcpseq(self, tcpseq):
        if tcpseq:
            self.tcp_expander.set_use_markup(True)
            table, hbox = self.create_table_hbox()

            combo = gtk.combo_box_new_text()
            for v in tcpseq['values'].split(','):
                combo.append_text(v)

            table.attach(HIGEntryLabel(_('Class:')),0,1,0,1)
            table.attach(HIGEntryLabel(tcpseq.get('class', '')),1,2,0,1)
            
            table.attach(HIGEntryLabel(_('Difficulty:')),0,1,1,2)
            table.attach(HIGEntryLabel(tcpseq['difficulty']),1,2,1,2)
            
            table.attach(HIGEntryLabel(_('Index:')),0,1,2,3)
            table.attach(HIGEntryLabel(tcpseq['index']),1,2,2,3)
            
            table.attach(HIGEntryLabel(_('Values:')),0,1,3,4)
            table.attach(combo,1,2,3,4)
            
            self.tcp_expander.add(hbox)
            self._pack_noexpand_nofill(self.tcp_expander)
    
    def set_ipseq(self, ipseq):
        if ipseq:
            self.ip_expander.set_use_markup(True)
            table, hbox = self.create_table_hbox()
            
            combo = gtk.combo_box_new_text()
            
            for i in ipseq['values'].split(','):
                combo.append_text(i)
            
            table.attach(HIGEntryLabel(_('Class:')),0,1,0,1)
            table.attach(HIGEntryLabel(ipseq['class']),1,2,0,1)
            
            table.attach(HIGEntryLabel(_('Values:')),0,1,1,2)
            table.attach(combo,1,2,1,2)
            
            self.ip_expander.add(hbox)
            self._pack_noexpand_nofill(self.ip_expander)
    
    def set_tcptsseq(self, tcptsseq):
        if tcptsseq:
            self.tcpts_expander.set_use_markup(True)
            table, hbox = self.create_table_hbox()

            combo = gtk.combo_box_new_text()

            for i in tcptsseq.get('values', '').split(','):
                combo.append_text(i)
            
            table.attach(HIGEntryLabel(_('Class:')),0,1,0,1)
            table.attach(HIGEntryLabel(tcptsseq['class']),1,2,0,1)
            
            table.attach(HIGEntryLabel(_('Values:')),0,1,1,2)
            table.attach(combo,1,2,1,2)
            
            self.tcpts_expander.add(hbox)
            self._pack_noexpand_nofill(self.tcpts_expander)
    
    def set_comment(self, comment=''):
        self.comment_expander.set_use_markup(True)
        if comment:
            self.comment_expander.set_expanded(True)
        
        hbox = HIGHBox()
        
        self.comment_scrolled = gtk.ScrolledWindow()
        self.comment_scrolled.set_border_width(5)
        self.comment_scrolled.set_policy(gtk.POLICY_AUTOMATIC,\
                                         gtk.POLICY_AUTOMATIC)
        
        self.comment_txt_vw = gtk.TextView()
        self.comment_txt_vw.set_wrap_mode(gtk.WRAP_WORD)
        self.comment_txt_vw.get_buffer().set_text(comment)
        
        self.comment_scrolled.add(self.comment_txt_vw)
        hbox._pack_expand_fill(self.comment_scrolled)
        
        self.comment_expander.add(hbox)
        self._pack_noexpand_nofill(self.comment_expander)
    
    def get_comment(self):
        buffer = self.comment_txt_vw.get_buffer()
        return buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter())
