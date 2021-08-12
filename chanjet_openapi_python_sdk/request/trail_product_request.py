# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 10:03
# @Author  : zc
# @Desc    : 产品试用请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class TrailProductRequest(ChanjetRequest):

    def get_http_method(self):
        return 'post'
