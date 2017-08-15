# !/usr/bin/Python
# -*- coding: utf-8 -*-
# python3.4中不能使用python2.7中的MySQLdb连接数据库，取而代之的是pymysql
import pymysql
connection = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',password = '',db = 'y2',charset = 'utf8mb4',cursorclass = pymysql.cursors.DictCursor)
cur = connection.cursor()  #获取一个游标
cur.execute('select *from example ')
data = cur.fetchall()     #将所有查询结果返回元组
print(data)
cur.close()               #关闭游标
connection.close()         #释放数据库资源


