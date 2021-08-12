# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 10:59
# @Author  : zc
# @Desc    : 获取应用凭证请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class GetAppAccessTokenRequest(ChanjetRequest):

    def get_http_method(self):
        return 'post'
