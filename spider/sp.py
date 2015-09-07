#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getContent(html):
    #reg = r'<title>(.+?)</title>'
    #imgre = re.compile(reg)
    reg = r'<item>(.+?)</item>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
        #urllib.urlretrieve(imgurl,'%s.jpg' % x)
        print imgurl 


html = getHtml("http://rss.cnbeta.com/rss")

print getContent(html)
