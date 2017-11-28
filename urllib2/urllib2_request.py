#!/usr/bin/env python
# coding=utf-8

import urllib2

url = "http://www.baidu.com"

heads = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400"}

request = urllib2.Request(url)

response = urllib2.urlopen(request)

html = response.read()

#返回200表明爬取成功
print response.getcode()

#返回实际数据的实际url
print response.geturl()

#返回响应的HTTP报头
#print response.info()
