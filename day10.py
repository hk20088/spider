#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='Leon Hu'

import logging
import time

logging.basicConfig(filename='example.log',format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG)

mor_hour = 6  # 早六点
eve_hour = 18 # 晚十点
minute = 13


def auto_weibo():
    while True:
        current_time = time.localtime()
        # 每天早上六点和晚上十点自动发微博
        if ((current_time.tm_hour == mor_hour) and (current_time.tm_min == minute)):
            logging.info('发早间微博，时间：%s' % (time.strftime('%Y-%m-%d %H:%M:%S')))
            print('发早间微博，时间：%s' % (time.strftime('%Y-%m-%d %H:%M:%S')))
            time.sleep(16 * 60 * 60)  # 16个小时之后继续运行（因为早上六点到晚上十点相差16个小时）
            continue;
        elif ((current_time.tm_hour == eve_hour) and (current_time.tm_min == minute)):
            logging.info('发晚间微博，时间：%s' % (time.strftime('%Y-%m-%d %H:%M:%S')))
            print('发晚间微博，时间：%s' % (time.strftime('%Y-%m-%d %H:%M:%S')))
            time.sleep(8 * 60 * 60)  # 8小时之后再继续运行（因为晚上十点到第二天早上六点相差8个小时 ）
            continue;
        else:
            logging.info(u'还没到时间...')
            print('还没到时间...')
            break;





if __name__ == '__main__':
    print(time.daylight)
    auto_weibo()