#!/usr/bin/Python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
#给页数获取那一页的html代码

def gethtml(number):
    url = "https://www.qiushibaike.com/8hr/page/"
    r  = requests.get(url+str(number),headers = Headers)
    html = r.text
    return html

#获取给定页数的作者和内容
# def gettitles(number):
#     html = gethtml(number)
#     soup = BeautifulSoup(html,"html.parser")
#     titles = soup.find_all('div',{'class':"author clearfix"})
#     return titles
# def getbodys(number):
#     html = gethtml(number)
#     soup = BeautifulSoup(html, "html.parser")
#     bodys = soup.find_all('div',{'class':'content'})
#     return bodys
def gettitles(number):
    html = gethtml(number)
    soup = BeautifulSoup(html,"html.parser")
    divs = soup.find_all('div', attrs={'class': {'author clearfix', 'content'}})
    return divs
#打印所有内容
# def getall(begin,end):
#     for f in range(int(begin),int(end)+1):
#         print('第{}页'.format(f))
#         titles = gettitles(f)
#         bodys = getbodys(f)
#         for title in titles:
#             tit = title.find('h2')
#             if title:
#                 print(tit.text)
#             for body in bodys:
#                 bod = body.find('span')
#                 if body:
#                     print(bod.text)
def getall(begin,end):
    for f in range(int(begin),int(end)+1):
        print('第{}页'.format(f))
        divs = gettitles(f)
        for div in divs:
            data = div.find('span')
            if data:
                print(data.text)
            tit = div.find('h2')
            if tit:
                print(tit.text)

if __name__ =='__main__':
    Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
    begin = input("请输入开始页数：").strip()
    end = input("请输入结束页数：").strip()
    getall(begin,end)


