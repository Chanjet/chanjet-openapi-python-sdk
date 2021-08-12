# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 16:37
# @Author  : zc
# @Desc    : 授权码换token请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class GetTokenRequest(ChanjetRequest):

    def get_http_method(self):
        return 'get'
