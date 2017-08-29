#!/usr/bin/Python
# -*- coding: utf-8 -*-
#使用代理ip
#amazon 手机名称 品牌,url,价格导入数据库,导出csv,xls格式各一份
#所有图片以手机名称命名+价格命名并下载到本地
#多线程 共216964条数据
import requests
from bs4 import BeautifulSoup
import re
Headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
url = 'https://www.amazon.cn/s/ref=nb_sb_noss_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Daps&field-keywords=%E6%89%8B%E6%9C%BA&rh=i%3Aaps%2Ck%3A%E6%89%8B%E6%9C%BA'
allname = []
alltitle = []
allprice = []
allurl = []
def gethtml(url):
    try:
        html = requests.get(url,headers = Headers).content
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except Exception as e:
        print(e)
        print("获取html失败")
def getname(soup):
    try:
        names = soup.find_all('h2')
        name = re.findall('data-attribute="(.*?)"',str(names))         #正则表达式的类型必须是字符串
        print(len(name))
        for na in name:
            alltitle.append(na)
    except Exception as e:
        print(e)
        print('获取names失败')
def gettitle(soup):
    try:
        titles = soup.select('.a-size-small.a-color-secondary')
        print(len(titles))
        # for title in titles:
        #     alltitle.append(title)                                   #  ##tits列表的最后两个并不为需要获取的目标，等结束后再处理
        #     print(title.text)
    except Exception as e:
        print(e)
        print('获取title失败')
def getprice(soup):
    try:
        prices = soup.select('.a-size-base.a-color-price.s-price.a-text-bold')
        print(len(prices))
        for price in prices:
            allprice.append(price)
            # print(price.text)
    except Exception as e:
        print(e)
        print('获取价格失败')
def geturl(soup):
    try:
        urls = soup.select('.a-link-normal.s-access-detail-page.s-color-twister-title-link')
        href = re.findall('href="(.*?)"',str(urls))
        print(len(href))
        for url in href:                       #allurl里面前两条数据和最后一条数据有问题
            allurl.append(url)
    except Exception as e:
        print(e)
        print('获取商品url失败')


soup = gethtml(url)
geturl(soup)
gettitle(soup)
getname(soup)
getprice(soup)

