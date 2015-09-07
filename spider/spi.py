#coding=utf-8
import urllib
import re
import MySQLdb as  DB  
import time
#import md5 
import hashlib

my = DB.connect("127.0.0.1","root","root","data" ,charset="utf8")
db = my.cursor()
sql = "SET NAMES UTF8;"
db.execute(sql)
my.commit()



def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getContent(html):
    item_list = []
    #reg = r'<title>(.+?)</title>'
    #imgre = re.compile(reg)
    reg = r'<item>(.+?)<\/item>'
    #imgre = re.compile(reg)
    itemlist = re.findall(reg, html,re.S)
    for item in itemlist:
        url_reg = r'<link>(.+?)<\/link>'
        url_list = re.findall(url_reg, item)
        title_reg = r'<title>(.+?)<\/title>'
        title_list = re.findall(title_reg, item)
        item_list.append({'url':url_list[0], 'title':title_list[0]})
        
    return item_list    

def intoDB(item_list) :
    #hashf = md5.md5()
    hashf = hashlib.md5()
    for item in item_list:
        #print "%s\t%s  "%(item['url'], item['title'])
        t = int(time.time()) 
        hashf.update(item['url']) 
        str_md5 = hashf.hexdigest() 
        sql = "insert ignore into py_news(url,title,datetime,md5,`like`) value('%s', '%s', '%d', '%s', '0')"%(item['url'], item['title'],t, str_md5)
        db.execute(sql)
        my.commit()

html = getHtml("http://rss.cnbeta.com/rss")

item_list = getContent(html)
intoDB(item_list)

