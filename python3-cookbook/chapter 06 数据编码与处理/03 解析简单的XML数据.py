# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     03
   Description :
   Author :       jusk?
   date：          2019/12/4
-------------------------------------------------
   Change Activity:
                   2019/12/4:
-------------------------------------------------
"""

# 解析简单的XML数据
from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)
print(doc)
# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()

# Steve Holden: Python for Data Analysis
# Mon, 19 Nov 2012 02:13:51 +0000
# http://holdenweb.blogspot.com/2012/11/python-for-data-analysis.html
#
# Vasudev Ram: The Python Data model (for v2 and v3)
# Sun, 18 Nov 2012 22:06:47 +0000
# http://jugad2.blogspot.com/2012/11/the-python-data-model.html
#
# Python Diary: Been playing around with Object Databases
# Sun, 18 Nov 2012 20:40:29 +0000
# http://www.pythondiary.com/blog/Nov.18,2012/been-...-object-databases.html
#
# Vasudev Ram: Wakari, Scientific Python in the cloud
# Sun, 18 Nov 2012 20:19:41 +0000
# http://jugad2.blogspot.com/2012/11/wakari-scientific-python-in-cloud.html
#
# Jesse Jiryu Davis: Toro: synchronization primitives for Tornado coroutines
# Sun, 18 Nov 2012 20:17:49 +0000
# http://feedproxy.google.com/~r/EmptysquarePython/~3/_DOZT2Kd0hQ/