# !/usr/bin/Python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import os

os.mkdir('G://hozin照片')
os.chdir('G://hozin照片')  # 如果没有这两句就会下载文件到当前代码所在的文件夹中
x = 1
for num in range(1,4):
    print("第%s页"%num)
    base_url = "https://tieba.baidu.com/p/3290636056?pn="
    url = base_url+str(num)
    # print(url)
    html = urlopen(url)
    soup = BeautifulSoup(html,"html.parser")

    piclist = soup.select('.BDE_Image')

    for pic in piclist:
        hand = pic.attrs['src']
        print('正在下载第%s张' % x)
        print(hand)
        filename = '第%s张.jpg'%x
        # filename = hand.split('/')[-1]    #split()函数用来分割字符串，这句仅仅用来给下载的图片起名
        urllib.request.urlretrieve(hand,filename,None)
        x=x+1





    #urllib.urlretrieve(imgurl,'F:\\taiyan\\'+'%s.jpg'%x)  #自定义下载的图片的存贮路径 ，首先应该在F盘下创建taiyan这个文件夹
    #urllib.urlretrieve(imgurl,'%s.jpg'% x)#urlretrieve用来保存下载的数据,保存到代码所在的文件夹下

