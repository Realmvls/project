# !/usr/bin/Python
# -*- coding: utf-8 -*-
import os
import urllib
import urllib.request
from urllib.request import urlopen
import threading
from urllib.error import URLError
from bs4 import BeautifulSoup

class hozinSpider:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko'
        self.header = {'User-Agent':self.user_agent}
        #初始网址
        self.url = 'https://tieba.baidu.com/p/3290636056?pn=%s'
        #迭代页面数
        self.num = 3
        self.save_dir = 'F:/spider_data/hozin'
        return
    def start_spider(self):
        try:
            for n in range(1,self.num):
                #创建线程
                thread = threading.Thread(target=self.get_html,args=str(n))
                thread.start()
        except Exception as e:
            print('创建线程失败',e)
        return
    def get_html(self,page):
        try:
            web_url = self.url % page
            html = urlopen(web_url)
            # request = urllib.request.Request(web_url,headers = self.header)
            # with urllib.request.urlopen(request) as f:
            #     html_content = f.read().decode('utf-8')
            self.get_picture(html)
        except URLError as e:
            print(e.reason)
        return
    def get_picture(self,html):
        #匹配出网页中的图片链接
        soup = BeautifulSoup(html,"html.parser")
        piclist = soup.select('.BDE_Image')
        for n in piclist:
            self.save_picture(str(n))
        return
    def save_picture(self,img):
        #save_dir为F：/spider_data/hozin
        save_path = self.save_dir + '/' + img.replace(':','@').replace('/','_')
        #看目录是否存在，不存在则创建一个
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        print(save_path + ' ------%s'% threading.current_thread())
        #下载图片
        urllib.request.urlretrieve(img, save_path)
        return

spider = hozinSpider()
spider.start_spider()








# from urllib.request import urlopen
# import urllib.request
# from bs4 import BeautifulSoup
# import os
# os.mkdir('G://hozin照片')
# os.chdir('G://hozin照片')  # 如果没有这两句就会下载文件到当前代码所在的文件夹中
# x = 1
# for num in range(1,4):
#     print("第%s页"%num)
#     base_url = "https://tieba.baidu.com/p/3290636056?pn="
#     url = base_url+str(num)
#     # print(url)
#     html = urlopen(url)
#     soup = BeautifulSoup(html,"html.parser")
#
#     piclist = soup.select('.BDE_Image')
#
#     for pic in piclist:
#         hand = pic.attrs['src']
#         print('正在下载第%s张' % x)
#         print(hand)
#         filename = '第%s张.jpg'%x
#         # filename = hand.split('/')[-1]    #split()函数用来分割字符串，这句仅仅用来给下载的图片起名
#         urllib.request.urlretrieve(hand,filename,None)
#         x=x+1
#
#
#
#
#
#     #urllib.urlretrieve(imgurl,'F:\\taiyan\\'+'%s.jpg'%x)  #自定义下载的图片的存贮路径 ，首先应该在F盘下创建taiyan这个文件夹
#     #urllib.urlretrieve(imgurl,'%s.jpg'% x)#urlretrieve用来保存下载的数据,保存到代码所在的文件夹下
#
