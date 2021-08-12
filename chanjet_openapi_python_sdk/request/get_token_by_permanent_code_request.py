# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 16:57
# @Author  : zc
# @Desc    : 使用用户永久授权码获取token请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class GetTokenByPermanentCodeRequest(ChanjetRequest):

    def get_http_method(self):
        return 'post'
