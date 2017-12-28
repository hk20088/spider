#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='Leon Hu'

import requests
import os
import time
from bs4 import BeautifulSoup

url_home = 'https://www.liaoxuefeng.com'  # 主页
url_first = '/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'  # Python3教程首页

filepath = 'f:/python教程/'
imgpath = 'attachments/'

# 封装headers和cookies模拟浏览器请求，不然可能会报503
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}

cookies = {'Hm_lpvt_2efddd14a5f2b304677462d06fb4f964':'1514276914', 'Hm_lvt_2efddd14a5f2b304677462d06fb4f964':'1513759510,1513840593,1514170543,1514272126' }

# 请求网页函数
def request(url):
    return requests.get(url,headers=headers, cookies=cookies)

# 创建目录
def mkdir(path):
    path = path.rstrip('/')
    if not os.path.isdir(path):
        # os.mkdir(path) # 创建一级目录
        os.makedirs(path)  # 创建多级目录
        print('目录创建成功...')
    else:
        print('目录已存在...')

# 创建目录
mkdir(filepath + imgpath)

# 请求教程主页
res = request(url_home + url_first)
soup = BeautifulSoup(res.text, 'html.parser')
# 拿到教程左侧菜单栏的所有URL
hrefs = soup.find_all('a', class_='x-wiki-index-item')

start = time.time()
# 循环菜单栏URL，获取每页的内容
for h in hrefs:
    url_index = h['href']
    res = request(url_home + url_index)
    soup = BeautifulSoup(res.text, 'html.parser')

    # 只获取教程正文内容，过滤掉所有菜单栏及广告
    div_content = soup.find('div', class_='x-wiki-content x-main-content')

    # 将正文中的图片下载到本地，并将图片地址指向本地图片存放的地址
    imgs = div_content.find_all('img')
    for img in imgs:
        img_url = img['data-src']
        img_res = request(img_url)
        filename = img_url.split('/')[6]+'%s' % '.jpg'
        # 下载图片
        with open(filepath + imgpath + filename,'wb' ) as f:
            f.write(img_res.content)

        img['src'] = imgpath + filename  # 将img标签的src属性修改成本地图片地址
        del img['data-src'] # 删除img标签的 data-src 属性
        # img['class'] = 'democlass' # 给标签添加新属性


    result_name = 'python.html'
    with open(filepath + result_name,'a',encoding='utf-8') as f:
        f.write(str(div_content)) # 将div内容转化为str

end = time.time()
print('抓取完毕，使用时间 %s 秒' % (start - end))