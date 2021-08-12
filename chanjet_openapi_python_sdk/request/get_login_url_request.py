# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 14:35
# @Author  : zc
# @Desc    : 获取登录url请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class GetLoginUrlRequest(ChanjetRequest):

    def get_http_method(self):
        return 'get'
