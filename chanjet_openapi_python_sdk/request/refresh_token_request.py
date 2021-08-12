# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 14:01
# @Author  : zc
# @Desc    : 刷新开放平台token请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class RefreshTokenRequest(ChanjetRequest):

    def get_http_method(self):
        return 'get'
