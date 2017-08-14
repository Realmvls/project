#!/usr/bin/Python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

num = [0,25,50,75,100,125,150,175,200,225]
Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

for f in num:
    base_url = 'https://movie.douban.com/top250?start='
    url = base_url+'%d&filter'%(f)
    html = requests.get(url,headers = Headers).content       #url在这里是一个response对象，无法用BeautifulSoup解析，如果要解析，解析对象应该是web.content
    soup = BeautifulSoup(html,'html.parser')                #.content和.text的区别是.text返回的是Unicode数据，而.content返回的是bytes型也就是二进制数据.. #也就是说，如果你想取文本，可以通过r.text。如果想取图片，文件，则可以通过r.content。（resp.json()返回的是json格式数据）
    datas = soup.find_all('div',{'class':'hd'})
    for data in datas:
        name = data.find_all('span')[0].string
        print(name)




