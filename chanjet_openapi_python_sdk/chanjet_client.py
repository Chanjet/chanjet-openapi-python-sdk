# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 畅捷通开放平台客户端
import json
import logging

import requests

from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent
from chanjet_openapi_python_sdk.chanjet_response import ChanjetResponse
from chanjet_openapi_python_sdk.exception.http_method_exception import HttpMethodException
from chanjet_openapi_python_sdk.exception.serialize_response_exception import SerializeResponseException


class ChanjetClient:

    def __init__(self, server_url, app_key='', app_secret='', open_token='', content_type='application/json', connect_timeout=3, read_timeout=15):
        self._server_url = server_url
        self._content_type = content_type
        self._open_token = open_token
        self._app_key = app_key
        self._app_secret = app_secret
        self._headers = {}
        # 设置链接超时时长，单位s
        self._connect_timeout = connect_timeout
        # 设置接口响应超时时长，单位s
        self._read_timeout = read_timeout
        # 请求方法对应的执行函数
        self._http_method_func = {
            'get': self._do_get,
            'post': self._do_post,
            'put': self._do_put,
            'delete': self._do_delete
        }

    # 获取请求头参数
    def get_request_headers(self):
        self._headers['appKey'] = self._app_key
        self._headers['appSecret'] = self._app_secret
        self._headers['openToken'] = self._open_token
        self._headers['Content-Type'] = self._content_type
        return self._headers

    # 设置请求头参数
    def add_request_headers(self, headers):
        self._headers.update(headers)

    # 设置单个请求头参数
    def add_request_header(self, key, value):
        self._headers[key] = value

    # 获取请求头app_key
    @property
    def app_key(self):
        return self._app_key

    # 设置请求头app_key
    @app_key.setter
    def app_key(self, app_key):
        self._app_key = app_key

    # 获取请求头app_secret
    @property
    def app_secret(self):
        return self._app_secret

    # 设置请求头app_secret
    @app_secret.setter
    def app_secret(self, app_secret):
        self._app_secret = app_secret

    # 获取请求头open_token
    @property
    def open_token(self):
        return self._open_token

    # 设置请求头open_token
    @open_token.setter
    def open_token(self, open_token):
        self._open_token = open_token

    # 获取请求头content_type
    @property
    def content_type(self):
        return self._content_type

    # 设置请求头content_type
    @content_type.setter
    def content_type(self, content_type):
        self._content_type = content_type

    # http异常处理方法
    def _handle_exception(self, res):
        try:
            res.raise_for_status()
            return True
        except requests.exceptions.HTTPError as e:
            logging.error(f'http请求错误: {e}')

    # post请求
    def _do_post(self, req):
        return requests.post(self._server_url + req.request_uri,
                             json=req.content,
                             headers=self.get_request_headers(),
                             timeout=(self._connect_timeout, self._read_timeout))

    # get请求
    def _do_get(self, req):
        return requests.get(self._server_url + req.request_uri,
                            params=req.get_query_params(),
                            headers=self.get_request_headers(),
                            timeout=(self._connect_timeout, self._read_timeout))

    # put请求
    def _do_put(self, req):
        return requests.put(self._server_url + req.request_uri,
                            json=req.content,
                            headers=self.get_request_headers(),
                            timeout=(self._connect_timeout, self._read_timeout))

    # delete请求
    def _do_delete(self, req):
        return requests.delete(self._server_url + req.request_uri,
                               params=req.get_query_params(),
                               headers=self.get_request_headers(),
                               timeout=(self._connect_timeout, self._read_timeout))

    # 执行请求的方法
    def execute(self, req, response_class=None):
        # 从request对象上获取请求方法，并找到对应的处理方法
        http_method = req.get_http_method().lower()
        func = self._http_method_func.get(http_method, False)
        if not func:
            raise HttpMethodException('仅支持get、post、put、delete请求方法')

        # 如果请求体是Content对象，则将对象转化为字典
        if isinstance(req.content, ChanjetContent):
            req.content = json.loads(json.dumps(req.content, default=lambda obj: obj.__dict__))

        logging.info(f'url: {self._server_url + req.request_uri}')
        logging.info(f'request-header: {str(self.get_request_headers())}')
        if http_method in ['get', 'delete']:
            logging.info(f'request-params: {str(req.get_query_params())}')
        else:
            logging.info(f'request-content: {str(req.content)}')

        # 发起请求
        res = func(req)
        self._handle_exception(res)

        # 如果传入Response类，则返回该类的实例并绑定返回数据，否则返回dict数据
        result = None
        if response_class:
            if issubclass(response_class, ChanjetResponse):
                result = json.loads(res.text, object_hook=response_class)
            else:
                raise SerializeResponseException(f"传入的'{response_class.__name__}'类不是'ChanjetResponse'的子类")
        else:
            result = json.loads(res.text)
        return result
