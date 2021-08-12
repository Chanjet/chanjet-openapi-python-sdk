# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : json格式的response序列化成实例对象异常


class SerializeResponseException(Exception):
    def __init__(self, err_msg):
        super().__init__(self, err_msg)
