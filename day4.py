#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='Leon Hu'

import requests
import ssl
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context  # 忽略 ssl 证书的验证

url_home = 'https://www.liaoxuefeng.com'  # 主页
url_first = '/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'  # Python3教程首页
filepath = 'f:/wiki/'  # 存储路径
filepath_='0014316089557264a6b348958f449949df42a6d3a2e542c000/'  # 教程第一个页面的名称，其它页面都在这个页面下面

# 封装headers和cookies模拟浏览器请求，不然可能会报503
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}

cookies = {'Hm_lpvt_2efddd14a5f2b304677462d06fb4f964':'1514276914', 'Hm_lvt_2efddd14a5f2b304677462d06fb4f964':'1513759510,1513840593,1514170543,1514272126' }

# 请求网页
def request(url):
    return requests.get(url,headers=headers, cookies=cookies)

# 请求网页，拿到所有目录的URL
res = request(url_home + url_first)
soup = BeautifulSoup(res.text,'html.parser')
hrefs = soup.find_all('a', class_='x-wiki-index-item')

# 循环写入内容
for h in hrefs:
    href = h['href'] # 拿到左侧目录的URL值
    filenames = href.split('/')

    # 这里作一个简单的判断，拿到第一级页面的名称，其它页面都在第一级页面之下
    if len(filenames) == 3:
        filename = filenames[2]+'.html'
    else:
        filename = filepath_+filenames[3]


    # 写入文件
    con = request(url_home + href)
    with open(filepath+filename,'w',encoding='utf-8') as f:
        f.write(con.text)


