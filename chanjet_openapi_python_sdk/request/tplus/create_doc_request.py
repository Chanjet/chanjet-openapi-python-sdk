# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 创建凭证请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class CreateDocRequest(ChanjetRequest):

    def get_http_method(self):
        return 'post'
