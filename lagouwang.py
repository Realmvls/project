#!/usr/bin/Python
# -*- coding: utf-8 -*-
#拉勾网Python相关职位抓取
#保存职位信息，工资和要求以及工作单位成csv文件

import requests
import random
Proxies=[]
post_data = {'first':'True','kd':'python','pn':'1'}
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
# result = requests.post(url,data = post_data).text
# print(result)
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
    print("ip代理写入失败")
proxy_ip = random.choice(Proxies)
print(proxy_ip)
result = requests.get(url,headers = Headers,proxies = proxy_ip).text
print(result)