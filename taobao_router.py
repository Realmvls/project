#!/usr/bin/Python
# -*- coding: utf-8 -*-
import requests
import re

baseurl = 'https://s.taobao.com/search?q=%E8%B7%AF%E7%94%B1%E5%99%A8&s='    # s=1,48,96 第一页  第二页 第三页
Headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
for k in range(0,79):
    print('第%d页'%(k+1))
    url = baseurl+'%d'%(48*k)
    # print(url)
    response = requests.get(url,headers = Headers).content
    # print(response)

    title = re('title(.*?)pic_url',response)
    print(len(title))
