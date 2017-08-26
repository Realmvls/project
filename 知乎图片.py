#!/usr/bin/Python
# -*- coding: utf-8 -*-
# #requests.get()返回Response，urlopen（）返回HTTPResponse
# #requests.get().content方法返回数据类型为bytes，  .text方法返回str类型
# #urlopen()返回值无.content 和.text 方法但是有.read方法，其返回的数据类型为bytes
# 在字符串中，包含换行符\n，在这种情况下，如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始。而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，在整体中进行匹配
#异常处理时try中的变量为局部变量，不能在except中使用，要经过其他处理

#动态网页抓取都是典型的办法 直接查看动态网页的加载规则。如果是ajax，则将ajax请求找出来给python。 如果是js去处后生成的URL。就要阅读JS，搞清楚规则。再让python生成URL

from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time
import requests


driver = webdriver.Chrome()
driver.get('https://www.zhihu.com/question/60962825')
time.sleep(2)
try:
    for t in range(1,135):             #大概循环130次可以到屏幕最下面，每次停留1秒左右，再快了图片加载不出来。。。#一次下移2000个像素刚好，再多了图片加载不全。。。
        print(t)
        t = 2000*t
        js = "var q=document.body.scrollTop=%d"%(t)
        driver.execute_script(js)
        time.sleep(1)
    driver.find_element_by_css_selector("button.QuestionMainAction").click()
    for t in range(1,160):
        print(t)
        t = 2000*t
        js = "var q=document.body.scrollTop=%d"%(t)
        driver.execute_script(js)
        time.sleep(1)
    driver.find_element_by_css_selector("button.QuestionMainAction").click()
    for t in range(1,250):
        print(t)
        t = 2000*t
        js = "var q=document.body.scrollTop=%d"%(t)
        driver.execute_script(js)
        time.sleep(1)
    driver.find_element_by_css_selector("button.QuestionMainAction").click()
    for t in range(1,300):
        print(t)
        t = 2000 * t
        js = "var q=document.body.scrollTop=%d" % (t)
        driver.execute_script(js)
        time.sleep(1)
    driver.find_element_by_css_selector("button.QuestionMainAction").click()
    for t in range(1,300):  # 大概循环130次可以到屏幕最下面，每次停留1秒左右，再快了图片加载不出来。。。#一次下移2000个像素刚好，再多了图片加载不全。。。
        print(t)
        t = 2000 * t
        js = "var q=document.body.scrollTop=%d" % (t)
        driver.execute_script(js)
        time.sleep(1)
except Exception as e:
    print(e)
try:
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    pictures = soup.findAll('img',{'class':'origin_image zh-lightbox-thumb lazy'})        #pictures为resultset类型
    # print(type(pictures))
    res = r'src="(.*?)"'
    allpicture = re.findall(res,str(pictures))                        #正则表达式传入的对象要为字符串类型
    print(len(allpicture))
    list1 = []
    n=1
    for picture in allpicture:
        if picture not in list1:
            print("正在把第%d张图存入列表"%(n))
            n = n+1
            list1.append(picture)
    print(len(list1))
except Exception as e:
    print(e)
try:
    for pic in list1:
        print(pic)
    #保存图片：
    for i,j in enumerate(list1):
        with open('F:/spider_data/知乎图片/{0}.jpg'.format(i),'wb') as file:
            print('正在保存第{}张图片'.format(i))
            file.write(requests.get(j).content)
except Exception as e:
    print(e)




