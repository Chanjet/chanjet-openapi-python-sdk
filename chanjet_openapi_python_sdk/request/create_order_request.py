# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 10:32
# @Author  : zc
# @Desc    : 代客下单请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class CreateOrderRequest(ChanjetRequest):

    def get_http_method(self):
        return 'post'
