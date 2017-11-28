#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="

fordata = {
        "start":"0",
        "limit":"20"
        }

data = urllib.urlencode(fordata)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400"}

request = urllib2.Request(url,data = data,headers = headers)

html = urllib2.urlopen(request).read()

print html
