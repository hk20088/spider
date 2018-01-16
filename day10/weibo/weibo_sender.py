#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Leon Hu'

import time
import json
import re
from day10.logger import logger
from day10.conf.confg import MAX_IMAGES, ADD_WATERMARK, WATERMARK_URL, WATERMARK_NIKE

send_blog_url = 'https://weibo.com/aj/mblog/add?ajwvr=6&__rnd=%s'

def upload_img(session,images):
    pids = ''
    for image in images:
        pid = upload_img_stream(session, image)
        if pid:
            pids += " " + pid
        # time.sleep(10)
    return pids.strip()

def upload_img_stream(session,image_url):
    # 判断是否需要加水印
    if ADD_WATERMARK:
        url = "http://picupload.service.weibo.com/interface/pic_upload.php?\
                    app=miniblog&data=1&url=" \
              + WATERMARK_URL + "&markpos=1&logo=1&nick=" \
              + WATERMARK_NIKE + \
              "&marks=1&mime=image/jpeg&ct=0.5079312645830214"
    else:
        url = "http://picupload.service.weibo.com/interface/pic_upload.php?\
                    rotate=0&app=miniblog&s=json&mime=image/jpeg&data=1&wm="

    try:
        with open(image_url, 'rb') as f:
            img = f.read()
        resp = session.post(url,data=img)
        upload_json = re.search('{.*}}', resp.text).group(0)
        result = json.loads(upload_json)
        code = result["code"]
        if code == "A00006":
            pid = result["data"]["pics"]["pic_1"]["pid"]
            return pid

    except Exception as e:
        logger.error(u'上传图片失败：%s' % image_url)
    return None




def send_blog(session, uid, message,imgs):
    # session.headers['Referer'] = 'https://weibo.com/leonhuug/home?wvr=5&uut=fin&from=reg'
    session.headers['Referer'] = 'http://www.weibo.com/u/%s/home?wvr=5' % '6449528843'
    pids = upload_img(session,imgs)

    data = {
        'location': 'v6_content_home',
        'text': message,
        'appkey': '',
        'style_type':'1',
        'pic_id':pids,
        'tid':'',
        'pdetail':'',
        'rank':0,
        'rankid':'',
        'module':'stissue',
        'pub_source': 'main_',
        'pub_type': 'dialog',
        'isPri': 0,
        '_t': 0
    }

    resp = session.post(send_blog_url % time.time(), data = data)
    result = json.loads(resp.text)
    if(result['code'] == '100000'):
        logger.info('微博发送成功...')
    else:
        logger.error('微博发送失败...')


