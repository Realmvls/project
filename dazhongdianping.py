#!/usr/bin/Python
# -*- coding: utf-8 -*-

#获取大众点评上的南京地区所有日本料理店的名字，地址和人均消费
import requests
from bs4 import BeautifulSoup
import pymysql

base_url = 'http://www.dianping.com/search/category/5/10/g113p'
Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

for f in range(1,2):        #一共43页
    url = base_url+'%d'%(f)
    html = requests.get(url,headers = Headers).content
    # print(type(html))
    soup = BeautifulSoup(html,'html.parser')

    allname = soup.find_all(attrs={'data-hippo-type':'shop'})
    alladdr = soup.find_all('div',class_='tag-addr')
    allprice = soup.find_all('a',class_='mean-price')             #soup.find_all返回的是一个set


conn = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',password = '',db = 'y1',charset = 'utf8mb4',cursorclass = pymysql.cursors.DictCursor)
cur = conn.cursor()


z = 1
for b in allname:
    title = b.find('h4').text                       #title的类型此时为字符串        字符串和列表都可以直接存入数据库
    print('正在存入''第%d个'%(z),'名称')
    cur.execute("insert into y1 (name) values ('%s')"%(title))
    z = z+1
   # print(title)


z = 1
for n in alladdr:
    addr = n.find('span',{'class':'addr'}).text
    print('正在存入''第%d个' % (z), '地址')
    cur.execute("insert into y1 (place) values ('%s')" % (addr))
    z = z+1


z = 1
for m in allprice:
    price = m.find('b').text
    print('正在存入''第%d个' % (z), '价格')
    cur.execute("insert into y1 (price) values ('%s')"%(price))
    z = z+1
#
cur.close()
conn.close()




