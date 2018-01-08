#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='Leon Hu'


import requests
import itchat
import random

KEY = '04f44290d4cf462aae8ac563ea7aac16'  # KEY有时效性，如果失效，可以到图灵机器人官网重新注册一个

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = '你好，主人不在，有事请留言。'
    robots=['——By机器人冰冰','——By机器人萌萌']
    reply = get_response(msg['Text'])+random.choice(robots)
    return reply or defaultReply

itchat.auto_login(enableCmdQR=True)
itchat.run()