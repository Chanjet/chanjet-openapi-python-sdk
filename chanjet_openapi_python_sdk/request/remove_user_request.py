# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 16:12
# @Author  : zc
# @Desc    : 企业内移除用户请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class RemoveUserRequest(ChanjetRequest):

    def get_http_method(self):
        return 'post'
