#!/usr/bin/env python
# coding=utf-8

import urllib2
import urllib2
import ssl


url = "http//www.baidu.com"

headers ={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

request =  urllib2.Request(url,headers = headers)

html = urllib2.urlopen(request).read()

print html

