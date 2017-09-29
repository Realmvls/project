#!/usr/bin/Python
# -*- coding: utf-8 -*-
#获取西刺代理ip
#http://www.xicidaili.com/wn/       https代理
#http://www.xicidaili.com/wt/       http代理





#并没有成功使用代理访问检测代理是否失效的网站。。明天改
import requests
from bs4 import BeautifulSoup

Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

url = 'http://www.xicidaili.com/wn/'
html = requests.get(url,headers=Headers).content
soup = BeautifulSoup(html,'html.parser')
data = soup.find_all('tr')
# print(len(data))
#采集第一页的所有代理ip
proxys = []
for x in range(1,len(data)):    #ip地址以及端口信息是从第二个tr标签开始的,所以从1开始而非从0开始
    ip = data[x]
    tds = ip.find_all('td')
    # print(tds)
    proxys.append(tds[1].text)
    proxys.append(tds[2].text)
    #也可以这样写 d = tds[1].text+'\t'+tds[2].text
#并不是所有的代理都能用，原因有很多，可能是我们所处的网络连不到这个代理，也有可能是这个代理，连不到我们的目标网址，所以，我们要验证一下。以http://ip.chinaz.com/getip.aspx作为目标网址为例（这个是测试ip地址的网址）代码如下：
#可以用socket.setdefaulttimeout(3)设置全局超时时间为3s，也就是说，如果一个请求3s内还没有响应，就结束访问，并返回timeout（超时）,也可以直接在resquests.get中设置timeout

#此处对代理ip格式进行处理
z = []
num = len(proxys)//2
h=0
for i in range(0,num):
    proxy_host = 'https://'+proxys[h]+':'+proxys[h+1]
    proxy_temp = {"https":proxy_host}                     #proxy_temp = {"http":proxy_host}其中http代表代理的类型，除了http之外还有https，socket等，这里就以http为例    #此处为代理ip的固定格式
    z.append(proxy_temp)
    h=h+2

finallyip = []
url = "http://ip.chinaz.com/getip.aspx"        #这个是测试ip地址的网址
p = 1
for proxy in z:
    print('正在处理第%d个'%(p),proxy)
    p = p+1
    try:
        response = requests.get(url,proxies=proxy,timeout = 1)           #此处可传递proxies参数，urlopen不可以传递proxies参数。以代理模式访问目标网址
        finallyip.append(proxy)
        print(response.text)     #此句打印的信息可以看设置代理ip有没有成功
    except Exception as e:           # Exception 为所有异常的基类。此句为捕捉多个异常并将异常对象输出
        print(proxy,e)
        continue
print('共有{}个代理ip可以使用'.format(len(finallyip)))             #共有多少个可用ip
#将筛选过的代理保存到磁盘
try:
    for u in finallyip:
        file = open('F:/spider_data/ip.txt', 'w')  # a的意思是接着写入，改成w则为替换写入
        for e in finallyip:
            file.write(str(e))  # 此处finallyip为列表，里面的所有的元素为字典对象，file.write的对象必须是字符串所以用str转换一下
            file.write('\n')
    file.close()
    print('文件写入成功')
except Exception as e:

    print('文件写入失败',e)

# 随机或按顺序获取finallyip并把它直接传入requests的get方法中便可切换代理访问网址
# web_data = requests.get(url, headers=headers, proxies=proxies)

# 代理IP里的“透明”“匿名”“高匿”分别是指？
# 透明代理的意思是客户端根本不需要知道有代理服务器的存在，但是它传送的仍然是真实的IP。使用透明IP，就无法绕过通过一定时间内IP访问次数的限制。
# 普通匿名代理能隐藏客户机的真实IP，但会改变我们的请求信息，服务器端有可能会认为我们使用了代理。不过使用此种代理时，虽然被访问的网站不能知道你的ip地址，但仍然可以知道你在使用代理，这样的IP就会被网站禁止访问。
# 高匿名代理不改变客户机的请求，这样在服务器看来就像有个真正的客户浏览器在访问它，这时客户的真实IP是隐藏的，网站就不会认为我们使用了代理。
# 综上所述，爬虫代理IP最好使用“高匿IP”