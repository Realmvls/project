#!/usr/bin/Python
# -*- coding: utf-8 -*-
# 啊啊啊啊啊啊啊淘宝这种商品信息是保存在script标签中的，目的是方便动态内容的及时更新，右键检查网页元素的到的结果直接用BeautifulSoup没法匹配到，
#所以爬网页之前一定要养成右键检查网页源代码的习惯年轻人。。。
#Beautifulsoup不能解析<script>标签中的内容，会把其中内容当字符串处理

import re
import requests

url = 'https://s.taobao.com/search?q=python%E4%B9%A6&s='       #url传参数的时候第一个用问好，第二个以及以后的所有均用&可根据传递参数找到url的翻页规律！！！

# file = open('F:/spider_data/taobao_test.txt','w',encoding='utf-8')

for k in range(0,100):        #100次，就是100个页的商品数据
    print('第%d页'%(k+1))
    resp = requests.get(url+'%d'%(44*k)).text
    #print(url+'%d'%(44*k))
                                               #此页面商品的名称，价格，归属地写在html的script标签中，分别对应raw_title，view_price，item_loc
    # print(resp)                                  #script标签的作用是用于定义客户端脚本，比如 JavaScript。script 元素既可以包含脚本语句，也可以通过 src 属性指向外部脚本文件。必需的 type 属性规定脚本的 MIME 类型。JavaScript 的常见应用时图像操作、表单验证以及动态内容更新。
    title = re.findall('"raw_title":"([^"]+)"',resp)
    price = re.findall('"view_price":"([^"]+)"',resp)
    loc = re.findall('"item_loc":"([^"]+)"',resp)
    # print(len(loc))
    x = len(title)
    for f in range(x):
        print('第%d个'%f)
        print(title[f])
        print(price[f])
        print(loc[f])
        print('************************************************************************************')

    # title = soup.find_all('raw_title')    #title 为一个list
    # print(len(title))
    # print(len(title))
    # for tit in title:
    #     print(tit.find('span'))
#     price = soup.findall()
#     loc = re.findall(r'"item_loc":"([^"]+)"',resp.text,re.I)
#
#     x = len(title)           #每一页商品的数量
#
#     for i in range(0,x) :    #把列表的数据保存到文件中
#         file.write(str(k*44+i+1)+'书名：'+title[i]+'\n'+'价格：'+price[i]+'\n'+'地址：'+loc[i]+'\n\n')
#
#
# file.close()
