#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Leon Hu'

import logging
from logging.handlers import RotatingFileHandler
from day10.conf.confg import ISLOGGER

logger = logging.getLogger('weibo') # 定义一个名为 weibo 的logger

if(ISLOGGER):
    # 定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
    # 实例化handler，注意要用 utf-8编码
    handler = RotatingFileHandler('weibo.log', maxBytes=10 * 1024 * 1024, backupCount=5, encoding='utf-8')

    fmt = "%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)s] - %(message)s"  # 定义日志格式
    formatter = logging.Formatter(fmt)  # 实例化formatter
    handler.setFormatter(formatter)  # 为hnadler添加formatter
    # handler.setLevel(logging.DEBUG) # 注意在 Python3中这样设置日志级别不生效，还是按默认级别 warning输出

    logger.addHandler(handler)  # 为logger添加handler
    logger.setLevel(logging.DEBUG)  # 设置日志级别

