"""
    This file is part of EmailHarvester
    Copyright (C) 2016 @maldevel
    https://github.com/maldevel/EmailHarvester
    
    EmailHarvester - A tool to retrieve Domain email addresses from Search Engines.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    For more see the file 'LICENSE' for copying permission.
"""

#config = None
app_emailharvester = None


def search(domain, limit):
    all_emails = []
    app_emailharvester.show_message("\n[+] Searching in Instagram..\n")

    app_emailharvester.show_message("\n[+] Searching in Yahoo + Instagram..\n")
    yahooUrl = "http://search.yahoo.com/search?p=site%3Ainstagram.com+%40{word}&n=100&ei=UTF-8&va_vt=any&vo_vt=any&ve_vt=any&vp_vt=any&vd=all&vst=0&vf=all&vm=p&fl=0&fr=yfp-t-152&xargs=0&pstart=1&b={counter}"
    app_emailharvester.init_search(yahooUrl, domain, limit, 1, 100)
    app_emailharvester.process()
    all_emails += app_emailharvester.get_emails()
    
    app_emailharvester.show_message("\n[+] Searching in Bing + Instagram..\n")
    bingUrl = "http://www.bing.com/search?q=site%3Ainstagram.com+%40{word}&count=50&first={counter}"
    app_emailharvester.init_search(bingUrl, domain, limit, 0, 50)
    app_emailharvester.process()
    all_emails += app_emailharvester.get_emails()
    
    app_emailharvester.show_message("\n[+] Searching in Google + Instagram..\n")
    googleUrl = 'https://www.google.com/search?num=100&start={counter}&hl=en&q=site%3Ainstagram.com+"%40{word}"'
    app_emailharvester.init_search(googleUrl, domain, limit, 0, 100)
    app_emailharvester.process()
    all_emails += app_emailharvester.get_emails()

    app_emailharvester.show_message("\n[+] Searching in Baidu + Instagram..\n")
    url = 'http://www.baidu.com/search/s?wd=site%3Ainstagram.com+"%40{word}"&pn={counter}'
    app_emailharvester.init_search(url, domain, limit, 0, 10)
    app_emailharvester.process()
    all_emails += app_emailharvester.get_emails()

    app_emailharvester.show_message("\n[+] Searching in Exalead + Instagram..\n")
    url = "http://www.exalead.com/search/web/results/?q=site%3Ainstagram.com+%40{word}&elements_per_page=10&start_index={counter}" 
    app_emailharvester.init_search(url, domain, limit, 0, 50)
    app_emailharvester.process()
    all_emails += app_emailharvester.get_emails()

    #dogpile seems to not support site:
    
    return all_emails


class Plugin:
    def __init__(self, app, conf):#
        global app_emailharvester, config
        #config = conf
        app.register_plugin('instagram', {'search': search})
        app_emailharvester = app
        