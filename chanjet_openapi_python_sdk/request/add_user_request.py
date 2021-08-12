# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 15:50
# @Author  : zc
# @Desc    : 企业内添加用户请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class AddUserRequest(ChanjetRequest):

    def get_http_method(self):
        return 'post'
