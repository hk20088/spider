#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='Leon Hu'

import requests
from bs4 import BeautifulSoup


url = 'http://www.tuku.cn/bizhi/page2.aspx'
res = requests.get(url)
# print(res)   # 打印出<Response [200]>
# print(res.text)  # 打印出html页面

soup = BeautifulSoup(res.text, 'html.parser')  # html.parser是html 解析器

# 找到网页中a标签，且标签的href='tuji2715.aspx'的节点。[0]是因为find_all返回的是一个list集合，取第一个，也就是我们想要的
imgs = soup.find_all('a',href='tuji2715.aspx')[0]

# 从imgs集合中获取属性 src 的值 。 集合内容类似：<img alt="熊出没桌面壁纸" src="http://img.tuku.cn/file_image/201709/m2017091209220438.jpg"/>
img = imgs.find('img')['src']


# 下载图片
img_res = requests.get(img)
with open('f://imgs//dog.jpg','wb') as f:  # wb表示写入二进制文件
    f.write(img_res.content)
