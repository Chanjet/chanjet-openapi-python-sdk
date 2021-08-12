# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 10:56
# @Author  : zc
# @Desc    : 获取当前cia用户的详细信息请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class GetCIAUserinfoRequest(ChanjetRequest):

    def get_http_method(self):
        return 'get'
