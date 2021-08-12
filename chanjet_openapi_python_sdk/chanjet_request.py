# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 畅捷通开放平台Request基类
from chanjet_openapi_python_sdk.exception.http_method_exception import HttpMethodException


class ChanjetRequest:

    def __init__(self, request_uri=''):
        self._query_params = {}
        self._request_uri = request_uri
        self._content = None

    # 获取请求参数
    def get_query_params(self):
        return self._query_params

    # 添加多个请求参数
    def add_query_params(self, query_params):
        self._query_params.update(query_params)

    # 添加单个请求参数
    def add_query_param(self, key, value):
        self._query_params[key] = value

    # 获取请求uri
    @property
    def request_uri(self):
        return self._request_uri

    # 设置请求uri
    @request_uri.setter
    def request_uri(self, request_uri):
        self._request_uri = request_uri

    # 获取请求体内容
    @property
    def content(self):
        return self._content

    # 设置请求体内容
    @content.setter
    def content(self, content):
        self._content = content

    # 获取http请求方法名
    def get_http_method(self):
        raise HttpMethodException('请重写父类的get_http_method方法')
