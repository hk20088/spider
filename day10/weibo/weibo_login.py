#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Leon Hu'

import json
import re
import rsa
import binascii
import base64
import requests

from day10.logger import logger
from day10.conf.confg import USER_NAME, USER_PAWD, WBCLIENT, USER_AGENT


weibo_prelogin_url = 'https://login.sina.com.cn/sso/prelogin.php?' \
                     'entry=weibo&callback=sinaSSOController.preloginCallBack&' \
                     'su=%s&rsakt=mod&client=%s'
weibo_login_url = 'https://login.sina.com.cn/sso/login.php?client=%s'

session = requests.session()
session.headers['User-Agent'] = USER_AGENT

def login():
    # 先获取登录必要的一些参数
    resp = session.get(weibo_prelogin_url % (base64.b64encode(requests.utils.quote(USER_NAME).encode('utf-8')),WBCLIENT))
    pre_login_str = re.match(r'[^{]+({.+?})', resp.text).group(1)
    pre_login_info = json.loads(pre_login_str)

    data = {
        'entry': 'weibo',
        'gateway': 1,
        'from':'',
        'savestate': 7,
        'useticket': 1,
        'vsnf': 1,
        'su': base64.b64encode(requests.utils.quote(USER_NAME).encode('utf-8')),
        'service':'miniblog',
        'servertime': pre_login_info['servertime'],
        'nonce': pre_login_info['nonce'],
        'pwencode': 'rsa2',
        'rsakv': pre_login_info['rsakv'],
        'sp': encrypt_passwd(USER_PAWD,pre_login_info['pubkey'],pre_login_info['servertime'],pre_login_info['nonce']),
        'encoding': 'UTF-8',
        'prelt': '18',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.si'
               'naSSOController.feedBackUrlCallBack',
        'returntype': 'META'
    }


    login_resp = session.post(weibo_login_url % WBCLIENT, data=data)
    login_resp.encoding = 'gbk' # 让结果以gbk编码方式输出
    logger.info('Post得到的结果是：%s' % login_resp.text)
    match_obj = re.search(r'replace\([\"\']([^\'\"]+)[\"\']', login_resp.text)
    if match_obj is None:
        print('登录失败，请检查登录信息')
        return (session, None)

    # 登录请求后，会返回登录页面，取里面的登录URL进行请求
    login_url_pre = match_obj.group(1)

    logger.info('post请求后获取到的URL1：%s' % login_url_pre)
    resp_pre = session.get(login_url_pre)
    resp_pre.encoding = 'gbk'
    logger.info('请求URL1得到的结果：%s' % resp_pre.text)

    # # 取到真正登录的URL，调用它就会返回用户的信息
    login_url = re.search(r'replace\([\"\']([^\'\"]+)[\"\']',resp_pre.text).group(1)

    logger.info('获取到真正登录的URL2：%s' % login_url)
    resp = session.get(login_url)
    resp.encoding = 'gbk'
    logger.info('请求URL2得到的结果：%s' % resp.text)

    login_str = login_str = re.search('\((\{.*\})\)', resp.text).group(1)
    login_info = json.loads(login_str)
    print('登录成功：%s' % str(login_info))
    uniqueid = login_info["userinfo"]["uniqueid"]
    return (session, uniqueid)



# 根据新浪的密码加密规则，将用户密码进行加密编译
def encrypt_passwd(passwd, pubkey, servertime, nonce):
    key = rsa.PublicKey(int(pubkey, 16), int('10001', 16))
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(passwd)
    passwd = rsa.encrypt(message.encode('utf-8'), key)
    return binascii.b2a_hex(passwd)


if __name__ == '__main__':
    (session, uid) = login()
