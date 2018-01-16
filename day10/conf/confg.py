#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='Leon Hu'

# 定时发微博的时间
MOR_HOUR = 6  # 早六点
NO_HOUR = 12  # 中午十二点
EVE_HOUR = 22 # 晚十点
MINUTE = 00

MAX_IMAGES = 0                      # 允许上传图片的最大数量。如果设置为0，则不上传图片。
ADD_WATERMARK = False               # 是否添加图片水印，为True时，应设置以下两项
WATERMARK_NIKE = "@微博"             # 水印名称
WATERMARK_URL = "weibo.com"         # 水印链接

# 用户名密码
USER_NAME = 'hk20088@126.com'
USER_PAWD = 'LeonHuug180111'

# 系统配置
WBCLIENT = 'ssologin.js(v1.4.19)'

# 是否开启日志
ISLOGGER = True

USER_AGENT = (
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/63.0.3239.132 Safari/537.36'
)