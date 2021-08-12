# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 15:24
# @Author  : zc
# @Desc    : 创建租户请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class CreateTenantRequest(ChanjetRequest):

    def get_http_method(self):
        return 'post'
