#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='Leon Hu'

from splinter.browser import Browser
from bs4 import BeautifulSoup
import requests
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context  # 忽略 ssl 证书的验证

# b = Browser(driver_name='chrome')  # 使用chrome浏览器对应的驱动
# b.visit('http://baidu.com')  # 打开网页
# b.fill('wd','splinter')   #  搜索 splinter。 注意，wd 是百度搜索框的的name属性值
#
# but = b.find_by_id('su') # 根据id='su'找到 百度一下的按钮
# but.click() # 提交
#
# b.quit() # 退出

# -------------------- 分割线， 以上代码是练手用的，下面是实际抢票代码 ----------------------------------

username = '675293396@qq.com'
password = 'abc920318'

# 出发到达地点及出行日期，这些值可以先在浏览器模拟查询一次，然后在cookie里拿到
start_station ='%u6DF1%u5733%u5317%2CIOQ'
to_station = '%u6842%u6797%u5317%2CGBZ'
# to_station ='%u9A7B%u9A6C%u5E97%u897F%2CZLN'
train_date = '2017-12-30'

login_url = 'https://kyfw.12306.cn/otn/login/init'  # 登录页面
query_url = 'https://kyfw.12306.cn/otn/leftTicket/init'   # 查询页面
my12306_url = 'https://kyfw.12306.cn/otn/index/initMy12306' # 登录成功后会跳到这个页面
book_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc' #订票页面

b = Browser(driver_name='chrome')

# 登录
def login():
    b.visit(login_url)
    b.fill('loginUserDTO.user_name', username)
    b.fill('userDTO.password', password)

    # 等待用户输入验证码，登录成功后，会跳到 my12306_url。这里根据网址判断是否登录成功
    while True:
        if b.url == my12306_url:
            print('登录成功...')
            break
        else:
            continue

# 查询
def query():
    print('封装cookie...')
    b.cookies.add({'_jc_save_fromStation': start_station})
    b.cookies.add({'_jc_save_toStation': to_station})
    b.cookies.add({'_jc_save_fromDate': train_date})
    print('cookie封装完成,跳转到订票页面...')
    b.visit(query_url)

    print('自动填充查询信息,开始查询...')
    b.find_by_text(u'GC-高铁/城际').click() # 选择高铁
    b.find_by_id(u'query_ticket').click() # 查询
    print('查询完毕...')

# 订票逻辑
# 1、判断是否有可以预订的列车（利用BeautifulSoup）
# 2、如果有则按优先级预定（优先级自己设置）；如果没有，则再次查询，如此循环，直到查到票为止
def book_ticket():
    count =1
    while True:
        # 这里的判断方法不对，因为没票的车次也会有预订按钮，只不过按钮不可点。如果想到其它有效的判断方式再来修改。
        if b.is_element_present_by_text(u'预订'):
            break
        else:
            count +=1
            print('无票...开始第%s次查询' % count)
            #停三秒后，再次查询余票
            time.sleep(3)
            b.find_by_id(u'query_ticket').click()
            continue

    while True:
        # 说明有票，开始预订。这里默认预订第一张票
        b.find_by_text(u'预订')[0].click()
        print('开始订票...')
        if b.url == book_url:
            b.find_by_id(u'normalPassenger_0').click()  # 选择乘车人
            b.find_by_id(u'submitOrder_id').click()  # 提交订单
            b.find_by_id(u'qr_submit_id').click() # 确认订单
            print('订票成功...')
            break


if __name__ == '__main__':
    login()
    query()
    book_ticket()

