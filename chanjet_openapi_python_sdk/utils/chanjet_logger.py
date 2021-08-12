# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 9:17
# @Author  : zc
# @Desc    : 自定义日志配置器
import logging


class ChanjetLogger:

    def __init__(self, level):
        log_format = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(level=logging.DEBUG, format=log_format)
