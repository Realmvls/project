#!/usr/bin/Python
# -*- coding: utf-8 -*-
import requests
import re
import pymysql
conn = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',password = '',db = 'taobao_router',charset = 'utf8mb4',cursorclass = pymysql.cursors.DictCursor)
cur = conn.cursor()
baseurl = 'https://s.taobao.com/search?q=%E8%B7%AF%E7%94%B1%E5%99%A8&s='    # s=1,48,96 第一页  第二页 第三页
Headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}


for k in range(0,79):
    print('第%d页'%(k+1))
    url = baseurl+'%d'%(48*k)
    # print(url)
    response = requests.get(url,headers = Headers).text
    # print(type(response))

    title = re.findall('"title":(.*?),"pic_url"',response)
    price = re.findall('"price":(.*?),"trace"',response)
    sales = re.findall('"month_sales":(.*?),"seller"',response)
    del title[0]
    del sales[0]
    del price[0]
    x = 0
    while x < len(title):
        cur.execute("insert into router(title,price,sales) values ('%s','%s','%s')" % (title[x], price[x], sales[x]))
        print('正在导入第%s条数据' % x)
        x = x + 1
cur.close()
conn.close()

