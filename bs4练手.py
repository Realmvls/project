#!/usr/bin/Python                 
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
#一

# html = '''<div class="p-name p-name-type-2">
#         <a target="_blank" title="Apple iPhone 6 (A1589) 16GB 金色 移动4G手机" href="//item.jd.com/1217493.html" onclick="searchlog(1,1217493,0,1,'','flagsClk=4194952')">
#             <em>Apple <font class="skcolor_ljg">iPhone</font> <font class="skcolor_ljg">6</font> (A1589) 16GB 金色 移动4G手机</em>
#             <i class="promo-words" id="J_AD_1217493"></i>
#         </a>
#     </div>'''
# soup = BeautifulSoup(html,"html.parser")
# data = soup.find_all('div',{'class':'p-name p-name-type-2'})[0].find_all('a')[0]
# print(data['href'])
# print(data['title'])

#二
html = '''                               <tr class="bg">
<td class="td-title faceblue">
<span class="face" title="普通帖">

</span>
<a href="/post-basketball-200125-1.shtml" target="_blank">
当教练的最高境界——让对手任谁都能打出神仙球！
</a>
</td>
<td><a href="http://www.tianya.cn/75944044" target="_blank" class="author">司马取印</a></td>
<td>4420</td>
<td>163</td>
<td title="2017-04-25 23:44">04-25 23:44</td>
</tr>

<tr>
<td class="td-title faceblue">
<span class="face" title="普通帖">

</span>
<a href="/post-basketball-200496-1.shtml" target="_blank">
10年的黑色乔丹6代！！！(转载)<span class="art-ico art-ico-3" title="内有2张图片"></span>
</a>
</td>
<td><a href="http://www.tianya.cn/126744501" target="_blank" class="author">13141373133</a></td>
<td>102</td>
<td>9</td>
<td title="2017-04-25 17:44">04-25 17:44</td>
</tr>
'''
# #方法一
# soup = BeautifulSoup(html,'html.parser')
# data = soup.find_all('a')
# for item in data:
#     print(item['href'])

# #方法2
# soup=BeautifulSoup(html,'lxml')
# zzr=soup.find_all(attrs={'class':'td-title faceblue'})
# print(type(zzr))      #确定经过soup查找匹配后的数据是一个set
# for item in zzr:
#     list_tmp=item.find_all('a')
#     for a in list_tmp:
#         print(a.get('href'))


#三
# #抓起这个网址的提供的ip地址和端口   http://www.xicidaili.com/nn/1
#
# import requests
# from bs4 import BeautifulSoup
# import re
#
# user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
# headers = {'User-Agent': user_agent}
#
# session = requests.session()
# page = session.get("http://www.xicidaili.com/nn/1", headers=headers)
# soup = BeautifulSoup(page.text, 'lxml')  # 这里没有装lxml的话,把它去掉用默认的就好
#
# # 匹配带有class属性的tr标签
# taglist = soup.find_all('tr', attrs={'class': re.compile("(odd)|()")})
# for trtag in taglist:
#     tdlist = trtag.find_all('td')  # 在每个tr标签下,查找所有的td标签
#     print(tdlist[1].string) # 这里提取IP值
#     print(tdlist[2].string)  # 这里提取端口值


#四
# #爬糗百的段子前2页   #糗百的首页热门段子过一小会刷新一次就会有改变，需要更换headers
# import requests
# from bs4 import BeautifulSoup
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
# base_url = "https://www.qiushibaike.com/8hr/page/"
# for num in range(1,3):
#     print('第{}页'.format(num))
#     r = requests.get(base_url+str(num), headers = headers)
#     content = r.text
#     soup = BeautifulSoup(r.text, 'html.parser')
#     divs = soup.select('div[class="author clearfix"]')
#     tits = soup.select('div[class="content"]')
#     for div in divs:
#         data = div.select('h2')[0].text
#         for tit in tits:
#             joke = tit.select('span')[0].text
#             print(data)
#             print(joke)
#             print('------')
# #方法二：
# import requests
# from bs4 import BeautifulSoup
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
# base_url = "https://www.qiushibaike.com/8hr/page/"
# for num in range(1,3):
#     print('第{}页'.format(num))
#     r = requests.get(base_url+str(num), headers = headers)
#     content = r.text
#     soup = BeautifulSoup(r.text, 'html.parser')
#     divs = soup.find_all('div',attrs={'class':{'author clearfix','content'}})
#     for div in divs:
#         data = div.find('span')
#         if data:
#             print(data.text)
#         tit = div.find('h2')
#         if tit:
#             print(tit.text)
#

#五
# #收集新浪新闻的正文
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# url = "http://news.sina.com.cn/o/2017-08-05/doc-ifyitayr9313287.shtml"
# html = urlopen(url)
# soup = BeautifulSoup(html,"html.parser")
# data = soup.select('#artibody')[0].text
# print(data)
