#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='Leon Hu'

import requests
import os
from bs4 import BeautifulSoup
from time import time
from multiprocessing import Pool

'''
思路：1、我们要抓取图库网上的动物图片100张  http://www.tuku.cn/bizhi/tuji2715.aspx
2、共4页，我们利用for循环抓取每一页的内容
3、图片以数字命名
4、图片下载到本地磁盘的某个目录下
'''
#
# filepath = 'f://imgs//'
# n =1 # 初始化的文件名
# start = time()
# print(start)
# for i in range(1,5):
#     url = 'http://www.tuku.cn/bizhi/tuji2715_page{0}.aspx'.format(i)
#     res = requests.get(url)
#
#     soup = BeautifulSoup(res.text, 'html.parser')
#     imgs = soup.find_all('div', class_='disp_img1')  # 属性class后为什么要加个下划线
#
#     for im in imgs:
#         _img = im.find_all('img')[0]['src']
#         _img_res = requests.get(_img)
#         filename = '{0}.{1}'.format(n, 'jpg')  # 文件路径
#         with open(filepath + filename, 'wb') as f:
#             f.write(_img_res.content)
#         n+=1
# end = time()
# print(end)
# print((end- start) +'s')

def parser_html(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    imgs = soup.find_all('div', class_='disp_img1')
    downimg(imgs)

filepath = 'f://imgs//'
def downimg(imgs):
    for im in imgs:
        number = im.find('img')['alt'][12:-9].strip()  # 解析出数字给图片命名
        _img = im.find('img')['src']
        _img_res = requests.get(_img)
        filename = '{0}.{1}'.format(number,'jpg')

        if not os.path.exists(filename):
            with open(filepath+filename, 'wb') as f:
                f.write(_img_res.content)


if __name__=='__main__':
    start = time()
    p = Pool(4)
    for i in range(1,5):
        url = 'http://www.tuku.cn/bizhi/tuji2715_page{0}.aspx'.format(i)
        p.apply_async(parser_html(url))

    p.close()
    p.join()
    end = time()
    print(start - end)


