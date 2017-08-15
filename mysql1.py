# !/usr/bin/Python
# -*- coding: utf-8 -*-
# # python3.4中不能使用python2.7中的MySQLdb连接数据库，取而代之的是pymysql
# import pymysql
# connection = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',password = '',db = 'y2',charset = 'utf8mb4',cursorclass = pymysql.cursors.DictCursor)
# cur = connection.cursor()  #获取一个游标
# cur.execute('select *from example ')
# data = cur.fetchall()     #将所有查询结果返回元组
# print(data)
# cur.close()               #关闭游标
# connection.close()         #释放数据库资源



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

a = []
b = []
c = []

for t in allname:
    title = t.find('h4').text                       #title的类型此时为字符串        字符串和列表都可以直接存入数据库
    a.append(title)

for y in alladdr:
    addr = y.find('span',{'class':'addr'}).text
    b.append(addr)

for u in allprice:
    price = u.find('b').text
    c.append(price)
cur.execute("insert into y1(name,place,price) values ('%s','%s','%s')"%(a,b,c))

cur.close()
conn.close()

