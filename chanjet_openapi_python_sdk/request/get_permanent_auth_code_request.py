# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 11:33
# @Author  : zc
# @Desc    : 获取企业永久授权码请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class GetPermanentAuthCodeRequest(ChanjetRequest):

    def get_http_method(self):
        return 'post'
