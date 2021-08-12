# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 15:53
# @Author  : zc
# @Desc    : 企业内添加用户返回值实体
from chanjet_openapi_python_sdk.chanjet_response import ChanjetResponse


class AddUserResponse(ChanjetResponse):

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
            # 畅捷通企业ID
            self.orgId = ''
            # 畅捷通用户ID
            self.userId = ''
