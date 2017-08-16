#!/usr/bin/Python
# -*- coding: utf-8 -*-
#获取大众点评上的南京地区所有日本料理店的名字，地址和人均消费     #大众点评反爬虫比较严格，大概录入不到三百的数据就会出现录入错误。。有待改进爬虫
import requests
from bs4 import BeautifulSoup
import pymysql
import time
import random

conn = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',password = '',db = 'y1',charset = 'utf8mb4',cursorclass = pymysql.cursors.DictCursor)
cur = conn.cursor()

base_url = 'http://www.dianping.com/search/category/5/10/g113p'
Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

for f in range(18,44):        #一共43页 range(1,44)

    url = base_url+'%d'%(f)
    html = requests.get(url,headers = Headers).content
    # print(type(html))
    soup = BeautifulSoup(html,'html.parser')
    print('正在处理第%s页'%f)
    allname = soup.find_all(attrs={'data-hippo-type':'shop'})
    alladdr = soup.find_all('div',class_='tag-addr')
    allprice = soup.find_all('a',class_='mean-price')             #soup.find_all返回的是一个set
    a = []
    b = []
    c = []

    for t in allname:
        try:
            title = t.find('h4').text                       #title的类型此时为字符串        字符串和列表都可以直接存入数据库
            a.append(title)
        except:
            a.append('xxx')
            print('一条数据录入allname出错')

    for y in alladdr:
        try:
            addr = y.find('span',{'class':'addr'}).text
            b.append(addr)
        except:
            b.append('xxx')
            print('一条数据录入alladdr出错')

    for u in allprice:
        try:
            price = u.find('b').text
            c.append(price)
        except:
            c.append('xxx')
            print("一条数据录入allprice出错")
    x = 0
    while x<len(a) :
        cur.execute("insert into y1(name,place,price) values ('%s','%s','%s')"%(a[x],b[x],c[x]))
        print('正在导入第%s条数据'%x)
        x = x+1

cur.close()
conn.close()

