# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 10:05
# @Author  : zc
# @Desc    : 产品试用返回值实体
from chanjet_openapi_python_sdk.chanjet_response import ChanjetResponse


class TrailProductResponse(ChanjetResponse):

    def __init__(self, data=None):
        # 是否成功
        self.result = ''
        # 响应内容
        self.value = self.Value()
        # 错误信息，result为true时为null
        self.error = self.Error()

        if data:
            self.__dict__ = data

    def __str__(self):
        return str(self.__dict__)

    class Error:

        def __init__(self):
            # 错误码
            self.code = 0
            # 错误信息
            self.msg = ''
            # 错误提示
            self.hint = ''

    class Value:

        def __init__(self):
            # 订单号
            self.orderNo = ''
