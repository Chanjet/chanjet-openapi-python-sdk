# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 17:14
# @Author  : zc
# @Desc    : 获取用户token请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class GetUserTokenRequest(ChanjetRequest):

    def get_http_method(self):
        return 'post'

