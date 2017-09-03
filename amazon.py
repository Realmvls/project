#!/usr/bin/Python
# -*- coding: utf-8 -*-
#使用代理ip
#amazon 手机名称 品牌,url,价格导入数据库,导出csv,xls格式各一份
#所有图片以手机名称命名+价格命名并下载到本地
#多线程 共216964条数据

#基本框架出来了，剩下的解决分布式和存入mysql中的数据匹配的问题

import requests
from bs4 import BeautifulSoup
import re
import pymysql
import random
urllist = []
Proxies = []
Headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
def gethtml(url):
    proxy = random.choice(Proxies)
    try:
        html = requests.get(url,headers = Headers,proxies=proxy).content
        soup = BeautifulSoup(html, 'html.parser')
        return soup                   #这句很关键啊啊啊啊
    except Exception as e:
        print(e)
        print("获取html失败")
def getname(soup):
    try:
        names = soup.find_all('h2')
        name = re.findall('data-attribute="(.*?)"',str(names))         #正则表达式的类型必须是字符串
        print('获取商品名{}个'.format(len(name)))
        for na in name:
            # print(na)
            allname.append(na)
        return allname
    except Exception as e:
        print(e)
        print('获取names列表失败')
def gettitle(soup):
    try:
        titles = soup.select('.a-size-small.a-color-secondary')                                #所要获取的title夹在两个空span标签中间
        selecttitles = [i for idx,i in enumerate(titles[1:-1])if titles[idx] == titles[idx+2] ]        #此处取得的title中混入了两个不相关的数据
        print('获取标签{}个'.format(len(selecttitles)))
        for title in selecttitles:
            alltitle.append(title.text)
        return alltitle
    except Exception as e:
        print(e)
        print('获取title列表失败')
def getprice(soup):
    try:
        prices = soup.select('.a-size-base.a-color-price.s-price.a-text-bold')
        print('获取价格{}个'.format(len(prices)))
        for price in prices:
            allprice.append(price.text)
            # print(price.text)
        return allprice
    except Exception as e:
        print(e)
        print('获取价格列表失败')
def geturl(soup):
    try:
        urls = soup.select('.a-link-normal.s-access-detail-page.s-color-twister-title-link')
        href = re.findall('href="(.*?)"',str(urls))
        print('获取url个数{}个'.format(len(href)))
        for url in href:                       #allurl里面前两条数据和最后一条数据有问题
            allurl.append(url)
            # print(url)
        return allurl
    except Exception as e:
        print(e)
        print('获取商品url列表失败')
def getpicture(soup):
    try:
        pictures = soup.select('.s-access-image.cfMarker')
        imgs = re.findall('src="(.*?)"',str(pictures))
        print('获取图片个数{}个'.format(len(imgs)))
        for i, j in enumerate(imgs):
            with open('F:/spider_data/amazon图片/第{}页，第{}张.jpg'.format(page,i), 'wb') as file:         #用format填充两个参数时的用法
            #with open('F:/spider_data/amazon图片/{},{}.jpg'.format(allname[i],allprice[i]),'wb') as file:       #这里写成这样每页保存几个图片后就会报错，怀疑是图片命名格式有问题，待修改。。。
                file.write(requests.get(j).content)
                print('正在保存第{}张图片'.format(i))
        return
    except Exception as e:
        print('下载图片失败')
        print(e)
def url_list(base_url):
    for i in range(1,401):
        url = base_url.format(i,i)
        urllist.append(url)
    return urllist
#设置代理ip
try:
    file = open('F:/spider_data/ip.txt','r')
    while True:
        line = file.readline()
        if line:
            Proxies.append(line)
        else:
            break
    file.close()
except Exception as e:
    print(e)
    print("ip代理池写入失败")

conn = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',password = '',db = 'amazon',charset = 'utf8mb4',cursorclass = pymysql.cursors.DictCursor)
cur = conn.cursor()
base_url = 'https://www.amazon.cn/s/ref=sr_pg_{}?fst=as:on&rh=k:手机,n:664978051&page={}&keywords=手机&ie=UTF8&qid=1504354063'
url_list(base_url)
page = 1   #用来记录抓取的页数
for url in urllist:
    allname = []
    alltitle = []
    allprice = []
    allurl = []
    img = []
    print('第{}页'.format(page))
    soup = gethtml(url)
    getname(soup)
    gettitle(soup)
    getprice(soup)
    geturl(soup)
    for num in range(len(allname)):
        try:
            # cur.execute('insert into phone (name,title,price,url) values ({},{},{},{})'.format(allname[num],alltitle[num],allprice[num],allurl[num]))   #这样写有点小问题，待修改。。。
            sql = ('insert into phone(name,title,price,url) values(%s,%s,%s,%s)')
            cur.execute(sql,(allname[num],alltitle[num],allprice[num],allurl[num]))
            conn.commit()
            print('正在写入第{}条数据'.format(num))
        except Exception as e:
            print(e)
            print("录入mysql出错")
    getpicture(soup)
    page = page+1
cur.close()
conn.close()

