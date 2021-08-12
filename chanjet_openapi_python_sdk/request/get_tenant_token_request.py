# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 16:38
# @Author  : zc
# @Desc    : 获取租户token请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class GetTenantTokenRequest(ChanjetRequest):

    def get_http_method(self):
        return 'post'
