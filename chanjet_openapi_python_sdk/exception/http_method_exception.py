# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : http请求方法异常


class HttpMethodException(Exception):
    def __init__(self, err_msg):
        super().__init__(self, err_msg)
