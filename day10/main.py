#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='Leon Hu'

import time

from day10.logger import logger
from day10.weibo.weibo_login import login
from day10.weibo.weibo_sender import send_blog
from day10.conf.confg import MOR_HOUR, NO_HOUR, EVE_HOUR, MINUTE
import linecache
import random


# 定时
def timer():
    con = 0
    count = 1
    while True:
        current_time = time.localtime()
        # 每天早上六点和晚上十点自动发微博
        if ((current_time.tm_hour == MOR_HOUR) and (current_time.tm_min == MINUTE)):
            count += 1

            # 获取微博内容和配图并发送微博
            mor_mess = linecache.getline('conf/morning.txt',count).strip() + '【早安，世界】'
            img_url = 'imgs/cats/{0}.jpg'.format(count)
            imgs = [img_url]
            send_weibo(mor_mess,imgs)

            logger.info('发早间微博，时间：%s，内容：%s' % (time.strftime('%Y-%m-%d %H:%M:%S'),mor_mess))
            time.sleep(16 * 60 * 60)  # 6个小时之后继续运行（因为早上六点到中午十二点相差6个小时）
            continue
        # elif ((current_time.tm_hour == NO_HOUR) and (current_time.tm_min == MINUTE)):
        #     count += 1
        #     logger.info('发午间微博，时间：%s' % (time.strftime('%Y-%m-%d %H:%M:%S')))
        #     send_weibo('')
        #     time.sleep(10 * 60 * 60) # 10个小时之后发晚间微博
        #     continue
        elif ((current_time.tm_hour == EVE_HOUR) and (current_time.tm_min == MINUTE)):
            count += 1

            # 获取内容和配图并发送微博
            eve_mess = linecache.getline('conf/eveing.txt', count).strip() + '【晚安，世界】'
            img_url = 'imgs/dogs/{0}.jpg'.format(count)
            imgs = [img_url]
            send_weibo(eve_mess,imgs)

            logger.info('发晚间微博，时间：%s,内容：%s' % (time.strftime('%Y-%m-%d %H:%M:%S'), eve_mess))
            time.sleep(8 * 60 * 60)  # 8小时之后再继续运行（因为晚上十点到第二天早上六点相差8个小时 ）
            continue
        else:
            if(con < 1):
                con += 1
                logger.info(u'还没到时间...')
                strs = linecache.getlines('conf/morning.txt')
                mes = random.choice(strs)
                img_url = 'imgs/{0}/{1}.jpg'.format(random.choice(['cats','dogs']), random.choice(range(1,100)))
                imgs = [img_url]
                send_weibo(mes,imgs)
            time.sleep(30)
            continue

# 发送微博
def send_weibo(message,imgs):
    (session, uid) = login()
    send_blog(session, uid, message,imgs)


if __name__ == '__main__':
    timer()

