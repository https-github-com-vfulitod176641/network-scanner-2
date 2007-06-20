# Copyright (C) 2005 Insecure.Com LLC.
#
# Authors: Adriano Monteiro Marques <py.adriano@gmail.com>
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

import urllib
import urllib2

insecure_site = "http://www.insecure.org/"
nmap_submission_page = insecure_site + "cgi-bin/servicefp-submit.cgi"

class ServiceFingerprintRegister(object):
    def __init__(self):
        try:
            urllib.urlopen(insecure_site)
        except:
            return None

        self.service = ""
        self.platform = ""
        self.description = ""
        self.ip = ""
        self.fingerprint = ""
        self.email = ""
        self.notes = ""

    def report(self):
        data = urllib.urlencode({"email":self.email,
                                 "service":self.service,
                                 "platform":self.platform,
                                 "description":self.description,
                                 "ip":self.ip,
                                 "fingerprint":self.fingerprint,
                                 "notes":self.notes})

        # The submit page source code points that the info should be set using POST method
        # But, it only worked sending it through GET method. So, I decided to send using
        # both methods, to insure that it's going to work.
        request = urllib2.Request(nmap_submission_page + "?" + data, data)
        response = urllib2.urlopen(request)

        from tempfile import mktemp
        import webbrowser

        tfile = mktemp()
        open(tfile, "w").write(response.read())
        webbrowser.open(tfile)


if __name__ == "__main__":
    f = ServiceFingerprintRegister()
    f.report()